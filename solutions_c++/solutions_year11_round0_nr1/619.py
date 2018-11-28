#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64
#define abs(t) ((t<0)?-(t):(t))
#define max(a,b) ((a)<(b)?(b):(a))

int n, a[110], f[110];

int work(){
	int i, j, x, y, u, v, t;
	x = y = 1;
	u = v = 0;
	F(i,n){
		if(f[i]==0){  // x
			u += abs(x-a[i]) + 1;
			x = a[i];
			if(u<=v)u=v+1;
		}
		else {       // y
		     v += abs(y-a[i]) + 1;
		     y = a[i];
		     if(v<=u)v=u+1;
		}
	}
	return max(u, v);
}

int main(){
     int i, j, T, TT=1;
     char s[100];
 //    freopen("A-large.in", "r", stdin);
//     freopen("A-large.out", "w", stdout);
     scanf("%d",&T);
     while(T--){
		scanf("%d",&n);
		F(i,n){
			scanf("%s%d", s, &a[i]);
			if(s[0]=='O')f[i]=0;
			else f[i] = 1;
		}
		printf("Case #%d: %d\n",TT++, work());
	}
//	cin>>i;
     return 0;
}
