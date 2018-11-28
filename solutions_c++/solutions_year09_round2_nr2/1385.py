// qa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "cstdio"
#include "cstring"
#include "algorithm"
using namespace std;

char str[22] ={0};
int len;
int a[22];




int main()
{
	freopen("e:\\s.txt","r",stdin);
	freopen("a.txt","w",stdout);
	int zz;
	int ans;
	int i,j;

	scanf("%d",&zz);

	for (int z = 1; z <= zz; z++)
	{
		scanf("%s",str);
		len = strlen(str);
		
		for (i = 0; i < 10; i++)
			a[i] = 0;

		for (i = 0; i < len; i++)
			a[str[i]-'0']++;
			
		int n = atoi(str) + 1;

		while (true)
		{
			int t[10] = {0};
			int tmp = n;

			while (tmp)
			{
				t[tmp%10]++;
				tmp /= 10;
			}

			for (i = 1; i < 10; i++)
				if (a[i] != t[i])
					break;

			if (i == 10)
			{
				ans = n;
				break;
			}
			n++;
		}
		printf("Case #%d: %d\n",z,ans);
	}

	return 0;
}