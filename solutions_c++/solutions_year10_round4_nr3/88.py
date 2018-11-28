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
const int MAXN = 120;
bool f[MAXN][MAXN],g[MAXN][MAXN];
int n;
char buf[MAXN+1];
int r;
int main(){
	int T;scanf("%d",&T);
	REP(Case,1,T+1){
		memset(f,false,sizeof(f));
		scanf("%d",&r);
		REP(i,0,r){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			x1++;x2++;y1++;y2++;
			REP(x,x1,x2+1)REP(y,y1,y2+1)
				f[x][y] = true;
		}
		n = 100+2;
		int ans = 0;
		while ( true ){
			bool ok = false;
			REP(i,0,n)REP(j,0,n) if (f[i][j])ok=true;
			if (!ok)break;
			ans++;
			memset(g,0,sizeof(g));
			REP(i,1,n)REP(j,1,n){
				if ( f[i][j] ){
					if( !f[i-1][j] && !f[i][j-1] )
						g[i][j] = false;
					else
						g[i][j] = true;
				}else{
					if( f[i-1][j] && f[i][j-1] )
						g[i][j] = true;
					else
						g[i][j] = false;
				}
			}
			memcpy(f,g,sizeof(g));
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
