#include<stdio.h>
#include<string.h>
char flag[2000001];
int a, b;
int digit_num(int x)
{
	int ret = 0;
	while( x /= 10)
		ret++;
	return ret;
}

int pow10(int num)
{
	int ret = 1;
	for(int i = 0;i < num; i++)
	{
		ret *= 10;
	}
	return ret;
}

int count(int x)
{
	flag[x] = 0;
	int num = 1;
	int dnum = digit_num(x);
	int base = pow10(dnum);
	for(int i = 0;i < dnum; i++)
	{
		x = (x % 10) * base + (x / 10);
		if(x > base && x >=a && x <= b && flag[x])
		{
			flag[x] = 0;
			num += 1;
		}
	}
	return num * (num - 1) / 2;
}

void solveC()
{
	int t;
	
	int res;
	scanf("%d\n", &t);
	
	for(int i = 1; i <= t; i++)
	{
		scanf("%d%d", &a, &b);
		memset(flag, -1, sizeof(flag));
		res = 0;
		for(int i = a; i <= b ; i++)
		{
			res += count(i);
		}
		printf("Case #%d: %d\n", i, res);
	}
}

int main()
{
	solveC();
	return 0;
}