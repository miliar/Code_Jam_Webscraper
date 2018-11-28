#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long LL;

#define sz(c) ((int) (c).size ())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

#define next(x) ((x + 1) % N)

int R, k, N;
int g[1005], ne[1005], s[1005];

int main ()
{
	int T;
	scanf ("%d", &T);
	for (int test = 1; test <= T; test++)
	{
		printf ("Case #%d: ", test);	
		scanf ("%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; i++)
			scanf ("%d", &g[i]);
		for (int i = 0; i < N; i++)
		{
			int j = (i + N - 1) % N, t = 0;
			s[i] = 0;
			while (t < N && s[i] + g[next (j)] <= k)
			{
				j = next (j);
				s[i] += g[j];
				t++;
			}
			ne[i] = next (j);
		}
		int i = 0;
		LL res = 0;
		while (R--)
		{
			res += s[i];
			i = ne[i];
		}
		printf ("%lld\n", res);
	}
	return 0;
}

