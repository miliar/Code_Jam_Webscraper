#include <stdio.h>
#include <string.h>

int main()
{
int T , i , L , t , j , min;
int base;
bool check[50];
int a[50];
char s[100];
int translate[100];
__int64 res , be;

	//freopen("A-large.in" , "r" , stdin);
	//freopen("Alarge.txt" , "w" , stdout);
	scanf("%d" , &T);
	for (t = 1; t <= T; t ++)
	{
		scanf("%s" , s);
		L = strlen(s);
		memset(a , 0 , sizeof(a));
		for (i = 0; i < L; i ++)
			if (s[i] >= '0' && s[i] <= '9')
				a[s[i]-'0'] = -1;
			else a[s[i]-'a' + 10] = -1;
		base = 0;
		for (i = 0; i < 50; i ++) base += a[i];
		base = -base;
		if (base <= 1) base = 2;
		memset(check , 0 , sizeof(check));
		memset(translate , 0 , sizeof(translate));
		if (s[0] >= '0' && s[0] <= '9') a[s[0] - '0'] = 1;
		else a[s[0] - 'a' + 10] = 1;
		translate[0] = 1;
		check[1] = true;
		for (i = 1; i < L; i ++)
		{
			if (s[i] >= '0' && s[i] <= '9')
			{
				if (a[s[i] - '0'] == -1) //new
				{
					j = 0;
					while (check[j] && j < 50) j ++;
					check[j] = true;
					a[s[i] - '0'] = j;
					translate[i] = j;
				}
				else translate[i] = a[s[i] - '0'];
			}
			else
			{
				if (a[s[i] - 'a' + 10] == -1)
				{
					j = 0;
					while (check[j] && j < 50) j ++;
					check[j] = true;
					a[s[i] - 'a' + 10] = j;
					translate[i] = j;
				}
				else translate[i] = a[s[i] - 'a' + 10];
			}
		}
		res = 0; be = 1;
		for (i = L - 1; i >= 0; i --)
		{
			res = res + be * (__int64)translate[i];
			be = be * (__int64)base;
		}
		printf("Case #%d: %I64d\n" , t , res);
	}
	return 0;
}