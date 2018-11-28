// GoogleCodeJam1.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <cstdio>

int main(int argc, char* argv[])
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	int N, K;
	int temp;
	//int temp1;
	for (int i = 0; i < T; i++)
	{
		scanf("%d%d",&N, &K);
		temp = 1 << N;
		//temp1 = 1 << (N - 1);
		if (K % temp == temp - 1 )
		{
			printf("Case #%d: ON\n",i+1);
		}
		else 
		{
			printf("Case #%d: OFF\n",i+1);
		}
	}
	return 0;
}

