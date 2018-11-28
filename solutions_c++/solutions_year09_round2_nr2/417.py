#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <algorithm>
#include <memory.h>
#include <bitset>
#include <vector>
using namespace std;

int hash[10] , a[10];

int main()
{
	int i , j , t , cas = 0 , len , MAX , id;
	char s[100] , c[100];
	freopen("11.txt" , "w" , stdout);
	scanf("%d" , &t);
	while(t --)
	{
		cas ++;
		scanf("%s" , s);
		len = strlen(s);
		for(i = len - 1 ; i >= 0 ; i --)
		{
			MAX = -1;
			for(j = i + 1 ; j <= len - 1 ; j ++)
			{
				if(s[j] > s[i])
				{
					if(MAX == -1)
					{
						MAX = s[j] - '0';
						id = j;
					}
					else if(MAX > s[j] - '0')
					{
						MAX = s[j] - '0';
						id = j;
					}
				}
			}
			if(MAX != -1)
			{
				c[0] = s[id];
				s[id] = s[i];
				s[i] = c[0];
				break;
			}
		}
		printf("Case #%d: " , cas);
		if(i != -1)
		{
			for(i = i + 1 ; i < len ; i ++)
			{
				for(j = i + 1 ; j < len ; j ++)
				{
					if(s[i] > s[j])
					{
						c[0] = s[i];
						s[i] = s[j];
						s[j] = c[0];
					}
				}
			}
			printf("%s\n" , s);
		}
		else
		{
			for(i = len - 1 ; i >= 0 ; i --)
			{
				if(s[i] != '0')
					break;
			}
			id = i;
			printf("%c" , s[id]);
			printf("0");
			for(i = len - 1 ; i >= 0 ; i --)
			{
				if(i == id)
					continue;
				printf("%c" , s[i]);
			}
			printf("\n");
		}
	}
	return 0;
}