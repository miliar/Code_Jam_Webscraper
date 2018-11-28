// qua_3.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <cstdio>
const int MAXN = 1100;

int main(int argc, char* argv[])
{
	int T;
	int group[MAXN];
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);

	int nFrom, nEnd;

	int R, K, N;
	__int64 result;		//防止溢出
	for (int i = 0 ; i < T; i++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for (int j = 0; j < N; j++)
		{
			scanf("%d",&group[j]);
		}
		result = 0;
		nFrom = 0;
		int sum, temp;
		while (R--)
		{
			sum = 0;
			int nCount = 0;
			while ((temp = sum + group[nFrom]) <= K)
			{
				sum = temp;
				nFrom = (nFrom + 1) % N;
				nCount++;
				if (nCount >= N)
					break;
			}
			result += sum;
		}
		printf("Case #%d: %I64d\n",i+1, result);
		
	}
	return 0;
}

