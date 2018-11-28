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

const int MAXN = 1010;
int a[MAXN];
int n;

map<int,int> cnt;

int deal( int st ){
	int cv = a[st];
	int i = st;
	a[st] = 0;
	int cl = 1;
	vector<int> used;
	used.push_back( cv );
	while ( true ){
		while ( i < n && a[i] < cv+1 )
			i++;
		if ( i == n || ( i < n && a[i] > cv+1 ) || 
			( i<n&&a[i]==cv+1&&cnt[cv+1]<cnt[cv]) ){
				break;
		}
		cv = a[i];
		a[i] = 0;
		cl++;
		used.push_back( cv );
	}
	REP(i,0,used.size()){
		cnt[ used[i] ]--;
	}
	return cl;
}

int main(){
	int T; cin >> T;
	REP(Case,1,T+1){
		cin>>n;
		REP(i,0,n) cin >> a[i];

		sort(a,a+n);
		
		REP(i,0,n) cnt[a[i]]++;

		int ans = n;
		for( int i = 0; i < n ; ){
			check_min( ans, deal(i) );
			while ( i < n && a[i] == 0 ) i++;
		}

		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
