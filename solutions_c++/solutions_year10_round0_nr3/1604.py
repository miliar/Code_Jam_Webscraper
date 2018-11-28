// Problem_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
using namespace std;

int mark[1001];

int t, k, r, n;
int g[1001];

__int64 work(int index);

int value[1001];

__int64 money[1001 * 1001];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("C-large.in", "r", stdin);
	freopen("out_c_large.txt", "w", stdout);

	scanf("%d", &t);

	for(int i = 0;i<t;i++)
	{
		printf("Case #%d: %I64d\n", i+ 1, work(i));
	}

	return 0;
}

__int64 work(int index)
{
	memset(mark, 0, sizeof(mark));
	memset(money, 0 , sizeof(money));
	scanf("%d%d%d", &r, &k, &n);

	for(int i = 0;i<n;i++)
	{
		scanf("%d", &value[i]);
	}

	int exit_flag = 0;

	int now = 0;
	int count = 0;
	int length = 0;
	while(1)
	{
		if(mark[now % n])
		{
			length = count + 1 - mark[now % n];
			break;
		}

		mark[now % n] = count + 1;

		int tmp = 0;
		int team_count = 0;
		while(tmp + value[now % n] <= k && team_count <n)
		{
			tmp += value[now % n];
			now ++;
			team_count ++;
		}
		
		money[count + 1] = tmp;
		count ++;
	}

	for(int i = 1;i<count + 1;i++)
	{
		money[i] += money[i-1];
	}

	__int64 res = 0;
	res = (r - mark[now % n]) / length;
	res *= (money[count] - money[mark[now % n] - 1]);
	res += money[(r - mark[now % n]) % length + mark[now % n]];
	return  res;
		
}