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

map<int,int> mp;
int ans;
void deal( int v ){
	if ( mp[v] <= 1 ) return;
	mp[v-1] ++;
	mp[v+1] ++;
	mp[v]--;mp[v]--;
	ans++;
	deal(v-1);
	deal(v+1);
	deal(v);
}
int main(){
	int T;cin>>T;
	REP(Case,1,T+1){
		int k;cin>>k;
		mp.clear();
		ans = 0;
		REP(i,0,k){
			int v,p;
			cin >>v >>p;
			mp[v] += p;
			deal(v);
		}
		cout << "Case #"<<Case<<": "<<ans<<endl;
	}
	return 0;
}
