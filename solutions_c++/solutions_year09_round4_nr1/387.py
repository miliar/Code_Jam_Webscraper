#include <stdio.h>

#define SIZE_N		50

int n, ans;
char matrix[SIZE_N][SIZE_N];
int cnt[SIZE_N];

void process()
{
	int i, j, k;
	int t;
	
	for(i = 0; i < n; i++)
	{
		for(j = n-1; j >= 0; j--)
			if(matrix[i][j] == '1') break;
		cnt[i] = j;
	}
	ans = 0;
	for(i = 0; i < n-1; i++)
	{
		if(cnt[i] <= i) continue;
		for(j = i+1; j < n; j++)
		{
			if(cnt[j] <= i) break;
		}
		for(; j > i; j--)
		{
			ans++;
			t = cnt[j];
			cnt[j] = cnt[j-1];
			cnt[j-1] = t;
		}
	}
}

int main()
{
	int t, casecnt;
	int i, j;

	scanf("%d", &t);
	for(casecnt = 0; casecnt < t; casecnt++)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%s", matrix[i]);
		process();
		printf("Case #%d: %d\n", casecnt + 1, ans);
	}

	return 0;
}