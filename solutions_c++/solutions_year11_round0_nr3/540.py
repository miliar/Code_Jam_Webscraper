// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	scanf("%d ",&T);
	REP(xx,T) {
		int n,a,sum=0,xor=0,min=2000000;
		scanf("%d",&n);
		REP(i,n) {
			scanf("%d",&a);
			if(a<min) min=a;
			sum+=a;
			xor^=a;
		}
		printf("Case #%d: ",xx+1);
		if(xor==0)  {
			printf("%d\n",sum-min);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}

