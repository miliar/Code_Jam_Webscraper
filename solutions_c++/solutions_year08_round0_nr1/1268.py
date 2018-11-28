#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
	int i,j,k,l,n,s,q,ans,cz,p[110];
	string a[110],b[1200];
	char t[1000];
	scanf("%d",&n);
	for(l=0;l<n;l++)
	{
		ans=0;
		scanf("%d",&s);
		for(i=0;i<s;i++)
		{
			scanf(" %[^\n]",t);
			a[i]=t;
			p[i]=0;
		}
		scanf("%d",&q);
		for(i=0;i<q;i++)
		{
			scanf(" %[^\n]",t);
			b[i]=t;
		}
		for(i=0;i<q;i++)
		{
			for(j=0;j<s;j++)
			{
				if(a[j]==b[i])
				{
					p[j]++;
					cz=0;
					for(k=0;k<s;k++)
					{
						if(p[k]==0)
							cz++;
					}
					if(cz==0)
					{
						ans++;
						for(k=0;k<s;k++)
							p[k]=0;
					}
					p[j]++;
				}
			}
		}
		printf("Case #%d: %d\n",(l+1),ans);
	}
	return 0;
}
