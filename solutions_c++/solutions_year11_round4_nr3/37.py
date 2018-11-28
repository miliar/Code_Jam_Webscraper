//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 1000 * 1000 + 10;

bool prm[MAX_N];
vector<int> allp;

int main(){
	memset(prm, 1, sizeof prm);
	prm[1] = 0;
	for(int i = 2; i < MAX_N; i++)
		if(prm[i]){
			allp.PB(i);
			for(int j = 2 * i; j < MAX_N; j += i)
				prm[j] = false;
		}
	
	int testN;
	cin >> testN;
	FOR(test, testN){
		long long n;
		cin >> n;
		if(n == 1){
			printf("Case #%d: 0\n", test + 1);
			continue;
		}
		long long ans = 1;
		for(int i = 0; i < SZ(allp) && allp[i] <= n; i++){
			int cnt = 0;
			long long mlt = 1;
			while(mlt * allp[i] <= n){
				mlt *= allp[i];
				cnt++;
			}
			if(cnt)
				ans += cnt - 1;
		}
		printf("Case #%d: %d\n", test + 1, (int)ans);
	}
	return 0;
}
