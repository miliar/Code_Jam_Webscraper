#include "stdio.h"
#include "string.h"
char ch[100];
int bian1[300][300],bian2[300][300],ok[300][300],mid[300][300],a[300],b[300],c[300],d[300];
int main()
{
	int tot,kase,j,l,i,k,r,x,y,z,res;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d",&r);
		x=y=105;
		z=0;
		for(i=0;i<=250;i++)
			for(k=0;k<=250;k++)
				mid[i][k]=ok[i][k]=bian2[i][k]=bian1[i][k]=0;
		while(r--)
		{
			scanf("%s%d",ch,&j);
			l=strlen(ch);
			while(j--)
			{
				for(i=0;i<l;i++)
				{
					if(ch[i]=='R')
					{
						z++;
						if(z==4)
							z=0;
					}
					else if(ch[i]=='L')
					{
						z--;
						if(z==-1)
							z=3;
					}
					else
					{
						if(z==0)
						{
							bian1[x][y]=1;
							y++;
						}
						else if(z==2)
						{
							y--;
							bian1[x][y]=1;
						}
						else if(z==1)
						{
							bian2[x][y]=1;
							x++;
						}
						else if(z==3)
						{
							x--;
							bian2[x][y]=1;
						}
					}
				}
			}
		}
		for(i=1;i<=210;i++)
			for(k=1;k<=210;k++)
				mid[i][k]=mid[i][k-1]+bian2[i][k];
		for(i=1;i<=210;i++)
			for(k=1;k<=210;k++)
				ok[i][k]=ok[i-1][k]+bian1[i][k];
		for(i=1;i<=210;i++)
			for(k=1;k<=210;k++)
			{
				if(mid[i][k]%2==1&&ok[i][k]%2==1)
					ok[i][k]=1;
				else
					ok[i][k]=0;
			}
		for(i=1;i<=210;i++)
		{
			a[i]=c[i]=-1;
			b[i]=d[i]=0x7fffffff;
		}
		for(i=1;i<=210;i++)
			for(k=1;k<=210;k++)
				if(ok[i][k]==1)
				{
					if(i>a[k])
						a[k]=i;
					if(k>c[i])
						c[i]=k;
					if(i<b[k])
						b[k]=i;
					if(k<d[i])
						d[i]=k;
				}
		res=0;
		for(i=1;i<=210;i++)
			for(k=1;k<=210;k++)
				if(ok[i][k]==0&&((i<a[k]&&i>b[k])||(k<c[i]&&k>d[i])))
					res++;
		printf("Case #%d: %d\n",kase,res);
	}
	return 0;
}