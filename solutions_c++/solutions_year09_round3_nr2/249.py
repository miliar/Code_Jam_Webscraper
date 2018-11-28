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


int main()
{
	FILE * f1 = fopen("pr2.out","w");
	int i,n,t,j,k,g,m;
	int A[600][3],B[600][3];

	scanf("%d",&n);
	FOR(g,n){
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));
		scanf("%d",&m);
		FOR(j,m)
			scanf("%d %d %d %d %d %d",&A[j][0],&A[j][1],&A[j][2],&B[j][0],&B[j][1],&B[j][2]);
		double X[3],XV[3];
		memset(X,0,sizeof(X));
		memset(XV,0,sizeof(XV));
		FOR(j,m) {
			X[0]+=A[j][0]/(1.0*m);
			X[1]+=A[j][1]/(1.0*m);
			X[2]+=A[j][2]/(1.0*m);
			XV[0]+=B[j][0]/(1.0*m);
			XV[1]+=B[j][1]/(1.0*m);
			XV[2]+=B[j][2]/(1.0*m);
		}	
		double res1,res2;
		if ((XV[0]*XV[0]+XV[1]*XV[1]+XV[2]*XV[2])<0.000001)  res1=0; 
		else	res1=-(X[0]*XV[0]+X[1]*XV[1]+X[2]*XV[2])/(XV[0]*XV[0]+XV[1]*XV[1]+XV[2]*XV[2]);
		if (res1<0.000001) res1=0;
		res2=sqrt(long double(XV[0]*res1+X[0])*(XV[0]*res1+X[0])+(XV[1]*res1+X[1])*(XV[1]*res1+X[1])+(XV[2]*res1+X[2])*(XV[2]*res1+X[2]));
		fprintf(f1,"Case #%d: %f %f\n",g+1,res2,res1);
		
	}
	return 0;
}