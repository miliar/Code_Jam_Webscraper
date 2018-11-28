// prrrr.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <cmath>
using namespace std;

long long ppow(long long a, long long b){
 long long res=1;
 int i;
 for (i=0;i<b;i++)
	 res*=a;
 return res;
}

int main()
{
	long long n,k,t;
		freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
    cin>>t;
	int i;
	for (i=0;i<t;i++){
	 cin>>n;
	 cin>>k;
     if (k%ppow(2,n)==ppow(2,n)-1)
		 cout<<"Case #"<<i+1<<": ON\n";
	 else
		 cout<<"Case #"<<i+1<<": OFF\n";
	}
	return 0;
}

