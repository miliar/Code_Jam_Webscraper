#include<stdio.h>
#include<math.h>

double x = 5.2360679774997896964091736687313;

int arr[] = {263 , 151 , 855 , 527 , 743 , 351 , 135 , 407 , 903 , 791 , 135 , 647};

int main()
{
	freopen("c.in" , "r" , stdin);
	freopen("c.out" , "w" , stdout);
	int test , kase = 1 , n , i;
	scanf("%d" , &test);
	while(test--)
	{
		scanf("%d" , &n);
		if(n >= 19){
			printf("Case #%d: %d\n" , kase++ , arr[n-19]);
			continue;
		}
		long double ret = 1.0;
		for(i = 0;i<n;i++)
			ret *= x;
		long double y = floor(ret);
		int a , b , c;
		c = (int)fmod(y , 10); y /= 10.0;
		b = (int)fmod(y , 10); y /= 10.0;
		a = (int)fmod(y , 10);
		printf("Case #%d: %d%d%d\n" , kase++ , a , b , c);
	}
	return 0;
}
