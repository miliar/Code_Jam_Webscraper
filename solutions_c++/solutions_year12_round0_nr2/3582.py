// GoogleCodeJam2012ProbB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int T, N, S, p; 
	scanf( "%d", &T );

	for (int i=0; i<T; i++)
	{ 
		scanf( "%d", &N );
	    scanf( "%d", &S );
		scanf( "%d", &p );
		int *t=new int[N];
		int num=0, can=0, nonzero=0;
		for (int j=0; j<N; j++)
		{	
			scanf( "%d", &t[j] );
		    if (t[j]>0) nonzero++;
			if (t[j]>=3*p-2) num++;
			else if (t[j]<3*p-4) continue;
			else can++;
		}

		if (p==0) printf("Case #%d: %d\n",i+1,N);
		else if (p==1) printf("Case #%d: %d\n",i+1,nonzero);
		else 
		{	
			if (can>=S) printf("Case #%d: %d\n",i+1,num+S);
			else printf("Case #%d: %d\n",i+1,num+can);
		}
	}

	return 0;
}

