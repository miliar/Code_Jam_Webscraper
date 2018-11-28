#include "stdio.h"
int res[1100],boo[1005],f[11][1005],lis[1005],ll;
int main()
{
	char ch;
	int e=0,t;
	int i,k,j,l,p,q,n,m;
	for(i=0;i<=1024;i++)
		res[i]=0;
	for(i=2;i<=10;i++)
		for(k=0;k<=1000;k++)
			f[i][k]=0;
	for(j=0;j<=1000;j++)
		boo[j]=0;
	l=0;
	for(i=2;l<511;i++)
	{
		p=0;
		for(k=2;k<=10;k++)
		{
			ll=0;
			q=i;
			while(1)
			{
				m=0;
				j=0;
				while(q>0)
				{
					n=q%k;
					q/=k;
					j+=n*n;
				}
				q=j;
				if(f[k][q]==1)
				{
					q=1;
					break;
				}
				else if(f[k][q]==-1)
				{
					q=0;
					break;
				}
				if(q==1||boo[q]==1)
					break;
				boo[q]=1;
				lis[ll++]=q;
			}
			if(q==1)
			{
				p+=(1<<(k-2));
				for(j=0;j<ll;j++)
				{
					boo[lis[j]]=0;
					f[k][lis[j]]=1;
				}
			}
			else
			{
				for(j=0;j<ll;j++)
				{
					f[k][lis[j]]=-1;
					boo[lis[j]]=0;
				}
			}
		}
		if(res[p]==0)
		{
			for(k=1;k<=511;k++)
			{
				if((k|p)==p&&res[k]==0)
				{
					res[k]=i;
					l++;
				}
			}
		}
	}
	scanf("%d",&t);
	j=0;
	for(j=1;j<=t;j++)
	{
		p=0;
		while(1)
		{
			scanf("%d",&q);
			ch=getchar();
			p+=(1<<(q-2));
			if(ch=='\n')
				break;
		}
		printf("Case #%d: %d\n",j,res[p]);
	}
	return 0;
}