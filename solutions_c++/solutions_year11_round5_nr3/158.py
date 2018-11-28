#include "stdio.h"
#include "string.h"
#include "math.h"
#include <algorithm>
using namespace std;
#define M 110

bool notp[M];//素数判定
int pr[110000],pn,ans;//pr存放素数,pn当前素数个数。
void getprime()
{
	pn=0;
	memset(notp,0,sizeof(notp));
	for(int i=2;i<M;i++) 
	{
		if(!notp[i])
			pr[pn++]=i;
		for(int j=0;j<pn && pr[j]*i<M;j++) 
		{
			notp[pr[j]*i]=1;
			if(i%pr[j]==0)break;
		}
	}
	//pr[pn++]=M;
}

int r,c;
char s[M][M];
int move[]={-1,0,1,0,-1};//n,e,s,w
int a[M][M];
int rr[M][M];

bool dfs(int x,int y,int k)
{
	int i,nx,ny;
	if(a[x][y])
	{
		switch(s[x][y])
		{
		case '|':nx=(x+r-1)%r;
			ny=y;
			break;
		case '-':ny=(y+c-1)%c;
			nx=x;
			break;
		case '\\':nx=(x+r-1)%r;
			ny=(y+c-1)%c;
			break;
		case char(47):nx=(x+r-1)%r;
			ny=(y+1)%c;
			break;
		default:return 0;
		}
	}
	else
	{
		switch(s[x][y])
		{
		case '|':nx=(x+1)%r;
			ny=y;
			break;
		case '-':ny=(y+1)%c;
			nx=x;
			break;
		case '\\':nx=(x+1)%r;
			ny=(y+1)%c;
			break;
		case char(47):nx=(x+1)%r;
			ny=(y+c-1)%c;
			break;
		default:return 0;
		}
	}
	if(rr[x][y]==0)
		rr[x][y]=k;
	if(rr[nx][ny]==0)
	{
		return dfs(nx,ny,k);
	}
	else
		return rr[nx][ny]==-rr[x][y];
}

int main()
{
	int i,j,k,t,tc=1;
	int pi,pj,pk;
	int ans;
	freopen("gcj/2011.6.11/C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	//getprime();
	while(t--)
	{
		printf("Case #%d: ", tc++);
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
		{
			scanf("%s",s[i]);
		}
		ans=0;
		for(i=0;i<(1<<(r*c));i++)
		{
			k=i;
			if(k==408)
				k=k;
			memset(a,0,sizeof(a));
			for(j=0;j<r*c&&k;j++,k>>=1)
			{
				if(k&1)
				{
					a[j%r][j/r]=1;
				}
			}
			memset(rr,0,sizeof(rr));
			pk=1;
			for(pi=0;pi<r;pi++)
			{
				for(pj=0;pj<c;pj++)
				{
					if(!rr[pi][pj])
					{
						rr[pi][pj]=-pk;
						if(dfs(pi,pj,pk))
						{
							pk++;
							continue;
						}
						else
							break;
					}
				}
				if(pj<c)
					break;
			}
			if(pi<r)
				continue;
			ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}

/*
3
3 3
|-/
|||
--|
3 4
----
||||
\\//
4 4
|---
\-\|
\|||
|--\
*/

