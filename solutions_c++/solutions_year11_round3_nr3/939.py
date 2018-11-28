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
int L,H,N;
vector<int> fr;


int solve(){
	string no = "NO";
	for(int i = L; i <= H; i++){
		bool isOK = true;
		for(int j = 0; j < fr.size(); j++){
			if(!(fr[j] % i == 0 || i % fr[j] == 0)){
				isOK = false;
				break;
			}
		}
		if(isOK)
			return i;
	}

	return -1;
}

int main(){

	ifstream ifs("input.txt");
	ofstream ofs("output.txt");

	ifs >> T;
	for(int i = 0; i < T; i++){
		ifs >> N >> L >> H;
		for(int j = 0; j < N; j++){
			int tmp;
			ifs >> tmp;
			fr.push_back(tmp);
		}
		ofs << "Case #" << i+1 << ": " << flush;
		//cout << "Case #" << i+1 << ": " << flush;
		int ret = solve();
		if(ret == -1){
			ofs << "NO" << endl;
			//cout << "NO" << endl;
		}
		else{
			ofs << ret << endl;
			//cout << ret << endl;
		}
		fr.clear();
	}

	int x;
	cin >> x;

	return 0;
}