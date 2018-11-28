// qa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "memory.h"
using namespace std;

typedef __int64 int2;

char str[1000];
int len;

int main()
{
	freopen("e:\\A-large.in","r",stdin);
	freopen("1a.txt","w",stdout);
	int zz;
	int i,j,k;

	scanf("%d",&zz);

	for (int z = 1; z <= zz; z++)
	{	
		scanf("%s",str);
		len = strlen(str);
		
		int2 ans = 0;
		int a[40] = {0};
		int tr[40] = {0};
		int used[40] = {0};
		int ba = 0;

		for (i = 0; i < 40; i++)
			tr[i] = -1;

		for (i = 0; i < len; i++)
			if (str[i] >= '0' && str[i] <= '9')
			{
				a[str[i]-'0']++;
				if (a[str[i]-'0'] == 1) ba++;
			}
			else
			{
				a[str[i]-'a'+11]++;
				if (a[str[i]-'a'+11] == 1) ba++;
			}

		if (ba < 2) ba = 2;

		if (str[0] >= '0' && str[0] <= '9')
			tr[str[0]-'0'] = 1;
		else
			tr[str[0]-'a'+11] = 1;
		used[1] = 1;

		for (i = 1; i < len; i++)
		{
			if (str[i] >= '0' && str[i] <= '9')
			{
				j = str[i] - '0';
			}
			else
			{
				j = str[i]-'a'+11;
			}

			if (tr[j] != -1)
				continue;
			else
			{
				for (k = 0; k < 40; k++)
					if (used[k] == 0)
						break;
				used[k] = 1;
				tr[j] = k;
			}
		}
		/*for (i = 0; i < len; i++)
		{
			if (str[i] >= '0' && str[i] <= '9')
			{
				k = str[i] - '0';
			}
			else
			{
				k = str[i]-'a'+10;
			}
			printf("%d",tr[k]);
		}
		printf("\n%s\n",str);*/

		int2 base = 1;
		for (i = len-1; i >= 0; i--,base *= ba)
		{
			if (str[i] >= '0' && str[i] <= '9')
			{
				k = str[i] - '0';
			}
			else
			{
				k = str[i]-'a'+11;
			}
			ans += tr[k] * base;
		}

		printf("Case #%d: %I64d\n",z,ans);
	}

	return 0;
}