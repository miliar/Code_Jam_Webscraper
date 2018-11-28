#include <cstdio>
#include <cstring>
#include <cstdlib>
#define MAXN 2005

static int a[MAXN];
static int next[MAXN];
static int g[MAXN];
int gc;

char CheckIt (int l, int r)
{
	//printf("%d..%d -",l,r);
	int i;
	//for (i = l; i <= r; i++) printf(" %d",a[i]);
	//printf("\n");
	if (l >= r) return 1;
	char isOne = 0;
	for (i = l; i < r; i++)
	{
		if (next[i] == r) isOne = 1;
		if (next[i] > r) return 0;
	}
	if (!isOne) return CheckIt(l,r-1);
	int j;
	for (i = l; i < r; i++) a[i]--;
	g[0] = r-1;
	gc = 1;
	for (i = r-1; i >= l; i--)
	{
		if (next[i] == r)
		{
			g[gc] = i;
			gc++;
		}
	}
	g[gc] = l-1;
	for (i = 0; i < gc; i++)
	{
		int step = ((a[r] - a[g[i]]) + (r - g[i] - 1)) / (r - g[i]);
		for (j = g[i]-1; j > g[i+1]; j--)
		{
			a[j] = a[j+1] - step;
		}
	}
	int prev = r;
	for (i = r-1; i >= l; i--)
	{
		if (next[i] == r)
		{
			if (!CheckIt(i+1, prev)) return 0;;
			prev = i;
		}
	}
	if (!CheckIt(l, prev)) return 0;
	return 1;
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		int N;
		scanf("%d",&N);
		int i;
		for (i = 0; i < (N-1); i++)
		{
			scanf("%d",&(next[i]));
			(next[i])--;
		}
		for (i = 0; i < N; i++) a[i] = 1000000000;
		printf("Case #%d:",iT+1);
		if (!CheckIt(0,N-1)) printf(" Impossible\n");
		else
		{
			for (i = 0; i < N; i++) printf(" %d",a[i]);
			printf("\n");
		}
	}
	return 0;	
}
