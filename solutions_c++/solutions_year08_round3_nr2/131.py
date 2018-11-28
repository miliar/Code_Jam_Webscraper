#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
#include<vector>
#include<map>
#include<algorithm>
#include<string.h>
#include<string>
////#define linux
//#ifdef linux
//#define __int64 long long
//#endif
char input[50];
int num;
int len;
void cal(__int64 res, int flag, __int64 cur, int t)
{
	if(t == len)
	{
		res = res + cur *((__int64)flag);
		__int64 res1 = res * (-1);
		if(res % 2 == 0 || res % 3 == 0 || res % 5 == 0 || res % 7 == 0 ||
			res1 % 2 == 0 || res1 % 3 == 0 || res1 % 5 == 0 || res1 % 7 == 0 || res == 0)
			num++;
		return ;
	}
	__int64 new_cur = cur * ((__int64)10) + __int64(input[t] - '0');
	cal( res, flag, new_cur , t + 1);
	if(t != len - 1)
	{
		cal( res + ((__int64)flag) * new_cur, 1, 0, t + 1);
		cal( res + ((__int64)flag) * new_cur, -1, 0, t + 1);
	}
}
int main()
{
	int n;
	int i;
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	scanf("%d", &n);
	for(i = 0; i < n; i++)
	{
		num = 0;
		scanf("%s", input);
		len = strlen(input);
		cal(0, 1, 0, 0);
		printf("Case #%d: %d\n", i + 1, num);
	}	
	return 0;
} 