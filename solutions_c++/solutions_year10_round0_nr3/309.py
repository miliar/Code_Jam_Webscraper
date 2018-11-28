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
const int MAXN = 2000;
typedef long long ll;
int g[MAXN],r,k;
int n;
ll sum[MAXN];//at g
ll asum;
int mark[MAXN];
int main(){
	int t;
	scanf("%d",&t);
	REP(Case,1,t+1){
		scanf("%d%d%d",&r,&k,&n);
		//k people one time, r times
		//n group
		REP(i,0,n) scanf("%d",g+i);

		asum = 0;
		REP(i,0,n) asum += g[i];

		memset(sum,0,sizeof(sum));
		memset(mark,0,sizeof(mark));
		int ps = 0, cnt = 0;
		ll ans = 0;
		int rr = r;
		while ( rr ){
			if ( mark[ps] ){
				int copy = rr/(cnt-mark[ps]+1);
				ans += (ans-sum[ps])*copy;
				rr %= (cnt-mark[ps]+1);
				memset(sum,0,sizeof(sum));
				memset(mark,0,sizeof(mark));
			}
			if ( !rr ) break;
			int nps = ps; ll rm = k;
			sum[ps] = ans;
			
			if ( rm >= asum ){
				rm -= asum;
				ans += asum;
			}else			
				while ( rm >= g[nps] ){
					rm -= g[nps];
					ans += g[nps];
					nps = ( nps+1 ) % n;
				}
			cnt++;
			mark[ps] = cnt;
			ps = nps;
			rr--;
		}
		cout << "Case #"<<Case<<": "<<ans<<endl;
	}

	return 0;
}
