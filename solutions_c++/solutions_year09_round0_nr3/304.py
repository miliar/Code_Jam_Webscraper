#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

int pd[600][30];
char IN[600];

int main() {

	string S = "welcome to code jam";
	int n;
	scanf("%d\n", &n);
	FOR(t,n) {
		printf("Case #%d: ", t+1);
		fgets(IN, 550, stdin);
		string in(IN);
		in.erase(sz(in)-1, 1);
//		printf("\n LHI %s\n" , in.c_str());
		memset(pd, 0, sizeof(pd));
		FOR(i,600) pd[i][0] = 1;
		FOR(i, sz(in)) {
			FOR(j, sz(S)-1) {
				if(S[j] == in[i]) {
					for(int k=i+1; k < sz(in); k++) {
						if(in[k] == S[j+1]) {
							pd[k][j+1] += pd[i][j];
							pd[k][j+1] %= 100000;
						}
					}
				}
			}
		}

		int r = 0;
		FOR(i,sz(in)) {
			if(in[i] == 'm') {
				r += pd[i][sz(S)-1];
				r %= 100000;
			}
		}
		r %= 10000;
		if(r < 1000) printf("0");
		if(r < 100) printf("0");
		if(r < 10) printf("0");
		printf("%d\n", r);
	}

    return 0;
}

