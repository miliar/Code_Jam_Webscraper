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
const int MAXN = 1100;
int X,S,R,t,N;
vector<PII> l;

double v[MAXN];
int main(){
	int T;
	cin >> T;
	REP(Case,1,T+1){
		cin >> X >> S >> R >> t >> N;
		l.clear();
		REP(i,0,N){
			int b,e,w;
			cin>>b>>e>>w;
			l.push_back( m_p( w, e-b ) );
			X -= (e-b);
		}
		if(X)l.push_back( m_p( 0, X ) );
		sort(l.begin(),l.end());

		double ans = 0;
		double rest = t;
		REP(i,0,l.size()){
			double lth = l[i].second;
			double w = l[i].first;
		//	printf(" lth=%.4lf w=%.4lf\n",lth,w);
			double et = lth / (R+w);
			if ( et <= rest ){
				rest -= et;
				ans += et;
			}else{
				double rlth = (R+w) * rest;
				ans += rest;
				rest-= rest;
				ans += (lth-rlth)/(S+w);
			}
		}

		printf("Case #%d: %.8f\n",Case,ans);
	}
	return 0;
}
