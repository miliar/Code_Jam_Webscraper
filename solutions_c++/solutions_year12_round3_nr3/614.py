/* GCJ 2012 1C - imiro */
#define OYE using namespace std
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>

OYE;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<char> vc;
typedef vector<string> vs;

#define SQR(a) ((a)*(a))
#define REP(i,s,n) for(int (i)=(s), _n = (n);(i)<_n;(i)++)
#define FOR(i,s,n) for(int (i)=(s), _n = (n);(i)<=_n;(i)++)
#define rep(i,n) REP(i,0,n)

#define All(v) (v).begin(), (v).end()
#define Reversed(v) (v).rbegin(), (v).rend()
#define sz(v) (int) v.size()

#define mp make_pair
#define pb push_back
#define ji first
#define ro second

#define SI ({int x; scanf("%d", &x); x;})

inline void OPEN(string a, bool out = false) {
	freopen(string(a + ".in").c_str(), "r", stdin);
	if(out) freopen(string(a + ".out").c_str(), "w", stdout);
}

#define EPS 1e-7

#define MAX 105
ll A[MAX][2], B[MAX][2];
ll Aa[MAX][2], Bb[MAX][2];
int n, m;

int main() {
	int TT = SI;
	FOR(T,1,TT) {
		printf("Case #%d: ", T);
		n = SI, m = SI;
		
		rep(i,n) { cin >> A[i][0] >> A[i][1]; }
		rep(i,m) { cin >> B[i][0] >> B[i][1]; }
		
		if(n==3) {
			if(A[0][1] == A[1][1] && A[0][1] == A[2][1]) {
				n = 1;
				A[0][0] += A[1][0] + A[2][0];
			}
			else if(A[0][1] == A[1][1]) {
				n = 2;
				A[0][0] += A[1][0];
				A[1][0] = A[2][0];
				A[1][1] = A[2][1];
			}
			else if(A[1][1] == A[2][1]) {
				n = 2;
				A[1][0] += A[2][0];
			}
		}
		
		if(n==1) {
			ll ans = 0LL;
			rep(i,m) if( A[0][1] == B[i][1] ) {
				ans += min(A[0][0], B[i][0]);
				if(A[0][0] > B[i][0]) A[0][0] -= B[i][0];
				else break;
			}
			cout << ans << endl;
		} else if(n==2) {
			ll best = 0LL;
			FOR(jj,0,m) { // item 1 sebanyak j
				ll tmp = 0LL;
				rep(i,n) Aa[i][0] = A[i][0], Aa[i][1] = A[i][1];
				rep(i,m) Bb[i][0] = B[i][0], Bb[i][1] = B[i][1];
				
				int i = 0, j = jj, k = m-jj;
				while(i < m && j) {
					if(Aa[0][1] == Bb[i][1]) {
						tmp += min(Aa[0][0], Bb[i][0]);
						if(Aa[0][0] > Bb[i][0]) Aa[0][0] -= Bb[i][0];
						else { Aa[0][0] = 0; i = jj-1; ++k; break; }
					}
					--j; ++i;
				}
				
				while(i < m && k) {
					if( Aa[1][1] == Bb[i][1] ) {
						tmp += min(Aa[1][0], Bb[i][0]);
						if(Aa[1][0] > Bb[i][0]) Aa[1][0] -= Bb[i][0];
						else { Bb[i][0] -= Aa[1][0]; break; }
					}
					--k; ++i;
				}
				best = max(best, tmp);
			}
			cout << best << endl;
		} else {
			ll best = 0LL; // puts("");
			FOR(jj,0,m) { // item 1 sebanyak j
				int r = m-jj; // remaining items
				FOR(kk,0,r) {
					ll tmp = 0LL;
					rep(i,n) Aa[i][0] = A[i][0], Aa[i][1] = A[i][1];
					rep(i,m) Bb[i][0] = B[i][0], Bb[i][1] = B[i][1];
				//	rep(i,n) cout << Aa[i][0] << " " << Aa[i][1] << " "; cout << endl;
				//	rep(i,m) cout << Bb[i][0] << " " << Bb[i][1] << " "; cout << endl;
					
					int i = 0, j = jj, k = kk, z = r-k;
					while(i < m && j) {
						if(Aa[0][1] == Bb[i][1]) {
							tmp += min(Aa[0][0], Bb[i][0]);
							if(Aa[0][0] > Bb[i][0]) Aa[0][0] -= Bb[i][0];
							else { 
								Bb[i][0] -= Aa[0][0]; 
								if(!k && Aa[0][1] == Aa[2][1]) {
									++z;
									i = jj-1; 
								}
								else i = jj;
								break; 
							}
						}
						--j; ++i;
					}
				//	printf("%d - %I64d, ", jj, tmp);
					
					while(i < m && k) {
						if( Aa[1][1] == Bb[i][1] ) {
							tmp += min(Aa[1][0], Bb[i][0]);
							if(Aa[1][0] > Bb[i][0]) Aa[1][0] -= Bb[i][0];
							else {Aa[1][0] = 0; }
						}
						--k; ++i;
					}
				//	printf("%d - %I64d, ", kk, tmp);
					
					while(i < m && z) {
						if(Aa[2][1] == Bb[i][1]) {
							tmp += min(Aa[2][0], Bb[i][0]);
							if(Aa[2][0] > Bb[i][0]) Aa[2][0] -= Bb[i][0];
							else Aa[2][0] = 0;
						}
						--z; ++i;
					}
				//	printf("%d - %I64d, ", r-kk, tmp);
				//	cout << tmp << endl;
					best = max(best, tmp);
				}
			}
			cout << best << endl;
		}
	}
	return 0;
}