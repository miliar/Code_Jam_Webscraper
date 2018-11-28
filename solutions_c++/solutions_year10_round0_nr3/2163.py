#include <stdio.h>
#define N 1001
int head[N];
int queue[N];
int money[N];
int r, k, n;
int main()
{
	int t, i, j, m, sum, p, header;
	int circle, circle_money, ans;
	//freopen("test.in", "r", stdin);
	freopen("C-small-attempt0.in.txt", "r", stdin);
	freopen("C-small-attempt0.out.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		if(scanf("%d %d %d", &r, &k, &n) == EOF) break;
		for(j = 0; j < n; j++)
		{
			scanf("%d", queue + j);
		}
		for(j = 0; j <= n; j++)
		{
			head[j] = -1;
			money[j] = 0;
		}
		head[0] = 0;
		header = 0;
		m = 0;		
		while(m < r)
		{
			sum = 0; p = 0;
			while(p < n && k >= sum + queue[(header + p) % n])
			{
				sum += queue[(header + p) % n];
				p++;
			}
			if(m == 0) money[0] = sum;
			else money[m] = money[m-1] + sum;
			header += p;			
			m++;
			if(head[header % n] >= 0) break;
			else head[header % n] = m;			
		}
		if(m >= r)
		{
			printf("Case #%d: %d\n", i + 1, money[r-1]);
		} else {
			m--;
		
			circle = m - head[header % n] + 1;
			if(head[header % n] > 0) {
				circle_money = money[m] - money[head[header % n] - 1];
			} else {
				circle_money = money[m];
			}
		
			ans = 0;						
			if(head[header % n] > 0){
				ans = money[head[header % n] - 1];				
				r -= head[header % n];
			} 
			ans += circle_money * (r / circle);
			if(r % circle > 0)
			{
				if(head[header % n] > 0) {
					ans += money[head[header % n] + r % circle - 1] - money[head[header % n] - 1];
				} else {
					ans += money[head[header % n] + r % circle - 1];
				}
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}		
	}
	return 0;
}