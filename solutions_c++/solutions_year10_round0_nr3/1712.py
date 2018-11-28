
#include <stdio.h>

int r, k, n;
int g[1000];
int number[1000];
int next[1000];

int solve()
{
	__int64 res;
	int i, pre, front, num, mcount;
	
	//‘§¥¶¿Ì
	for(i = 0; i < n; i++)
	{
		pre = -1;
		num = 0;
		mcount = 0;
		front = i;
		while(num <= k && mcount <= n)
		{
			num += g[front];
			pre = front; 
			front = (front + 1) % n;
			mcount++;
		}
		num -= g[pre];
		number[i] = num;
		next[i] = pre;
	}

	front = 0;
	res = 0;
	for(i = 0; i < r; i++)
	{
		res += number[front];
		front = next[front];
	}
	return res;
}

int main()
{
	int t, case_num;
	int i;
	__int64 res;
	scanf("%d", &t);
	for(case_num = 1; case_num <= t; case_num++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for(i = 0; i < n; i++)
		{
			scanf("%d", &g[i]);
		}
		res = solve();

		printf("Case #%d: %I64d\n", case_num, res);

	}
	return 0;
}