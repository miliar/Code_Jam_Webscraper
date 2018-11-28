#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
using namespace std;
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define N 1000

int t,T,n,arr[N+1],sorted_arr[N+1];
double A[N+1];
double D[N+1];
double Fac[N+1];


void process(){
	int i,count=0;
	copy(arr+1,arr+n+1,sorted_arr+1);
	sort(sorted_arr+1,sorted_arr+n+1);
	FOR(i,1,n){
		if (arr[i] != sorted_arr[i]) count++;
	}
	printf("Case #%d: %.6lf\n",t,A[count]);
}

double P(int n,int k){
	return D[n-k] / Fac[n-k] / Fac[k];
}

void preprocess(){
	int i,j;
	Fac[0] = 1. ,Fac[1] = 1.;
	FOR(i,2,N){
		Fac[i] = Fac[i-1]*i;
	}

	D[1] = 0. , D[2] = 1.;
	FOR(i,3,N){
		D[i] = i*D[i-1] + pow(-1.,i);
	}
	A[1] = 0.;
	FOR(i,2,N){
		A[i] = 0.;
		FOR(j,0,i-2){
			A[i] += P(i,j)*A[i-j];
		}
		A[i] = A[i]+1;
		A[i] /= (1-P(i,0));
	}
}

int main(){
	freopen("D-small.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
	preprocess();
	scanf("%d",&T);
	FOR(t,1,T){
		int i;
		scanf("%d",&n);
		FOR(i,1,n) scanf("%d",&arr[i]);
		process();
	}
	return 0;
}
