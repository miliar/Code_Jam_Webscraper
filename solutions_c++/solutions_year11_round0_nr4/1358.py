#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
int T,i,j,n,a[1002],b[1002];
double ans;
int main()
{
	freopen("data.in", "r", stdin);
    freopen("data.out", "w+", stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++) {
		ans=0;
		scanf("%d",&n);
		for(j=0;j<n;j++) {
			scanf("%d",&a[j]);
			b[j]=a[j];
		}
		sort(b,b+n);
		for(j=0;j<n;j++) {
			if (b[j]!=a[j]) 
				ans++;
		}
		printf("Case #%d: %.6f\n",i,ans);
	}
	return 0;
}