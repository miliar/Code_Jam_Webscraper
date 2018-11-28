#include <iostream>
#include <cstring>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	char s[70] , c;
	__int64 ans , d;
	int base , i , t , ca , len , b[256] , a[70] , x;
	scanf("%d" , &t);
	for( ca = 1 ; ca <= t ; ca++)
	{
		memset( b , -1 , sizeof(b));
		scanf("%s" , s);
		len = strlen(s);
		if(len == 1)
		{
			printf("Case #%d: 1\n" , ca);
		}
		else
		{
			base = 0;
			b[s[0]] = 1;
			base++;
			for( i = 1 ; i < len ; i++)
			{
				if( b[s[i]] == -1 )
				{
					b[s[i]] = 0;
					base++;
					break;
				}
			}
			x = 2;
			for( ; i < len ; i++)
			{
				if( b[s[i]] == -1 )
				{
					b[s[i]] = x;
					x++;
					base++;
				}
			}
			if( base == 1)base = 2;
			for( i = 0 ; i < len ; i++)
				a[i] = b[s[i]];
			for( ans = 0 , d = 1 , i = len -1 ; i >= 0 ; i-- , d *= base)
			{
				ans += (__int64)a[i] * d;
			}
			printf("Case #%d: %I64d\n" , ca , ans);
		}
	}
	return 0;
}

/*

3
11001001
cats
zig

*/