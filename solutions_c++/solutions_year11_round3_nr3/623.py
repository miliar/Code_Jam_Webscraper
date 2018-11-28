#include<cstdio>
int f[200],t,mt,l,r,n,i,j,find;
int main()
{
	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		scanf("%d%d%d",&n,&l,&r);
		for(i=0;i<n;i++)scanf("%d",&f[i]);
		find=0;
		for(i=l;i<=r;i++)
		{
			int p=0;
			for(j=0;j<n;j++)
			{
				if (f[j]%i!=0&&i%f[j]!=0) 
				{
					p=1;
					break;
				}
			}
			if (!p) 
			{
				find=1;
				break;
			}
		}
		if (!find) printf("Case #%d: NO\n",mt);
		else printf("Case #%d: %d\n",mt,i);
	}
}
	
