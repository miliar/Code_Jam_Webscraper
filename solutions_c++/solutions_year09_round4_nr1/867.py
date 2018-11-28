#include <cstdio>

int n,p[40];


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d: ",i+1);
		char temp[50];
		scanf("%d",&n);
		for(int j=0;j<n;++j)
		{
			scanf("%s",temp);
			int k;
			for(k=n-1;k>=0 && temp[k]=='0';--k);
			p[j]=k;
		}
		int ans=0;
		for(int j=0;j<n;++j)
		{
			int k;
			for(k=j;k<n;++k) if(p[k]<=j) break;
			ans+=k-j;
			int tt=p[k];
			for(int l=k;l>j;--l) p[l]=p[l-1];
			p[j]=p[k];
		}
		printf("%d\n",ans);
	}
	return 0;
}

