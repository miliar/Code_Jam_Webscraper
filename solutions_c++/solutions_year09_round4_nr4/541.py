using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define pb push_back
#define size(V) ((int)(V.size()))
#define f first
#define s second
#define II inline
#define ll long long
#define db double
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N) for (int i = 0; i < (int)(N); ++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define mp make_pair
#define oo 1<<30

#define IN "code.in"
#define OUT "code.out"

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}
typedef vector<string> VS;

int T;
vector< pair<int,pi> > V;

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	scanf("%d",&T);
}

II void solve()
{
	
}

II db dist(int x1,int y1,int x2,int y2)
{
	db a = (x1 - x2) * (x1 - x2);
	db b = (y1 - y2) * (y1 - y2);
	
	return sqrt(a + b);
}

II void solve_brute(int TestCase)
{
	V.resize(0);
	
	int N;
	scanf("%d",&N);
	
	int x,y,r;
	V.pb( mp(0,mp(0,0) ) );
	FOR(i,1,N)
	{
		scanf("%d %d %d\n",&x,&y,&r);
		V.pb( mp(r,mp(x,y) ) );
	}
	
	db rez = oo;
	
	if(N == 3)
	{
		rez = min( max(dist(V[1].s.f,V[1].s.s,V[2].s.f,V[2].s.s) + V[1].f + V[2].f,(db)V[3].f ), rez );
		rez = min( max(dist(V[2].s.f,V[2].s.s,V[3].s.f,V[3].s.s) + V[2].f + V[3].f,(db)V[1].f ), rez );
		rez = min( max(dist(V[1].s.f,V[1].s.s,V[3].s.f,V[3].s.s) + V[1].f + V[3].f,(db)V[2].f ), rez );
	}
	if(N == 2)
	{
		rez = max(V[1].f * 2,V[2].f * 2);
	}
	if(N == 1)
		rez = V[1].f * 2;
	
	printf("Case #%d: %lf\n",TestCase,rez / 2);
}

int main()
{
	scan();
	FOR(i,1,T)
		solve_brute(i);
	return 0;
}
