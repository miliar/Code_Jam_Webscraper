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
int A[10];

bool check(int temp,int t)
{
	memset(A,0,sizeof(A));
	while (t>0)
	{
		A[t%10]++;
		t/=10;
	}
	while (temp>0)
	{A[temp%10]--;
		temp/=10;
	}
	bool res=true;
	for(int i=1;i<10;i++)
		if (A[i]!=0) res=false;
	return !res;

}
int main()
{
	FILE * f1 = fopen("pr2.out","w");
	int i,n,t;
	scanf("%d",&n);
	FOR(i,n){

		scanf("%d",&t);
		int temp=t;
		t++;
		while( check(t,temp) ){
			t++;
		}
		fprintf(f1,"Case #%d: %d\n",i+1,t);
	}
	return 0;
}