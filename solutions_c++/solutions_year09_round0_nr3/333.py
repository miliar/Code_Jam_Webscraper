#include <iostream>
using namespace std;

int s[600] , a[600] , n;

int lowbit(int r)
{
	return r & (-r);
}

void update(int d , int v)
{
	while(d <= n)
	{
		s[d] += v;
		s[d] %= 10000;
		if(s[d] < 0)
			s[d] += 10000;
		d += lowbit(d);
	}
}

int sum(int d)
{
	int all;
	all = 0;
	while(d > 0)
	{
		all += s[d];
		if(all >= 10000)
			all %= 10000;
		d -= lowbit(d);
	}
	return all;
}

char date[600];

char mark[100] = "welcome to code jam";

int main()
{
	int i , j , t , cas = 0 , b , ans , k;
	freopen("3.txt" , "w" , stdout);
	scanf("%d" , &t);getchar();
	while(t --)
	{
		memset(s , 0 , sizeof(s));
		memset(a , 0 , sizeof(a));
		gets(date);
		n = strlen(date);
		for(k = 0 ; mark[k] != '\0' ; k ++)
		{
			for(i = n - 1 ; i >= 0 ; i --)
			{
				b = sum(i);
				update(i + 1 , -a[i]);
				a[i] = 0;
				if(date[i] != mark[k])
					continue;
				if(k == 0)
					b ++;
				if(b >= 10000)
					b %= 10000;
				update(i + 1 , b);
				a[i] = b;
			}
		}
		cas ++;
		ans = sum(n);
		if(ans >= 10000)
			ans %= 10000;
		printf("Case #%d: %04d\n" , cas , ans);
	}
	return 0;
}