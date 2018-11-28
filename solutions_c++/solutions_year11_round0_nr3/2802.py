#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define MAXN 1024

int n;
int c[MAXN];

int bt(int i, int s1, int s2, int t1, int t2)
{
	if (i == n && s1 == s2 && t1 && t2)
	{
		return max(t1, t2);
	}
	if (i == n)
	{
		return -1;
	}
	
	return max(bt(i+1, s1 ^ c[i], s2, t1 + c[i], t2), bt(i+1, s1, s2 ^ c[i], t1, t2 + c[i]));
}

int main (void)
{
	int teste;
	scanf ("%d", &teste);
	
	for (int t = 1; t <= teste; ++t)
	{
		scanf ("%d", &n);
		
		for (int i = 0; i < n; i++)
		{
			scanf ("%d", &c[i]);
		}
		
		int ans = bt(0, 0, 0, 0, 0);
		
		printf ("Case #%d: ", t);
		if (ans < 0)
		{
			printf ("NO\n");
		}
		else
		{
			printf ("%d\n", ans);
		}
	}

	return 0;
}

