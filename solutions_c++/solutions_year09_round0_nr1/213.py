#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

int l, d, n, result;
char dic[5100][20];
bool jihe[20][300];

int main()
{
	int i, j, k, now;
	bool you, kuohao;
	char buf[1000];
	
	scanf("%d%d%d", &l, &d, &n);
	for (i = 0; i < d; i++)
		scanf("%s", dic[i]);
	for (k = 1; k <= n; k++)
	{
		scanf("%s", buf);
		clr(jihe);
		now = 0;
		you = 0;
		kuohao = 0;
		//printf("%s\n", buf);
		for (i = 0; i < strlen(buf); i++)
		{
			if (kuohao)
			{
				if (buf[i] == '(')
				{
					now++;
				}
				if (buf[i] == ')')
				{
					now++;
					kuohao = 0;
				}
				else
				{
					jihe[now][buf[i]] = 1;
				}
			}
			else
			{
				if (buf[i] == '(')
				{
					kuohao = 1;
				}
				else
				{
					//you = 1;
					jihe[now][buf[i]] = 1;
					now++;
				}
					
			}
		}/*
		for (i = 0; i < l; i++)
		{
			for (j = 'a'; j <= 'z'; j++)
				if (jihe[i][j]) printf("%c", j);
			printf(" ");
		}
		printf("\n");*/
		result = 0;
		for (i = 0; i < d; i++)
		{
			for (j = 0; j < strlen(dic[i]); j++)
			{
				if (!jihe[j][dic[i][j]]) break;
			}
			if (j == strlen(dic[i])) result++;
		}
		printf("Case #%d: %d\n", k, result);
	}
	
	return 0;
}
