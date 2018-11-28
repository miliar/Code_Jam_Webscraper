#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int g[50][50];
int a[50];
int b[50];
int main()
{
	int cases;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
				scanf("%1d",&g[i][j]);
		memset(a,-1,sizeof(a));
		for(int i=0;i<n;++i)
		{
			int j=n-1,k;
			while(j>0&&g[i][j]==0)--j;
			//printf("%d\n",j);
			for(k=j;k<n;++k)
				if(a[k]==-1)break;
			a[k]=i;
		}
		int ans=0;
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j)
				if(a[i]>a[j])++ans;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
