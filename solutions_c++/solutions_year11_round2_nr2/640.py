#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64

double p[1001000];
int len, C, D;

bool fit(double m){
	double pre, x;
	int i, j;
	pre = p[0] - m;
	for(i=1;i<len;i++){
		if(p[i]+m < pre+D) return false;
		x = p[i] - m;
		if(x<pre+D) x =pre + D;
		pre = x;
	}
	return true;
}

int main(){
     int i, j, T, TT=1, k, u;
	double x, y;
     freopen("B-small-attempt0.in","r",stdin);
     freopen("B.out","w",stdout);
     scanf("%d",&T);
     while(T--){
		scanf("%d%d",&C,&D);
		len = 0;
		F(i,C){
			scanf("%d%d",&j,&k);
			F(u,k)p[len++] = j;
		}
		
		sort(p, p+len);
//		F(i,len)cout<<p[i]<<endl;
//          cout<<fit(0)<<endl;
		double L, R, mid;
		L =  0.0, R = 1.0e13;
		while(L<R-1.0e-12){
			mid = (L+R)/2.0;
			if(fit(mid)) R = mid;
			else L = mid;
		}
		
		printf("Case #%d: ",TT++);
		printf("%.10lf\n", mid);
	}
     
     return 0;
}
