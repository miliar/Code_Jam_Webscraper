// Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
int main()
{
	freopen("e:\\A-large.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	int T,N,K,period;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		period=1<<N;
		K=(K+1)%period;
		printf("Case #%d: ",i);
		if(K==0) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}

