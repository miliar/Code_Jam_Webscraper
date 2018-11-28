#include<iostream>
#include<cstring>
#include<stdlib.h>
#include<algorithm>

using namespace std;

#define MAX 1005

struct Node
{
	int l, r;
}w[MAX];

bool cmp(Node a, Node b)
{
	return a.l < b.l;
}

int main(void)
{
	int cas, sum, n;

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &cas);

	for (int t = 1; t <= cas; t++)
	{
		scanf("%d", &n);

		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &w[i].l, &w[i].r);
		}

		sort (w, w+n, cmp);

		sum = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = i +1; j < n; j++)
				if (w[j].r < w[i].r)
					sum++;
		}
		printf("Case #%d: %d\n", t, sum);
	}
}