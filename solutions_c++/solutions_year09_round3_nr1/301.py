#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <conio.h>

using namespace std;

#define lint long long

#define ss stringstream
#define pb push_back
#define sz size()
#define FOR(i,n) for(i=0;i<n;i++)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

string str;
int A[1000];

int main()
{
	
	int i,j,k,l=1,n=1,h,w;
	FILE * f1 = fopen("B-large.in","r");
	FILE * f2 = fopen("p1a.out","w");
	scanf("%d\n",&n);
	FOR(j,n){
		char buf[100];
		memset(A,0,sizeof(A));
		scanf("%s",buf);
		string s1=string(buf);
		FOR(i,s1.sz)
			A[s1[i]]++;
		int base=0;
		FOR(i,1000) if (A[i]>0) base++;
		__int64 res=0;
		
		memset(A,-1,sizeof(A));
		int g=0;
		if (base==1) base++;
		FOR(i,s1.sz) if (A[s1[i]]==-1) {A[s1[i]]=g; g++;}

		FOR(i,1000) if (A[i]==0) A[i]=1; else if (A[i]==1) A[i]=0;
		
		FOR(i,s1.sz) { res=res*base+A[s1[i]];}
		fprintf(f2,"Case #%d: %lld\n",j+1,res);



		
	}


	return 0;
}