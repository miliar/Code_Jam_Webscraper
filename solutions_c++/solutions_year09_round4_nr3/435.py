#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T,N,M,n;
struct ss
{
	int p[32];
}stock[128];
int used[128];
int r[128][128];
int er[18];
int may[65536*2],tot[65536*2];
int dy[65536*2],num_dy;
int list[65536];

int upp(int a,int b)
{
	if (a>b)
		return 1;
	if (a==b)
		return 0;
	return -1;
}

bool cmp(const struct ss a,const struct ss b)	
{
	int i=0;
	
	while (a.p[i]==b.p[i] && i<M)
		i++;
	if (i==M)
		return 0;
	return a.p[i]<b.p[i];
}

int check(int x)
{
	int j,k;
	
	for (j=0;j<N;j++)
		{
			for (k=j+1;k<N;k++)
			{
				if (er[j] & x)
				{
					if (er[k] & x)
					{
						if (r[j][k]==0)
							return 0;
					}
				}
			}
		}
	return 1;
}

void init()
{
	int i,j,k,ok;
	
	scanf("%d%d",&N,&M);
	memset(r,0,sizeof(r));
	memset(used,0,sizeof(used));
	memset(may,0,sizeof(may));
	memset(tot,0,sizeof(tot));
	er[0]=1;
	for (i=1;i<=17;i++)
	{
		er[i]=er[i-1]<<1;
	}
	for (i=0;i<N;i++)
	{
		for (j=0;j<M;j++)
		{
			scanf("%d",&stock[i].p[j]);
		}
	}
	
	//sort(stock,stock+N,cmp);
	memset(r,0,sizeof(r));
	for (i=0;i<N;i++)
	{
		for (j=i+1;j<N;j++)
		{
			ok=1;
			for (k=0;k<M-1;k++)
			{
				if (upp(stock[i].p[k],stock[j].p[k]) * upp(stock[i].p[k+1],stock[j].p[k+1]) <=0 )
				{
					ok=0;
					break;
				}
			}
			r[i][j]=r[j][i]=ok;
		}
	}
	
	num_dy=0;
	n=(1<<N)-1;
	for (i=n;i>=1;i--)
	{
		may[i]=check(i);
		if (may[i]==1)
		{
			dy[num_dy++]=i;
			//printf("%d ",i);
		}
	}
	//printf("\n");
}

int work()
{
	int i,j,k;
	int open,closed;
	
	/*int group[128];
	
	memset(used,0,sizeof(used));
	for (i=0;i<N;i++)
	{		
		if (used[i])
			continue;
		used[i]=1;
		tot++;
		memset(group,0,sizeof(group));
		group[1]=i;
		num=1;
		
		for (j=i+1;j<N;j++)
		{
			if (used[j])
				continue;
			
			if (r[group[num]][j])
			{
				group[++num]=j;
				used[j]=1;
			}
		}
	}
	
	return tot;*/
	
	open=0;
	closed=1;
	list[1]=0;
	while (open<closed && tot[n]==0)
	{
		open++;
		i=list[open];
		for (j=0;j<num_dy;j++)
		{
			if ((dy[j] & i)==0)
			{
				k=dy[j] | i;
				if (tot[k]==0)
				{
					tot[k]=tot[i]+1;
					closed++;
					list[closed]=k;
					if (k==n)
						break;
				}
			}
		}
		
	}
	return tot[n];
}

int main()
{
	int i;
	
	freopen("c-small-attempt2.in","r",stdin);
	freopen("c-small-try.out","w",stdout);
	scanf("%d",&T);
	for (i=1;i<=T;i++)
	{
		init();
		printf("Case #%d: %d\n",i,work());
	}
	
	return 0;
}
