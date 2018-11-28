#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>
#include<queue>
using namespace std;

#define INF 0x7fffffff

struct node
{
	int x,y,h;
}pp,qq;

bool operator<(node p,node q)
{
	return p.h<q.h;
}

int h[10005];
char f[10005];

int find(int t)
{
	if(h[t]!=t)
		h[t]=find(h[t]);
	return h[t];
}

int main()
{
	int t,c,n,m,i,j,k,mp[105][105],dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}},s,si,p,q;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		scanf("%d%d",&n,&m);
		priority_queue<node> pq;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				scanf("%d",&mp[i][j]);
				h[i*m+j]=i*m+j;
				pp.x=i,pp.y=j,pp.h=mp[i][j];
				pq.push(pp);
			}
		while(!pq.empty())
		{
			pp=pq.top();
			pq.pop();
			s=INF;
			si;
			for(i=0;i<4;i++)
			{
				qq.x=pp.x+dir[i][0];
				qq.y=pp.y+dir[i][1];
				if(qq.x<0||qq.x>=n||qq.y<0||qq.y>=m)
					continue;
				qq.h=mp[qq.x][qq.y];
				if(pp.h>qq.h&&s>qq.h)
					s=qq.h,si=i;
			}
			if(s==INF)
				continue;
			qq.x=pp.x+dir[si][0];
			qq.y=pp.y+dir[si][1];
			qq.h=mp[qq.x][qq.y];
			p=find(pp.x*m+pp.y);
			q=find(qq.x*m+qq.y);
			if(p!=q)
				h[p]=q;
			pq.push(qq);
		}
		memset(f,-1,sizeof(f));
		k=0;
		printf("Case #%d:\n",c);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				p=find(i*m+j);
				if(f[p]==-1)
					f[p]='a'+k,k++;
				if(j==0)
					printf("%c",f[p]);
				else
					printf(" %c",f[p]);
			}
			printf("\n");
		}
	}
}