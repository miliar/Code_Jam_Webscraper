#include<iostream>

using namespace std;

int d[100];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int R, k, N;
	int cas, icas, i;
	scanf("%d", &cas);
	for(icas = 1; icas <= cas; icas++)
	{
		scanf("%d %d %d", &R, &k, &N);
		int maxn = 0, sum = 0, maxi = -1;
		for(i = 1; i <= N; i++)
		{
			scanf("%d", &d[i]);
			if(d[i] > maxn) maxn = d[i], maxi = i;
			sum += d[i];
		}
		int res = 0;
		if(sum <= k)
		{
			res = R*sum;
			printf("Case #%d: %d\n", icas, res);
			continue;
		}
		res = 0;
		int tsum = 0;
		int cnt = 0;
		for(i = 1; i <= N; i= i%N+1)
		{
			tsum += d[i];
			if(tsum > k)
			{
				tsum -= d[i];
				res += tsum;
				tsum = 0;
				i--;
				cnt++;
				if(cnt == R)
					break;
			}
		}
		printf("Case #%d: %d\n", icas, res);
	}
	return 0;
}