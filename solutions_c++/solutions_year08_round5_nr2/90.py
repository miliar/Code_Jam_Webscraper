#include <stdio.h>
#include <map>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

#define MAX 20

char t[MAX][MAX];

int pd[MAX][MAX][MAX][MAX][MAX][MAX];

int di[]={0,1,0,-1},dj[]={1,0,-1,0};

typedef struct pto
{
	int i,j;
} pto;

typedef struct ar
{
	pto u,v;
} ar;

typedef struct st{
	int c;
	pto p;
	ar port;
} st;

bool operator < (const pto & a, const pto & b)
{
	if(a.i!=b.i)
		return a.i<b.i;
	else
		return a.j<b.j;
}

bool operator < (const ar & a, const ar & b)
{
	if(a.u<b.u)
		return 1;
	if(b.u<a.u)
		return 0;
	return a.v<b.v;
}

bool operator < (const st & a, const st & b)
{
	if(a.c<b.c)
		return 1;
	if(b.c<a.c)
		return 0;
	if(a.p<b.p)
		return 1;
	if(b.p<a.p)
		return 0;
	return a.port<b.port;
}

pto ext[4];

void fext(int n,int m, const pto & p)
{
	int i=p.i,j=p.j;
	int k;
	for(k=0;k<4;++k)
	{
		i=p.i;j=p.j;

		while(i<n && i>=0 && j<m && j>=0 && t[i][j]!='#')
		{
			i+=di[k];
			j+=dj[k];
		}
		i-=di[k];
		j-=dj[k];
		ext[k].i=i;
		ext[k].j=j;
	}
}


int solve(int n,int m, pto beg)
{
	set<st> q;
	int i,j,k;
	st next,now;
	now.p=beg;
	now.c=0;
	fext(n,m,beg);
	for(i=0;i<4;++i)
	{
		now.port.u=ext[i];
		for(j=i+1;j<4;++j)
		{
			now.port.v=ext[j];
			pd[now.p.i][now.p.j][now.port.u.i][now.port.u.j][now.port.v.i][now.port.v.j]=0;
			q.insert(now);
		}
	}
	while(!q.empty())
	{
		now=*(q.begin());
		q.erase(q.begin());
		if(t[now.p.i][now.p.j]=='X')
			return now.c;
		next=now;
		fext(n,m,now.p);
		for(k=0;k<4;++k)
		{
			next.port.u=ext[k];
			if(pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]>next.c)
			{
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j];
				q.erase(next);
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]=now.c;
				q.insert(next);
			}
		}
		next.port.u=now.port.u;
		for(k=0;k<4;++k)
		{
			next.port.v=ext[k];
			if(pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]>next.c)
			{
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j];
				q.erase(next);
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]=now.c;
				q.insert(next);
			}
		}
		next.port.v=now.port.v;
		for(k=0;k<4;++k)
		{
			next.p.i=now.p.i+di[k];
			next.p.j=now.p.j+dj[k];
			next.c=now.c+1;
			if(next.p.i<n && next.p.i>=0 && next.p.j<m && next.p.j>=0 && t[next.p.i][next.p.j]!='#' &&
				pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]>next.c)
			{
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j];
				q.erase(next);
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]=now.c+1;
				q.insert(next);
			}
		}
		if(!(now.p<now.port.u) && !(now.port.u<now.p))
		{
			next.p=now.port.v;
			next.c=now.c+1;
			if(next.p.i<n && next.p.i>=0 && next.p.j<m && next.p.j>=0 && t[next.p.i][next.p.j]!='#' &&
				pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]>next.c)
			{
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j];
				q.erase(next);
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]=now.c+1;
				q.insert(next);
			}
		}
		if(!(now.p<now.port.v) && !(now.port.v<now.p))
		{
			next.p=now.port.u;
			next.c=now.c+1;
			if(next.p.i<n && next.p.i>=0 && next.p.j<m && next.p.j>=0 && t[next.p.i][next.p.j]!='#' &&
				pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]>next.c)
			{
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j];
				q.erase(next);
				next.c=pd[next.p.i][next.p.j][next.port.u.i][next.port.u.j][next.port.v.i][next.port.v.j]=now.c+1;
				q.insert(next);
			}
		}
	}
	return -1;
}

#define rep(ii,nn) for(ii=0;ii<nn;++ii)

int main()
{
	int a,b,c,d,e,f;
	int n,m;
	int i,j;
	int tc,cnt;
	int resp;
	pto now;
	scanf("%d",&tc);
	for(cnt=1;cnt<=tc;++cnt)
	{
		scanf("%d %d",&n,&m);
		rep(a,n) rep(b,m) rep(c,n) rep(d,m) rep(e,n) rep(f,m)
			pd[a][b][c][d][e][f]=10000;
		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
			{
				scanf(" %c",&t[i][j]);
				if(t[i][j]=='O')
				{
					now.i=i;
					now.j=j;
				}
			}
		resp=solve(n,m,now);
		printf("Case #%d: ",cnt);
		if(resp<0)
			printf("THE CAKE IS A LIE\n");
		else
			printf("%d\n",resp);
	}
	return 0;
}

