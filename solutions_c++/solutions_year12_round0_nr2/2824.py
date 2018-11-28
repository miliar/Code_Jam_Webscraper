#include <climits>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

#define REP(i,n)    for(int i=1;i<=(n);++i)
#define FORE(i,e,n) for(int i=(e);i<(n);++i)
#define FOR(i,n)    for(int i=0;i<(n);++i)

#define _(A,v) memset(A,v,sizeof(A))
#define all(A)  (A).begin(), (A).end()
#define rall(A) (A).rbegin(),(A).rend()
#define pb push_back

bool ok(int a, int b, int c) {
	if(abs(a - b) > 2) return false;
	if(abs(a - c) > 2) return false;
	if(abs(b - c) > 2) return false;
	return true;
}

bool sur(int a, int b, int c) {
	int cnt = 0;
	if(abs(a - b) == 2) ++cnt;
	if(abs(a - c) == 2) ++cnt;
	if(abs(a - b) == 2) ++cnt;
	if(abs(b - c) == 2) ++cnt;
	return cnt;
}

int main() {
	freopen("d.in",  "r", stdin);
	freopen("d.out", "w", stdout);

	int n, s, p;
	int ss, m, cnt;
	int S[128];
	int C[128][2];	// encontrado 1, encontrado supr 2, no encontrado 0
	bool B[128];
	int tt;
	cin>>tt;
	REP(t,tt) {
		printf("Case #%d: ", t);
		_(S, 0);
		_(C, 0);
		_(B, false);
		cnt = 0;
		ss = 0;
		cin>>n>>s>>p;
		FOR(i, n) cin>>S[i];
		
		FOR(g, n) {
			FOR(i, 11) {
				FOR(j, 11) {
					FOR(k, 11) {
						if(!ok(i, j, k)) continue;
						if(max(i, max(j, k)) < p) continue;
						if(i + j + k == S[g]) {
							if(sur(i, j, k)) 	++C[g][1];
							else 				++C[g][0];
						}
					}
				}
			}
		}
		FOR(i, n) {
			if(C[i][0] == 0 && C[i][1]) {
				B[i] = true;
				if(ss < s) {
					++cnt;
					++ss;
				}
			}
		}
		FOR(i, n) {
			if(!B[i] && C[i][0]) ++cnt;
		}
		cout << cnt << endl;
	}
	return 0;
}
