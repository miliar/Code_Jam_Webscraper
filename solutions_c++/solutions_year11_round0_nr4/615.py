#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64
#define MAX 1005

double c[MAX][MAX];
double a[MAX], b[MAX];
double ans[MAX];
int x[MAX], y[MAX], n;

bool cmp(int A, int B){
	return x[A]<x[B];
}

int main(){
     int i, j, k, T, TT=1;
     // b[n] 1/n!
     b[0] = 1.0;
     for(i=1;i<MAX;i++)b[i]=b[i-1]/i;
     // a[n] 1/2!-1/3!...+(-1)^(n)*1/(n)!
     a[2] = b[2];
     for(i=3;i<MAX;i++){
		a[i] = 0.0;
		for(j=i;j>=2;j--)a[i]+=(j&1)?-b[j]:b[j];
	}
     // c[n][k]  n = k + n-k  yes:no
     // c[n][k] = 1/k!*(1/2!-1/3!...+(-1)^(n-k)*1/(n-k)!)
     // 1/2!.... ->0.367879
     F(i,MAX)F(j,MAX) c[i][j] = 0.0;
     c[1][1] = 1.0;
     c[2][0] = c[2][2] = 0.5;
     for(i=3;i<MAX;i++){
		// k 0...n-2,n
		for(k=0;k<=i-2;k++) c[i][k] = b[k]*a[i-k];
		c[i][i] = b[i];
	}
	
	ans[0] = 0.0;
	for(i=1;i<MAX;i++){
		double sum = 0;
		for(k=1;k<=i;k++)sum += c[i][k]*ans[i-k];
		ans[i] = (sum+1.0)/(1-c[i][0]);
	}
	
//    freopen("D-small-attempt0.in", "r", stdin);
 //   freopen("D-small-attempt0.out", "w", stdout);
//    freopen("D-large.in", "r", stdin);
//    freopen("D-large.out", "w", stdout);
	
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		F(i,n){
			scanf("%d",&x[i]);
			y[i] = i;
		}
		sort(y, y+n, cmp);
		j = 0;
		F(i,n)if(y[i]!=i)j++;
		printf("Case #%d: %.6lf\n",TT++, ans[j]);
	}
	
//	cin>>i;
     
     return 0;
}
