#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
int T,i,n,j,a[1002],temp,ans;
int main()
{
	freopen("data.in", "r", stdin);
    freopen("data.out", "w+", stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++) {
		ans=0;
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		for(j=0;j<n;j++) {
			scanf("%d",&a[j]);
			if (j==0) temp=a[j];
			else temp=temp^a[j];
		}
		printf("Case #%d: ",i);
		if (temp!=0) printf("NO\n");
		else {
			sort(a,a+n);
			for(j=1;j<n;j++) {
				ans+=a[j];
			}
			printf("%d\n",ans);
		}
	}
	return 0;
}
