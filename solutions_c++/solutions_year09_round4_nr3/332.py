#include<iostream>

using namespace std;

int n,zz,k,d[200][200];

bool checker(int x,int y)
{
	for(int i=1;i<=k;++i)
		if(d[x][i]>=d[y][i])
			return false;
	return true;
}

struct edge
{
	int v,f;
	edge *next,*pai;
	edge (int v,int f,edge *next,edge *pai) : v(v),f(f),next(next),pai(pai) {}
}*e[1000];

int s,t,level[1000],q[1000],h,l,ans;
bool flag[1000];

inline bool makelevel()
{
	memset(level,0,sizeof(level));
	level[s]=1;
	q[l=1]=s;
	h=0;
	for(;h++!=l;)
	{
		int u=q[h];
		for(edge *r=e[u];r;r=r->next)
		    if(!level[r->v]&&r->f)
		    {
		    	level[r->v]=level[u]+1;
		    	if(r->v==t)
		    	    return 1;
  	            q[++l]=r->v;
		    }
	}
	return 0;
}

int dfs(int u,int low)
{
	int out=0;
	if(u==t)
		return low;
	for(edge *r=e[u];r;r=r->next)
    	if(!flag[r->v]&&level[u]==level[r->v]-1&&r->f)
        {
        	int p=dfs(r->v,min(low-out,r->f));
        	r->f-=p;
        	r->pai->f+=p;
        	out+=p;
        	if(out==low)
        	    return out;
        }
	flag[u]=1;
    return out;
}

inline void dinic()
{
	for(;makelevel();memset(flag,0,sizeof(flag)))
	    ans+=dfs(s,1<<30);
}

inline void insert(int u,int v,int f)
{
	e[u]=new edge(v,f,e[u],0);
	e[v]=new edge(u,0,e[v],e[u]);
	e[u]->pai=e[v];
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&zz);
	for(int p=1;p<=zz;++p)
	{
		scanf("%d %d",&n,&k);
		ans=s=0;
		t=299;
		memset(e,0,sizeof(e));
		memset(level,0,sizeof(level));
		memset(flag,0,sizeof(flag));
		memset(q,0,sizeof(q));
		for(int i=1;i<=n;++i)
			for(int j=1;j<=k;++j)
				scanf("%d",&d[i][j]);
		for(int i=1;i<=n;++i)
			for(int j=1;j<=n;++j)
				if(checker(i,j))
					insert(i,j+n,1);
		for(int i=1;i<=n;++i)
			insert(0,i,1);
		for(int i=n+1;i<=n<<1;++i)
			insert(i,t,1);
		dinic();
		printf("Case #%d: %d\n",p,n-ans);
	}
	return 0;
}
