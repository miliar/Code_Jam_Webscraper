/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

template<class T>
void check_max( T&a, T b ){
	if ( a <  b ) a = b;
}
template<class T>
void check_min( T&a, T b ){
	if ( a > b ) a = b;
}

//#define debug
int g(int x){return x&-x;}
const int MAXP = 12,MAXN=1<<(MAXP+1);
typedef long long ll;
int m[MAXN];
ll c[MAXN];
ll f[MAXN][MAXP];
int p,n;
int main(){
	int T;scanf("%d",&T);
	REP(Case,1,T+1){
		scanf("%d",&p);
		for( int i = (1<<p); i < 2*(1<<p); i++ )
			scanf("%d",m+i);
		memset(f,0x2f,sizeof(f));
		for( int i = (1<<p); i < 2*(1<<p);i++ ){
			for( int k = 0; k <= min(m[i],p); k++ )
				f[i][k] = 0;
		}
		for( int l = p-1; l >= 0; l-- ){
			for( int i = 1<<l; i <2*(1<<l); i++ )
				scanf("%lld",c+i);
		}
		for( int i = (1<<p)-1; i > 0;i-- ){
			for( int k = 0; k <= p; k++ ){
				check_min( f[i][k] , f[i*2][k+1]+f[i*2+1][k+1] );
				check_min( f[i][k], c[i]+f[i*2][k]+f[i*2+1][k] );
			}
#ifdef debug
			cout << "f["<<i<<"]: ";
			REP(k,0,p+1)cout<< f[i][k]<<" ";
			cout << endl;
#endif
		}
#ifdef debug
		REP(i,1,2*(1<<p)){
			if(i<(1<<p))
				cout << c[i] << " ";
			else
				cout << m[i] << " ";
			if ( g(i+1) == i+1 ) cout << endl;
		}
#endif
		ll ans = 0x2f2f2f2f2f2f2f2f;
		for( int k = 0; k <= p; k++ )
			check_min( ans, f[1][k] );
		printf("Case #%d: %lld\n",Case,ans);
	}
	return 0;
}
