// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <string>
using namespace std;
int T;
int N;
int B[505][505];
void begin()
{
	B[1][0] = 1;
	B[1][1] = 1;
	B[0][0] = 1;
	for(int i = 2; i < 505; ++ i)
	{
		B[i][0] = 1;
		for(int k = 1; k <= i; ++ k)
		{
			if(k > i - k) {B[i][k] = B[i][i - k]; continue;}
			B[i][k] = (B[i - 1][k] + B[i - 1][k - 1]) % 100003;
		}
	}
}
int A[505][505];
void get()
{
	for(int i  = 2; i < 505; ++ i)
	{
		A[i][1] = 1;
		for(int k = 1; k < i; ++ k)
		{
			for(int d = 1; d < k; ++ d)
			{
				if (k - d - 1 > i - k - 1)
				{
					continue;
				}
				A[i][k] += (A[k][d] * B[i - k - 1][k - d - 1]) % 100003;
			}
		}
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output2.txt","w",stdout);
	scanf("%d",&T);
	begin();
	get();
	for(int i = 1; i <= T; ++ i)
	{
		scanf("%d",&N);
		int Z = 0;
		for(int k = 1; k < N; ++ k)
		{
			Z += A[N][k];
			//cout << A[N][k] << endl;
			Z %= 100003;
		}
		printf("Case #%d: ",i);
		printf("%d\n",Z);
	}
	return 0;
}
