#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
using namespace std;
double pi[5];
double A[5];
double B[5];
int main(){
	int T,a,b,i,j,cas;
	double p;
	double min;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++){
		min=1000000;
		p=0;
		scanf("%d %d",&a,&b);
		for(i=1;i<=a;i++)
			scanf("%lf",&pi[i]);
		for(i=0;i<=a;i++){
			A[i]=1;
		}
		for(i=1;i<=a;i++){
			A[i]=A[i-1]*pi[i];
			B[i]=A[i-1]*(1-pi[i]);
		}
		for(i=1;i<=a;i++)
			p+=B[i]*(b+2);
		p+=A[a]*(b+2);
		if(p<min)
			min=p;
	
		for(i=0;i<=a;i++){
			p=0;
			for(j=1;j<=a;j++){
				if(a-i<j)
					p+=B[j]*(2*i+b-a+1);
				else
					p+=B[j]*(2*i+b-a+1+b+1);
			}
			p+=A[a]*(2*i+b-a+1);
			
			if(p<min)
				min=p;
		}
		printf("Case #%d: %.6lf\n",cas,min);
	}
	return 0;
}

		



		






	
