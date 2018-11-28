/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
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

#define LET(x,a) __typeof(a) x (a)
#define ITER(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOREACH(it,v) ITER(it,v.begin(),v.end())

#define FILLA(a,x) memset(&a,x,sizeof(a))
#define FILL(a,x) memset(a,x,sizeof(a))
#define CLEARA(a,x) FILLA(a,0)
#define CLEAR(a) FILL(a,0)

#define m_p make_pair
#define fst first
#define snd second
typedef pair<int,int> PII;
typedef long long ll;
template<class T> void check_max( T&a, T b ){ if ( a < b ) a = b; }
template<class T> void check_min( T&a, T b ){ if ( a > b ) a = b; }

//#define debug
const int MAXSN = 1000000+10;

bool isp[MAXSN];
ll n;
int main(){
	memset(isp,true,sizeof(isp));
	isp[0] = isp[1] = false;
	REP(i,2,MAXSN) if ( isp[i] )
		for( int j = i+i; j <MAXSN;j+=i )
			isp[j]=false;
	int T;
	cin >> T;
	REP(Case,1,T+1){
		cin >> n;
		
		ll ans = n==1?0:1;
		for( ll i = 2; i*i <= n; i++ ) if ( isp[i] ){
			ll v = i;
			int mi = 1;
			while(v*i<=n){
				mi++;
				v*=i;
			}
			ans += mi-1;
		}

		printf("Case #%d: %lld\n",Case,ans);
	}
	return 0;
}
