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

vector<PII> seq;
int n;

int main(){
	int T;
	cin >> T;
	
	REP(Case,1,T+1){
		cin >> n;
		seq.clear();
		REP(i,0,n){
			string ts; int tv;
			cin>>ts>>tv;
			seq.push_back( make_pair( ts=="O"?0:1, tv ) );
		}

		int aim[2];
		for( int i = n-1; i >= 0; i-- )
			aim[ seq[i].first ] = seq[i].second;

		int cr[2] = {1,1};

		int ptr = 0, ans = 0;
		while ( ptr < n ){
			bool found = false;
			REP( x,0,2 ){
				if ( seq[ptr].first == x && seq[ptr].second == cr[x] ){
					for( int i = ptr + 1; i < n; i++ )
						if ( seq[i].first == x ){
							aim[x] = seq[i].second;
							break;
						}
					found = true;
				}else{
					if ( cr[x] > aim[x] )
						cr[x]--;
					else if ( cr[x] < aim[x] )
						cr[x]++;
				}
			}
			if ( found )
				ptr ++;
			ans++;
		}

		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
