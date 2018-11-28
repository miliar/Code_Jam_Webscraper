#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;

int a[1024],b[1024];

int main()
{
	int i,j,k,tc,T,ans,n;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d", &T);
	for(tc=1; tc<=T; tc++)
	{
		ans=0;
		scanf("%d", &n);
		for(i=0; i<n; i++)
			scanf("%d%d", &a[i], &b[i]);
		
		for(i=0; i<n; i++)
			for(j=i+1; j<n; j++)
			{
				if((a[i]-a[j])*(b[i]-b[j])<0)
					ans++;
			}
		printf("Case #%d: %d\n", tc,ans);
	}
	return 0;	
}

