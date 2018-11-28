#include <stdio.h>
#include <string.h>

int MAX_VAL = 1000000;

int cas = 0;
int	T;
int n;

int num[26];
int ans[26];

int test(int state, int sz)
{
	int i=0;
	int rank = 0;

	memset(num, 0xff, sizeof(num));
	for (i=0; i<sz; i++)
	{	
		if (state & (1 << i))
		{
			num[i+2] = ++rank;
		}
	}

	int step = sz + 1;	
	
	do
	{
		if (num[step] == -1)		
			return 0;
		step = num[step];
	} while (step != 1);
	return 1;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int i, j, k;

	for (i=0; i<26; i++)
		num[i] = i;

	int cnt;
	for (k=2; k<=25; k++)
	{
		int all = k - 1;
		int sz = 1 << all;
		cnt = 0;
		for (i=0; i<sz; i++)
		{
			cnt += test(i, all);
		}
		//printf("%d\n", cnt);
		ans[k] = cnt % 100003;
	}	

	scanf("%d", &T);	
	while (T--)
	{
		scanf("%d", &n);				
		printf("Case #%d: %d\n", ++cas, ans[n]);		
	}
	return 0;
}