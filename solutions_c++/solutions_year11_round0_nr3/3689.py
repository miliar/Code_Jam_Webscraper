#include<cstdio>
int t[1024];
int main()
{
	int X;
	scanf("%d",&X);
	int kase=0;
	while(X--)
	{
		int mmin=0,n,res=0,p=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&t[i]);
			res+=t[i];
			if(t[i]<mmin||i==0)mmin=t[i];
			p^=t[i];
		}
		kase++;
		if(p==0)printf("Case #%d: %d\n",kase,res-mmin);
		else printf("Case #%d: NO\n",kase);
	}
}
