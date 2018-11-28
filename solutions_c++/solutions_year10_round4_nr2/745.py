#include<cstdio>
#include<cstring>

int a[2000];

int main()
{
	freopen("B-small-attempt3.in" , "r" , stdin);
	freopen("1.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int p;
	for(p = 1;p <= t;p++)
	{
		int n;
		int i , j;
		scanf("%d" , &n);
		for(i = 0;i < (1 << n);i++) scanf("%d" , &a[i]);
		for(i = 0;i < (1 << n) - 1;i++) scanf("%*d");
		int s = 0;
		for(i = n;i >= 1;i--)
		{
			int m = 0;
			for(j = 0;j < (1 << i);j += 2)
			{
				if(a[j] == 0)
				{
					a[m++] = 0;
				}
				else if(a[j + 1] == 0)
				{
					a[m++] = 0;
				}
				else
				{
					if(a[j] < a[j + 1]) a[m++] = a[j] - 1;
					else a[m++] = a[j + 1] - 1;
					s++;
				}
			}
		}
		printf("Case #%d: %d\n" , p , (1 << n) - 1 - s);
	}
	return 0;
}