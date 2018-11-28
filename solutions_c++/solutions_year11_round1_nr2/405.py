#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int vis[15][30],ll[15],p[15],ne[30],used[10005];
char gus[30];
struct N
{
	char s[15];
	int len;
	int f[30];
}d[10005];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(ll,0,sizeof(ll));
		memset(vis,0,sizeof(vis));
		memset(d,0,sizeof(d));
		int n,m;
		scanf("%d%d",&n,&m);
		int i,j,k;
		for(i=0;i<n;i++)
		{
			scanf("%s",d[i].s);
			d[i].len=strlen(d[i].s);
			ll[d[i].len]++;
			for(j=0;j<d[i].len;j++)
			{
				vis[d[i].len][d[i].s[j]-'a']++;
				d[i].f[d[i].s[j]-'a']++;
			}
		}
		printf("Case #%d:",cas);
		for(i=0;i<m;i++)
		{
			int ans=-1,tmp,res,sum;
			memset(gus,0,sizeof(gus));
			scanf("%s",gus);
			for(j=0;j<n;j++)
			{
				memset(used,0,sizeof(used));
				tmp=0;
				if(ll[d[j].len]==1)
					if(tmp>ans)
					{
						ans=tmp;
						res=j;
						continue;
					}
				for(k=0;k<26;k++)
					ne[k]=vis[d[j].len][k];
				sum=ll[d[j].len];
				for(k=0;k<26;k++)
				{
					if(sum==1)
						break;
					int r;
					if(ne[gus[k]-'a']==0)
						continue;
					int num=d[j].f[gus[k]-'a'];
					if(num>0)
					{
						memset(p,0,sizeof(p));
						int flag=0;
						for(r=0;r<d[j].len;r++)
							if(d[j].s[r]==gus[k])
								p[r]=1;
						for(r=0;r<n;r++)
							if(!used[r]&&d[r].len==d[j].len&&d[r].f[gus[k]-'a']==num)
							{
								flag=1;
								int ss;
								for(ss=0;flag&&ss<d[r].len;ss++)
									if(p[ss]==1&&d[r].s[ss]!=gus[k])
										flag=0;
								if(flag==0)
								{
									used[r]=1;
									sum--;
									for(ss=0;ss<d[j].len;ss++)
										ne[d[r].s[ss]-'a']--;
								}
							}
							else if(!used[r]&&d[r].len==d[j].len&&d[r].f[gus[k]-'a']!=num)
							{
								used[r]=1;
								int ss;
								sum--;
								for(ss=0;ss<d[j].len;ss++)
									ne[d[r].s[ss]-'a']--;
							}
					}
					else
					{
						tmp++;
						for(r=0;r<n;r++)
							if(!used[r]&&d[r].len==d[j].len&&d[r].f[gus[k]-'a']>0)
							{
								used[r]=1;
								int ss;
								sum--;
								for(ss=0;ss<d[j].len;ss++)
									ne[d[r].s[ss]-'a']--;
							}
					}
				}
				if(tmp>ans)
				{
					ans=tmp;
					res=j;
				}
			}
			printf(" %s",d[res].s);
		}
		printf("\n");
	}
	return 0;
}
