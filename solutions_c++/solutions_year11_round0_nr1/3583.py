#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <string>
#include <numeric>
#include <iostream>
#include <sstream> 
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define ll long long
#define ull unsigned long long
#define ld long double
#define VV vector
#define VI VV<int>
#define VL VV<ll>
#define VS VV<string>
#define MP(x,y) make_pair(x,y)
#define LET(a,b) typeof(b) a=(b)
#define SS(a) ((int)((a).size()))
#define PUB push_back
#define POF pop_front
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND=0;
#define DBG(x){if(COND>0){COND--;cerr<<__LINE__<<" "<<#x<<" "<<x<<endl;cerr.flush();}}

#define REP(i,n) FOR(i,0,(n)-1)
#define FOR(i,a,b) for(ll i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(ll i=(a),_b=(b);i>=_b;--i)
#define FORE(a,b) for(LET(a,(b).begin());a!=(b).end();++a)

#define two(X) (((ll)1)<<(X))
template<class T> inline void mini(T &a,T b){if(b<a)a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a)a=b;}
template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T gcd(T a,T b){if(a<0)a=-a;if(b<0)b=-b;return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){if(a<0)a=-a;if(b<0)b=-b;return a*(b/gcd(a,b));}
template<class T> inline VV<pair<T,int>> factorize(T n)
	{VV<pair<T,int>> R;T _i=1;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.PUB(MP(i,C));}
	i+=_i;_i=2;if (i*i>n) i=n;}if (n>1) R.PUB(MP(n,1));return R;}
template<class T> inline bool prime(T n)
	{if(n<=1)return false;T _i=1;for (T i=2;i*i<=n;i+=_i,_i=2) if (n%i==0) return false;return true;}

//----------------------------------------------


int cmd[100][2];
int tt[100];
int pos[2];
int N;

int go() {
	int tm = 0;
	CLR(tt,0);
	pos[0] = pos[1]=1;
	REP (i, N) {
		int d = abs(pos[cmd[i][0]] - cmd[i][1]);
		DBG(pos[cmd[i][0]]);
		DBG(cmd[i][1]);
		DBG(d);
		pos[cmd[i][0]] = cmd[i][1];
		int t = 0;
		for(ll j=i-1; j >= 0 && cmd[j][0]!=cmd[i][0]; j--)
			t+=tt[j];
		DBG(t);
		if (t>=d) tt[i]=1;
		else tt[i] = d-t + 1;
		DBG(tt[i]);
		tm += tt[i];
//		DBG(tm);
	}

	DBG(tm);
	return tm;
}

int solve() {
	cin >> N;
	DBG(N);
	CLR(cmd,0);
	REP (i, N) {
		char c; cin >> c >> cmd[i][1];
		cmd[i][0] = c == 'O' ? 0: 1;
		//DBG(cmd[i][0]);
		//DBG(cmd[i][1]);
	}
	//getline(cin,line);
	return go();
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
	COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
	int caseCount; cin >> caseCount;
	string temp; getline(cin,temp);
	FOR (c, 1, caseCount) {
		printf("Case #%lld: %d\n", c, solve());
		//printf("Case #%d: %d\n", 1, solve());
	}
	return 0;
}
