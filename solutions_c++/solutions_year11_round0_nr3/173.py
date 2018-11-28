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
const int MAXN = 1000;
int a[MAXN];
int n;

const int MAXBIT = 20;
int f[2][1<<MAXBIT];

int main(){
	int T; cin >> T;
	REP(Case,1,T+1){
		cin >> n;
		REP(i,0,n) cin >> a[i];
		
		int all_xor = 0;
		REP(i,0,n) all_xor ^= a[i];
		
		int all_sum = 0;
		REP(i,0,n) all_sum += a[i];
		
		bool solvable = true;
		int ans = 0;
		if ( all_xor != 0 ){
			solvable = false;
		}else{
			int maxs = 1<<MAXBIT;
			
			memset(f,-1,sizeof(f));
			f[0][0] = 0;
			REP(i,0,n){
			//	memset( f[(i+1)%2],-1,sizeof(f[(i+1)%2]) );
				REP(s,0,maxs)if(f[i%2][s]>-1){
					check_max( f[(i+1)%2][s^a[i]], f[i%2][s] + a[i]);
					check_max( f[(i+1)%2][s], f[i%2][s] );
				}
			}
			
			ans = -1;
			REP(s,1,maxs-1)if(f[n%2][s]>-1 && s==(all_xor^s) )
				check_max( ans, f[n%2][s] );

			if ( ans == -1 ) solvable = false;
		}

		fprintf(stderr,"Case #%d\n",Case);
		printf("Case #%d: ",Case);
		if ( !solvable )
			puts("NO");
		else
			printf("%d\n",ans);
	}
	return 0;
}
