#pragma comment(linker, "/STACK:100000000")
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cctype>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b); ++i)

typedef long long i64;
typedef unsigned long long u64;

void cnt (int x, int dx[10])
{
	while (x)
	{
		int d = x % 10;
//		if (dx[d] == -1) dx[d] = 0;
		++dx[d];
		x /= 10;
	}
}

int nextBF(int x)
{
		int dx[11], dy[11];
		memset(dx, 0, sizeof(dx));
		cnt(x, dx);

		FOR(y,x+1,1000000000)
		{
			memset(dy, 0, sizeof(dy));
			cnt(y,dy);
			bool ok = true;
			FOR(i,1,10) if (dx[i] != -1 && dx[i] != dy[i]) ok = 0;
			if (ok)
			{
				return y;
			}
		}
}

string nextF(string s)
{
	if (!next_permutation(s.begin(), s.end()))
	{
		s.push_back('0');
		sort(s.begin(), s.end());
		FOR(i,0,s.size())
			if (s[i] != '0')
			{
				swap(s[0], s[i]);
				break;
			}
	}
	return s;
}

string intToStr(int x)
{
	char ts[100];
	sprintf(ts, "%d", x);
	return ts;
}

int main()
{
	//freopen("a.in", "rt", stdin);
	//freopen("a.out", "wt", stdout);

	int T;

	

	scanf("%d", &T);
	FOR(cas, 1, T+1)
	{
		/*
		int x;
		scanf("%d", &x);
		printf("Case #%d: %d\n", cas, nextBF(x));
		fprintf(stderr, "Case #%d\n", cas);
		*/
		if (cas == 33)
		{
			cas = cas;
		}
		char xs[25];
		scanf("%s", xs);
		printf("Case #%d: %s\n", cas, nextF(xs).c_str());
		fprintf(stderr, "Case #%d\n", cas);
	}

	return 0;
}
	