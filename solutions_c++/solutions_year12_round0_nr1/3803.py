/**
	offline
	A name (Code: Speaking-in-Tongues)
	Source: GCJ 2012
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <iterator>
#include <algorithm>
#include <functional>
#include <string>
#include <map>
#include <vector>
#include <set>

typedef long long ll;
typedef long long unsigned llu;

#define	_min(a,b)	((a)<(b)?(a):(b))
#define _max(a,b)	((a)>(b)?(a):(b))

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define REP(i,n) FOR(i,0,n)

#define MOD 1000000007
#define INF (int)1e9
#define EPS 1e-9

#define IT(a,it) for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define pb push_back
#define mp make_pair

// #define DEBUG

#ifdef DEBUG
	std::string tabs;
	#define INDENT		tabs+="\t"
	#define _EXIT(val)	{ UNINDENT; return val; }
	#define UNINDENT	tabs.erase(tabs.length()-1)
	#define SHOW(x)		cout << tabs << x
	#include <time.h>
	#define STARTTIME	clock_t start = clock();
	#define GETTIME		printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
	#define _DEBUG(x)	x
#else
	#define INDENT
	#define _EXIT(val)	return val
	#define UNINDENT
	#define SHOW(x)
	#define STARTTIME
	#define GETTIME
	#define _DEBUG(x)
#endif

using namespace std;

char code[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'}; 

void solve()
{
	int t = GI;
	while (t--)
	{
		
	}
}

char src[101];
char dest[101];

void solve_saving()
{
	int t = GI; scanf("\n");
	REP(i, t)
	{
		memset(src, 0, sizeof(src));
		memset(dest, 0, sizeof(dest));
		
		cin.getline(src, 101, '\n');
		int len = strlen(src);
		
		REP (j, len)
		{
			if ( (src[j] >= 'a') && (src[j] <= 'z') )
				dest[j] = code[src[j] - 'a'];
			else
				dest[j] = src[j];
		}
		cout << "Case #" << i+1 << ": " << dest << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
