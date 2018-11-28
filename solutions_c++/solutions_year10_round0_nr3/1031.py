#include <stdio.h>

const int NSIZE = 1100;
int r, k, n;
int g[NSIZE];
long long ans;

void process()
{
	int i, j, l, p, cnt;
	int check[NSIZE];
	long long sum[NSIZE], midsum;
	int itv[NSIZE][2];

	ans = p = cnt = 0;
	for(i = 0; i < n; i++) check[i] = 0;
	for(i = 0; i < r; i++)
	{
		itv[cnt][0] = p;
		sum[cnt] = g[p];
		for(j = (p+1) % n; j != p; j = (j+1) % n)
		{
			if(sum[cnt] + g[j] > k) break;
			sum[cnt] += g[j];
		}
		itv[cnt][1] = j;
		p = j;
		ans += sum[cnt++];
		for(j = 0; j < cnt; j++)
		{
			if(itv[j][0] == itv[cnt-1][1]) break;
		}
		if(j < cnt) break;
	}
	if(i >= r) return;
	i++;
	midsum = 0;
	for(l = j; l < cnt; l++)
		midsum += sum[l];
	ans += ((r-i) / (cnt-j)) * midsum;
	i += ((r-i) / (cnt-j)) * (cnt-j);
	for(l = 0; i < r; i++, l++)
		ans += sum[j+l];
}

int main()
{
	int t, i, z;

	z = 1;
	scanf("%d", &t);
	while(t > 0)
	{
		scanf("%d %d %d", &r, &k, &n);
		for(i = 0; i < n; i++)
			scanf("%d", &g[i]);
		process();
		printf("Case #%d: %lld\n", z++, ans);
		t--;
	}

	return 0;
}