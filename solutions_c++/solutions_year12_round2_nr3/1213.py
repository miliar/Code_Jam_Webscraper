/*
 * EqualSums.cpp
 *
 *  Created on: May 5, 2012
 *      Author: B2lawa
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
using namespace std;
int v[2000001];
int N;
int arr[20];
void printSol(int s1,int s2 ,int n)
{
	printf("Case #%d:\n",n);
	char *str="";
	for(int i=0;i<N;++i)
	{
		if(s1&(1<<i))
			printf("%s%d",str,arr[i]),str=" ";
	}
	printf("\n");
	str="";
	for(int i=0;i<N;++i)
	{
		if(s2&(1<<i))
			printf("%s%d",str,arr[i]),str=" ";
	}
	printf("\n");
}
int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt)
	{
		scanf("%d",&N);
		for(int i=0;i<N;++i)
			scanf("%d",&arr[i]);
		memset(v,-1,sizeof(v));
		for(int i=1;i<(1<<N);++i)
		{
			int sum=0;
			for(int j=0;j<N;++j)
				if(i&(1<<j))
					sum+=arr[j];
			if(v[sum]==-1)
				v[sum]=i;
			else
			{
				printSol(v[sum],i,tt);
				break;
			}
		}

	}
}
