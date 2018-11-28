#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64

int n, a[1010];

int main(){
     int i, j, T, TT=1, t, k, sum, x;
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small-attempt0.out", "w", stdout);
 //   freopen("C-large.in", "r", stdin);
 //   freopen("C-large.out", "w", stdout);
     scanf("%d",&T);
     while(T--){
		scanf("%d",&n);
		F(i, n)scanf("%d",&a[i]);
		t = a[0], k = 0, sum = x = 0;
		F(i,n){
			if(t>a[i])t=a[i],k=i;
			x+=a[i];
			sum^=a[i];
		}
		printf("Case #%d: ",TT++);
		if(sum)printf("NO\n");
		else printf("%d\n",x-t);
	}
//	cin>>i;
     
     return 0;
}
