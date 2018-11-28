#include <stdio.h>
#define MAX_GROUP_PEOPLE 1000
int test,t, r, k, n, nextPointer[MAX_GROUP_PEOPLE];
long long g[MAX_GROUP_PEOPLE], sum[MAX_GROUP_PEOPLE];
long long ans;

void init()
{
	scanf ("%d%d%d", &r, &k, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &g[i]);
}

void process()
{
	// preprocess
	for(int i = 0; i < n; i++)
	{
		sum[i] = 0;
		bool endMark = false;
		for(int j = i; j < n; j++)
			if (sum[i] + g[j] <= k)
				sum[i] += g[j];
			else
			{
				nextPointer[i] = j;
				endMark = true;
				break;
			}

		if (!endMark)
			for ( int j = 0; j < i; j++)
				if (sum[i] + g[j] <= k)
					sum[i] += g[j];
				else
				{
					nextPointer[i] = j;
					endMark = true;
					break;
				}

		if (!endMark)
			nextPointer[i] = i;
	}

	//simulation
	ans = 0;   
	long long nowPosition = 0;
	for (int i = 0; i < r; i++)
	{
		ans += sum[nowPosition];
		nowPosition = nextPointer[nowPosition];
	}
}

void print()
{
	printf ( "Case #%d: %lld\n", test + 1, ans);
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf ("%d", &t);
	for (test = 0; test < t; test++)
	{
		init();
		process();
		print();
	}
}