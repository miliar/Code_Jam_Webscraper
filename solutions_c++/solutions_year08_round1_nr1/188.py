#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("A.in","r");
FILE *out=fopen("A.out","w");

long long A[1000],B[1000];

int visA[1000],visB[1000];

int main()
{
	int t,z,i,j,test,n;
	long long ret;
	int pos;
	fscanf(in,"%d",&t);
	for(test=0;test<t;test++){
		ret=0;
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)fscanf(in,"%lld",&A[i]);
		for(i=0;i<n;i++)fscanf(in,"%lld",&B[i]);
		sort(A,A+n);
		sort(B,B+n);
		CLR(visA,0);
		CLR(visB,0);
		for(i=0;i<n;i++){
			for(j=n-1;j>=0;j--){
				if(visA[i] || visB[j])continue;
				if(A[i]<0 && B[j]>0){
					ret+=A[i]*B[j];
					visA[i]=1;
					visB[j]=1;
					break;
				}
			}
		}
		for(i=0;i<n;i++){
			for(j=n-1;j>=0;j--){
				if(visB[i] || visA[j])continue;
				if(B[i]<0 && A[j]>0){
					ret+=B[i]*A[j];
					visB[i]=1;
					visA[j]=1;
					break;
				}
			}
		}
		int ZA=0,ZB=0;
		for(i=0;i<n;i++){
			if(!visA[i] && !A[i]){
				ZA++;
				visA[i]=1;
			}
			if(!visB[i] && !B[i]){
				ZB++;
				visB[i]=1;
			}
		}
		long long maxx;
		for(i=0;i<ZB;i++){
			maxx=-1;
			for(j=0;j<n;j++){
				if(visA[j])continue;
				if(labs(A[j])>maxx){
					maxx=labs(A[j]);
					pos=j;
				}
			}
			if(maxx==-1)break;
			visA[pos]=1;
		}
		for(i=0;i<ZA;i++){
			maxx=-1;
			for(j=0;j<n;j++){
				if(visB[j])continue;
				if(labs(B[j])>maxx){
					maxx=labs(B[j]);
					pos=j;
				}
			}
			if(maxx==-1)break;
			visB[pos]=1;
		}
		for(i=0;i<n;i++){
			for(j=n-1;j>=0;j--){
				if(visB[i] || visA[j])continue;
				ret+=B[i]*A[j];
				visB[i]=1;
				visA[j]=1;
				break;
			}
		}
		fprintf(out,"Case #%d: %lld\n",test+1,ret);	
	}
	return 0;
}