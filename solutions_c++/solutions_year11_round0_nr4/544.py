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
		int n,a,cnt=0;
		scanf("%d",&n);
		REP(i,n) {
			scanf("%d",&a);
			cnt+=a-1!=i;

		}
		printf("Case #%d: %d\n",xx+1,cnt);
	}
	return 0;
}

