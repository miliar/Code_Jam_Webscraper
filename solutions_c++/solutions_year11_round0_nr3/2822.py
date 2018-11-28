#include <stdio.h>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>

using namespace std;

#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) (EQ((a).real(),(b).real()) && EQ((a).imag(),(b).imag()))

typedef complex<double> P;
typedef long long ll;

const int MAX_SIZE = 10000;

int T;
int N;

int maxNum = 0;
vector<int> C;
vector<bool> flags;
int cnt = 0;

void dfs(int p){
//	cout << cnt++ << endl;

	if(p >= N - 1)
		return;

	int sum = 0;
	int maxVal = -1;
	for(int i = 0; i < N; i++){
		if(flags[i])
			sum += C[i];
		else{
			maxVal = max(maxVal,C[i]);
		}
	}
	// 一番左のビット
	int idx = 0;
	int cnt = 1;

	int tmp = maxVal;
	while(maxVal > 0){
		if(maxVal & 1)
			idx = cnt;
		maxVal >>= 1;
		cnt++;
	}

	int mv = (1 << idx) - 1;
	if(mv < sum)
		return;

	for(int i = p; i < N; i++){
		flags[i] = true;

		// チェック
		int calc[2];
		int all[2];
		calc[0] = calc[1] = 0;
		all[0] = all[1] = 0;
		for(int j = 0; j < N; j++){
			if(flags[j]){
				all[0] += C[j];
				calc[0] ^= C[j];
			}
			else{
				all[1] += C[j];
				calc[1] ^= C[j];
			}
		}
		if(calc[0] == calc[1])
			maxNum = max(maxNum,max(all[0],all[1]));

		// 再帰
		dfs(i+1);
		flags[i] = false;
	}

}

int main(){

	ifstream ifs("input.txt");
	ofstream ofs("output.txt");

	ifs >> T;
	for(int i = 0; i < T; i++){
		ifs >> N;
		for(int j = 0; j < N; j++){
			int tmp;
			ifs >> tmp;
			C.push_back(tmp);
		}

		flags.clear();
		maxNum = 0;
		for(int i = 0; i < N; i++)
			flags.push_back(false);
		// solve()
		dfs(0);
		if(maxNum != 0)
			ofs << "Case #" << i + 1 << ": " << maxNum << endl;
		else
			ofs << "Case #" << i + 1 << ": " << "NO" << endl;
		C.clear();
	}

	//int x;
	//cin >> x;

	return 0;
}