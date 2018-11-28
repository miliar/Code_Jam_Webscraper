#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;
typedef long long LL ;
const LL INF = 2000*1000*1000+100 ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
char t[200][200] ;
double odp[200] ;
double OWP[200] ;
double WP[200][200] ; 
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ":" << endl ;
		int n, i, j, k ;
		cin >> n ;
		REP(i,n)
			REP(j,n) cin >> t[i][j] ;
		REP(i,n) {
			REP(j,n) {
				double ile=0 ;
				double win=0;
				REP(k,n) {
					if(j==k) continue ;
					if(t[i][k]!='.') ile++ ;
					if(t[i][k]=='1') win++ ;
				}
				WP[i][j] = win/ile ;
			}
		}
		REP(i,n) {
			double ile=0 ;
			double s=0 ;
			REP(j,n) {
				if(t[i][j] != '.') {
					ile ++ ;
					s += WP[j][i] ;
				}
			}
			OWP[i] = s/ile ;
		}
		REP(i,n) {
			odp[i] = 0.25*WP[i][i] + 0.5*OWP[i] ;
			double s=0, ile=0 ;
			REP(j,n) {
				if(t[i][j]!='.') {
					ile ++ ;
					s += OWP[j] ;
				}
			}
			odp[i] += 0.25*s/ile ;
		}
		cout.setf(ios::fixed) ;
		cout.precision(8) ;
		REP(i,n) cout << odp[i] << endl ;
	}
}

