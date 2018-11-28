#include<iostream>
#include<algorithm>

__int64 x[801] , y[801] , ans;
int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	int t , n , i , ca = 1 ;
	scanf("%d" , &t);
	while(t--)
	{
		scanf("%d" , &n);
		for( i = 0 ; i < n ; i++ )
			scanf("%I64d" , &x[i]);
		for( i = 0 ; i < n ; i++ )
			scanf("%I64d" , &y[i]);
		std::sort( x , x + n );
		std::sort( y , y + n );
		ans = 0;
		for( i = 0 ; i < n ; i++)
			ans += x[i] * y[n-i-1];
		printf("Case #%d: %I64d\n",ca,ans);
		ca++;
	}

}