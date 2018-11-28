// GoogleCodeJam2012ProbC.cpp : Defines the entry point for the console application.
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



int numDigits(int in)
{
	int nd=0;
	for (int i=0; i<8; i++)
	{
		if ((double)in/pow((double)10,(double)i)<1) 
		{nd=i;break;}
	}
	return nd;
}

int shiftNum(int num, int k)
{
	int kk = (int) pow(10.0,double(k));
	int p1 = num-num/kk*kk ;
	int p2 = num/kk;
	return (int) (p1*pow(10.0,double(numDigits(p2)))+p2);
}

int validPair(int A, int B, int nd)
{
	if ( B<=A || numDigits(A)!=numDigits(B) ) return 0;
	int *nExist = new int[2000000];
	for (int i=0; i<2000001; i++) nExist[i]=0;
	int nP=0; //number of valid pairs.
	for (int n=A;n<B;n++)
	{
        if (nExist[n]==1) continue;
		nExist[n]=1;
		int nPtmp=0;
		for (int s=1; s<nd; s++) //s is shift
		{
			int tmp = shiftNum(n,s);
			if (tmp>B || numDigits(n)!=numDigits(tmp)) continue;
			if (nExist[tmp]==1) continue;
			if (tmp>n) 
			{
				nPtmp++;
				nExist[tmp]=1;
			}
		}
		nP += (1+nPtmp)*nPtmp/2;
	}
	return nP;
}



int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int T, A, B; 
	scanf( "%d", &T );

	//cout<<shiftNum(123,1)<<endl;

	for (int i=0; i<T; i++)
	{ 
		scanf( "%d", &A );
	    scanf( "%d", &B );

		//cout<<numDigits(A);
		printf("Case #%d: %d\n",i+1,validPair(A,B,numDigits(A)));
		
	}

	return 0;
}