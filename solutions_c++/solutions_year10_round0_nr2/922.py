#include<cstdio>
#include<cstring>

int a[3] , b[3];

int gcd(int x , int y)
{
	if(y == 0) return x;
	else return gcd(y , x % y);
}

int main()
{
	int n , t , i , j;
	scanf("%d" , &t);
	for(j = 1;j <= t;j++)
	{
		scanf("%d" , &n);
		for(i = 0;i < n;i++)
			scanf("%d" , &a[i]);
		for(i = 0;i < n - 1;i++)
			b[i] = a[i + 1] - a[i];
		int s = b[0];
		for(i = 1;i < n - 1;i++)
			s = gcd(s , b[i]);
		if(s < 0) s = -s;
		printf("Case #%d: %d\n" , j , (s - a[i] % s) % s);
	}
	return 0;
}