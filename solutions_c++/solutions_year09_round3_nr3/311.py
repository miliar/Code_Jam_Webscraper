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

int A[10005];
int B[10005];
int F(int x,int y){
int i,t=2000000000,l=0;
SFOR(i,x+1,y) if (B[i]>0){l++; t=min(t,y-x-2+F(x,i)+F(i,y));}
if (l==0) return 0;
else return t;

}
int main()
{
	int temp,i,j,k,n,m;
	FILE * f1 = fopen("p3.out","w");
	scanf("%d",&n);
	FOR(j,n){
		int p,q;
		scanf("%d%d",&p,&q);
		memset(B,0,sizeof(B));
		FOR(i,q){scanf("%d",&temp);B[temp]=1;}
		fprintf(f1,"Case #%d: %d\n",j+1,F(0,p+1));

	
	}
getch();
	return 0;
}