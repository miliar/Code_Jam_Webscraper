#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
int mark[12000],p[12000],pt;
void init()
{
	int i,j;
	memset(mark,0,sizeof(mark));
	pt=0;
	for(i=2;i<=1000;i++)
	{
		if(mark[i])continue;
		p[pt++]=i;
		for(j=2;j*i<=1000;j++)
		mark[i*j]=1;
	}
}
int ct[1200][1200],lt[1200],use[1200][1200],un[1200];
bool cs[1200];
int ans[1200];
int _,ca,n,i,j,k,l,te,ma,mi;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	init();ans[1]=0;
	memset(ct,0,sizeof(ct));
	memset(lt,0,sizeof(lt));
	memset(cs,0,sizeof(cs));
	memset(un,0,sizeof(un));
	ma=1;
	for(i=2;i<=1000;i++)
	{
	//	printf("%d\n",i);
		int x=i;
		bool dn=false;
		for(j=0;j<pt;j++)
		{
			if(x%p[j]==0)
			{
				while(x%p[j]==0)
				{
					ct[i][j]++;x/=p[j];
				}
				if(ct[i][j]>lt[j])
				{
					dn=true;
					lt[j]=ct[i][j];
					un[j]=0;
				}
			}
		}
		if(dn)
		{
			ma++;cs[i]=1;
			for(j=0;j<pt;j++)
			{
				if(ct[i][j]==lt[j])
				{
					use[j][un[j]++]=i;
				}
			}
			for(j=0;j<i;j++)
			{
				if(cs[j])
				{
					bool can=true;
					for(k=0;k<pt;k++)
					{
						if(ct[j][k]>0&&ct[j][k]==lt[k])
						{
							if(un[k]==1)
							{can=false;break;}
						}
					}
					if(can)
					{
						cs[j]=0;
						for(k=0;k<pt;k++)
						{
							if(ct[j][k]>0&&ct[j][k]==lt[k])
							{
								te=0;
								for(int l=0;l<un[k];l++)
								{
									if(use[k][l]!=j)
									{
										use[k][te++]=use[k][l];
									}
								}
								un[k]=te;
							}
						}
						break;
					}
				}
			}
		}
		mi=0;
		for(j=1;j<=i;j++)if(cs[j])mi++;
		ans[i]=ma-mi;
	}
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		scanf("%d",&n);
		printf("Case #%d: %d\n",ca,ans[n]);
	}
}
