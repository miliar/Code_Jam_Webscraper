#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=b;--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(a) (int(a.size()))
#define CLEAR(array,c) memset(array,c,sizeof(array))
#define pb push_back
#define mp make_pair

#define debug(x) cerr<< #x << " = " << (x) << "\n";
#define debugv(v) cerr << #v << " = "; FOREACH(it,v) cerr << *it <<","; cerr << "\n";

template<typename T> inline void checkMax(T& a, T b) {if (b>a) a=b;}
template<typename T> inline void checkMin(T& a, T b) {if (b<a) a=b;}

typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<string> VS;
typedef pair<int,int> ii;
typedef long double ld;
const int INF = 1000000000;
const int INFLL = LL(INF)*LL(INF);
const double EPS = 1e-9;


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Case;
	cin >> Case;
	REP(_i, Case){
		int m;
		vector<ii> v;
		int P,K,L;
		cin >> P >> K >> L;
		REP(_j,L){cin >> m; v.pb(mp(m,0));}
		sort(v.rbegin(),v.rend());
		FOREACH(it,v){cerr<<it->first<<" "<<it->second<<endl;}
		bool test = true;
		REP(i,L){
			int tt = i/K + 1;
			v[i].second = tt;
			if(tt > P) {test = false; break;}
		}
		LL ret = 0;
		FOREACH(it,v){
			cerr<<it->first<<" "<<it->second<<endl;
			ret+=it->first*it->second;
		}
		if(test) cout<<"Case #"<<_i+1<<": "<<ret<<endl;
		else cout<<"Case #"<<_i+1<<": "<<"Impossible"<<endl;
	}
	
}