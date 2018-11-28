#include <iostream>
using namespace std;

int map[50][50] , s[50];

char a[50];

int main()
{
	int i , j , n , m , cas = 0 , t , k , ans;
	freopen("A-large.in" , "r" , stdin);
	freopen("1.txt" , "w" , stdout);
	scanf("%d" , &t);
	for(cas = 1 ; cas <= t ; cas ++)
	{
		scanf("%d" , &n);
		for(i = 0 ; i < n ; i ++)
		{
			scanf("%s" , &a);
			for(j = 0 ; j < n ; j ++)
			{
				map[i][j] = a[j] - '0';
			}
			for(j = n - 1 ; j >= 0 ; j --)
			{
				if(map[i][j] == 1)
					break;
			}
			s[i] = j;
		}
		ans = 0;
		for(i = 0 ; i < n ; i ++)
		{
			for(j = i ; j < n ; j ++)
			{
				if(s[j] <= i)
					break;
			}
			ans += j - i;
			for(k = j - 1 ; k >= i ; k --)
			{
				s[k + 1] = s[k];
			}
		}
		printf("Case #%d: %d\n" , cas , ans);
	}
	return 0;
}