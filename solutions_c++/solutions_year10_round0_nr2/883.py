// GCJ2010FairWaning.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
#include <conio.h>
#include <stdlib.h>
#include <math.h>


int sort(const void *x, const void *y) 
{
  return (*(long*)x - *(long*)y);
}


unsigned long computeGCD(unsigned long m, unsigned long n) {

  unsigned long t, r;

  if (m < n) {
    t = m;
    m = n;
    n = t;
  }

  if(n==0)
	  return m;

  r = m % n;

  if (r == 0) {
    return n;
  } else {
    return computeGCD(n, r);
  }

}

unsigned long computeGCD1(unsigned long a, unsigned long b)
{
	if(a==b)
		return a;

	if(a>b)
	{
		unsigned long tmp = a;
		a=b;
		b=tmp;
	}



	if(a==0)
		return b;
	
	if(a==1)
		return 1;

	return computeGCD(a, b-a);
}

int main(int argc, char* argv[])
{
    int noOftestCases = 0;

	/*
	The first line of the input gives the number of test cases, C. 
	C lines follow. Each starts with a single integer N, which is 
	followed by a space and then N space-separated integers ti, the number of 
	slarboseconds since Great Event i occurred.
	*/

	cin>>noOftestCases;
    
	
	for(int i=0;i<noOftestCases;i++)
	{
		 int N;
		 cin>>N;

		 unsigned long *t = new unsigned long[N];

		 for(int j=0;j<N;j++)
		 {
			 unsigned long l;
			 cin>>l;
             *(t+j) = l;
		 }
       
         qsort(t,N,sizeof(unsigned long),sort);

		 if(N==2)
		 {
			 unsigned long diff = t[1] - t[0];
             
			 unsigned long y = 0;

			 if(diff>t[0])
			 {
                 y = diff-t[0];
			 }
			 else if(diff<=t[0] && diff!=0)
			 {
				 unsigned long multiple  = (t[0]/diff);

				 if((t[0]%diff)!=0L)
				 {
					 multiple++;
				 }

				 y = (multiple * diff) - t[0];
			 }

             cout<<"Case #"<<i+1<<":"<<" "<<y; 
		 }
		 else
		 if(N==3)
		 {
			 unsigned long diff1 = t[1]-t[0];
			 unsigned long diff2 = t[2]-t[1];
             unsigned long diff3 = t[2]-t[0];

			 unsigned long gcd1 = computeGCD(diff1, diff2);
             unsigned long gcd = computeGCD(gcd1, diff3);

             unsigned long multiple  = (t[0]/gcd);
			 
			 if((t[0]%gcd)!=0L)
			 {
				 multiple++;
			 }

             unsigned long y = (multiple * gcd) - t[0];

             cout<<"Case #"<<i+1<<":"<<" "<<y; 
		     
		 }

		 cout<<"\n";

		 delete[] t;

	}

	return 0;
}
