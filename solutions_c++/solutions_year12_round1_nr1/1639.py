// googleCodeJam2012Round1A.cpp : Defines the entry point for the console application.
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

	int T, A, B; 
	scanf( "%d", &T );

	//cout<<shiftNum(123,1)<<endl;

	for (int i=0; i<T; i++)
	{ 
		scanf( "%d", &A );
	    scanf( "%d", &B );
		int size=(int)pow(2.0,A);
		double *expect = new double[A+2];
		float *prob=new float[A];

		float *p = new float[A];
		prob[0]=1.0;
		for (int j=0; j<A; j++)
		{
			scanf("%f",&p[j]);
			prob[0] *= p[j];
		}
		
		for (int j=1; j<A; j++)
			prob[j] = prob[j-1]/p[A-j];  

		int mm=B-A+1;
		int nn=2*B-A+2;
		for (int j=0; j<A; j++)
			expect[j]=(mm+2*j)*prob[j]+(nn+2*j)*(1-prob[j]);
		expect[A]=A+B+1;
		expect[A+1]=B+2;
		
		double min = expect[0];
		for (int j=1;j<A+2;j++)
		{
			if (expect[j]<min) 
				min = expect[j];
		}
		

		//cout<<numDigits(A);
		printf("Case #%d: %f\n",i+1,min);
		
	}
	return 0;
}

