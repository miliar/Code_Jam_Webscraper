#include <stdio.h>
#include <algorithm>

using namespace std;

int t;
int n;
int rez;
int v1[1000];
int v2[1000];

void Init()
{
	n = 0;
	rez = 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Init();
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%d", &v1[j]);
		for (int j = 0; j < n; j++)
			scanf("%d", &v2[j]);
		sort(v1, v1 + n);
		sort(v2, v2 + n);
		for (int j = 0; j < n; j++)
			rez += v1[j] * v2[n - j - 1];
		printf("Case #%d: %d\n", i + 1, rez);
	}
	return 0;
}