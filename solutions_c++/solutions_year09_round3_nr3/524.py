#include <iostream>
#include <algorithm>
bool b[10001];
int a[120];



int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int t , p , q , ca , i , j , d , k;
	__int64 ans , min;
	scanf("%d" , &t);
	for( ca = 1 ; ca <= t ; ca++)
	{
		scanf("%d%d" , &p , &q);
		for( i = 0 ; i < q ; i++)
		{
			scanf("%d" , &d);
			a[i] = d - 1;
		}
		min = 999999999;
		do
		{
			memset(b , 0 , sizeof(b));
			ans = 0;
			for( j = 0 ; j < q ; j++)
			{
				b[a[j]] = 1;
				for( k = a[j] + 1 ; k < p ; k++)
				{
					if(b[k])break;
					ans++;
				}
				for( k = a[j] - 1 ; k >=0 ; k--)
				{
					if(b[k])break;
					ans++;
				}
			}
			if( ans < min ) min = ans;

		}
		while (std::next_permutation(a , a+q));
		printf("Case #%d: %I64d\n" , ca , min);
	}

}