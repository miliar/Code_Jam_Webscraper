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
#define ll __int64//long long
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

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int T;
ll A,B,C;

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	scanf("%d",&T);	
}

II void solve(int TestCase)
{
	scanf("%I64d%I64d%I64d",&A,&B,&C);
	
	int sol = 0,rez = 0;
	
	for(;A * (ll)C < B;)
	{
		++rez;
		A = A * (ll)C; //ask for A * C, worst case is no
	}
	
	++rez;
	int aux = 1;
	for(;aux < rez;++sol,aux *= 2);
	
	printf("Case #%d: %d\n",TestCase,sol);
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}

