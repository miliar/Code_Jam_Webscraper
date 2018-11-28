#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <deque>
#include <cmath>
#include <queue>
#include <sstream>

using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define FOREACH(it,v) for(typeof(v.begin()) it=v.begin();it != v.end();it++)
#define FORN(i,x,y) for(int i=(x);i<(y);++i)
#define FOR(i,x) FORN(i,0,x)
#define ALL(a) (a).begin(),(a).end()
#define SET(x,a) memset(x,a,sizeof x)
#define VEC vector
#define PB push_back
#define MP make_pair

template<class T,class U> inline void checkmin(T& x,U y){x=min(x,(T)y);};
template<class T,class U> inline void checkmax(T& x,U y){x=max(x,(T)y);};

const int maxn = 1105 ;
int n ;;
lint B[maxn] , E[maxn] , X , T , R , S , W[maxn];
lint sT[256] ;
int main(){
	int cas ;
	cin >> cas ;
	for(int cs = 1; cs <= cas ; cs ++){
		cin >> X >> S >> R >> T >> n ;
		memset(sT , 0 ,sizeof sT );
		sT[0] = X ;
		for(int i = 0 ; i < n ; i ++){
			cin >> B[i] >> E[i] >> W[i];
			lint dist = E[i] -B[i] ;
			sT[0] -= dist ;
			sT[W[i]] += dist ;
		}
		double ans = 0 ,rem = T ;
		for(int i = 0 ; i < 256 ; i ++){
			double cdist = sT[i] , tak = min(rem , sT[i]*1.0 / (R + i));
			rem -= tak ; ans += tak ; cdist -= tak * (R + i);
			ans += cdist / (S + i) ; 
		}
		printf("Case #%d: %.8f\n", cs , ans );
	}
	return 0 ;
}
