using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define oo 1<<30
#define f first
#define s second
#define II inline
#define db double
#define ll long long
#define pb push_back
#define mp make_pair
#define Size(V) ((int)(V.size()))
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define REP(i, N) for (int (i)=0;(i)<(int)(N);++(i))
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define IN "code.in"
#define OUT "code.out"
#define N_MAX (1<<14)

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int T,N;
vector<pi> V(N_MAX);

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	scanf("%d",&T);
}

II void solve(int TestCase)
{
	scanf("%d",&N);
	FOR(i,1,N)
		scanf("%d%d",&V[i].f,&V[i].s);
	
	int rez = 0;
	FOR(i,1,N)
	FOR(j,i+1,N)
		if( (V[i].f < V[j].f && V[i].s > V[j].s) || (V[i].f > V[j].f && V[i].s < V[j].s) )
			++rez;
	
	printf("Case #%d: %d\n",TestCase,rez);
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}

