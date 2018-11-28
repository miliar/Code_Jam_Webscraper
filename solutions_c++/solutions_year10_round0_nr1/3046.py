#include<cstdio>
#include<cstring>
int main()
{
	int n , k , t , j;
	scanf("%d" , &t);
	for(j = 1;j <= t;j++)
	{
		scanf("%d%d" , &n , &k);
		int i;
		for(i = 0;i < n;i++)
		{
			if(k % 2 != 1) break;
			k = k / 2;
		}
		if(i == n) printf("Case #%d: ON\n" , j);
		else printf("Case #%d: OFF\n" , j);
	}
	return 0;
}