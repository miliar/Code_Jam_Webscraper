/**
	offline
	C name (Code: Recicled-Numbers)
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

void solve()
{
	int t = GI;
	while (t--)
	{
		
	}
}

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		int a = GI;
		int b = GI;
		
		int size = 0;
		int t = a;
		int mul = 1;
		while (t)
		{
			size++;
			t /= 10;
			mul *= 10;
		}
		mul /= 10;
		
		set<int> used;

		long long unsigned sol = 0;
		
		SHOW(a << " -a b- " << b << " size:" << size << " mul: " << mul << endl);
		
		FOR (j, a, b+1)
		{
			int amount = 0;
			used.insert(j);
			t = j;
			
			SHOW( j << endl );
			INDENT;
			
			REP (k, size-1)
			{
				int number = mul * (t % 10) + t / 10;
				t = number;
				if (number >= a && number <= b)
					if (used.find(number) == used.end())
					{
						SHOW(number << endl);
						used.insert(number);
						amount++;
					}
			}
			
			UNINDENT;
			
			sol += (amount * (amount + 1)) / 2;
		}
		
		cout << "Case #" << i+1 << ": " << sol << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
