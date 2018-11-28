#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int a[1000];
int main()
{
    freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,n,i,j;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
	    scanf("%d",&n);
		int sum=0;
		for(i=0;i<n;i++){
		    scanf("%d",a+i);
			sum^=a[i];
		}
		sort(a,a+n);
		int ans=0;
		for(i=1;i<n;i++)ans+=a[i];
		if(sum)printf("Case #%d: NO\n",test);
		else printf("Case #%d: %d\n",test,ans);
	}
}