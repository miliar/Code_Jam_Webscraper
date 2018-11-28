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

const int MAXN = 1200;
int n;
int a[MAXN];
bool vis[MAXN];

int main(){
	int T; cin >>T;
	REP(Case,1,T+1){
		cin>>n;
		REP(i,0,n){
			cin>>a[i];
			a[i]--;
		}

		int ans = 0;

		memset(vis,false,sizeof(vis));

		REP(i,0,n)if(!vis[i]){
			vis[i] = true;
			if ( a[i] == i )
				;
			else{
				int j = a[i];
				int l = 1;
				vis[j] = true;
				while ( j != i ){
					j = a[j];
					vis[j] = true;
					l++;
				}
				ans += l;
			}
		}

		double rans = ans*1.0;
		printf("Case #%d: %.10lf\n",Case,rans);
	}
	return 0;
}
