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
int L,P,C;
int get()
{
	int i = 0;
	long long _L = L;
	long long Z = C;
	long long _P = P;
	for(i = 0;Z * _L < _P; ++ i)
	{
		Z *= Z;
	}
	return i;
}
int main()
{
 	freopen("B-large.in","r",stdin);
 	freopen("output3.txt","w",stdout);
	scanf("%d",&T);
	for(int i = 1; i <= T; ++ i)
	{
		scanf("%d%d%d",&L,&P,&C);

		printf("Case #%d: ",i);
		printf("%d\n",get());
	}
	return 0;
}
