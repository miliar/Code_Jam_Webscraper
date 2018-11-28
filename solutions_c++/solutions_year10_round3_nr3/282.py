#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int n,m;
int c[1000];
struct R
{
	int sz;
	int cnt;
}r[10000];
int r_cnt=0;
bool del[100][100];
bool mat[100][100];
int up;
bool find()
{
	int i,j,k,sz,u,v;
	int ms=-1,mx,my;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(del[i][j])
				continue;
			for(sz=0;;sz++)
			{
				if(i+sz>=n||j+sz>=m)
					break;
				for(u=i;u<=i+sz;u++)
				{
					for(v=j;v<=j+sz;v++)
					{
						if(del[u][v]||(v>j&&mat[u][v]==mat[u][v-1]))
							break;
						else if(u>i&&mat[u][v]==mat[u-1][v])
							break;
					}
					if(v<=j+sz)
						break;
				}
				if(u<=i+sz)
					break;
				if(sz>ms)
				{
					ms=sz;
					mx=i,my=j;
				}
			}
		}
	}
	if(ms==-1)
		return 0;
	for(u=mx;u<=mx+ms;u++)
	{
		for(v=my;v<=my+ms;v++)
		{
			del[u][v]=1;
		}
	}
	if(r_cnt==0||ms<r[r_cnt-1].sz)
	{
		r[r_cnt].sz=ms;
		r[r_cnt].cnt=1;
		r_cnt++;
	}
	else
	{
		r[r_cnt-1].cnt++;
	}
	return 1;

}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("f.out","w",stdout);
	int i,j,k;
	int T;
	int case_cnt=1;
	scanf("%d",&T);
	while(T--)
	{
		memset(r,0,sizeof(r));
		memset(del,0,sizeof(del));
		memset(mat,0,sizeof(mat));
		r_cnt=0;
		scanf("%d%d",&n,&m);
		up=(1<<m)-1;
		for(i=0;i<n;i++)
		{
			scanf("%x",&c[i]);
			for(j=m-1;j>=0;j--)
			{
				if( (c[i]&(1<<j)))
					mat[i][m-j-1]=1;
				else
					mat[i][m-j-1]=0;
			}
		}
		while(find());
		printf("Case #%d: %d\n",case_cnt++,r_cnt);
		for(i=0;i<r_cnt;i++)
		{
			printf("%d %d\n",r[i].sz+1,r[i].cnt);
		}
	}
}