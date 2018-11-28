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
int A[1005];
int B[1005];
int N;
bool check(int k,int d)
{
	int difA = A[k] - A[d];
	int difB = B[k] - B[d];
	if(difA * difB < 0) return true;
	return false;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	scanf("%d",&T);
	for(int i = 1; i <= T; ++ i)
	{
		scanf("%d",&N);
		for(int k = 0; k < N; ++ k)
			scanf("%d%d",&A[k],&B[k]);
		int Z = 0;
		for(int k = 0; k < N; ++ k)
			for(int d = k + 1; d < N; ++ d)
				if(check(k,d))
				{
					++ Z;
				}

		printf("Case #%d: ",i);
		printf("%d\n",Z);
	}
	return 0;
}
