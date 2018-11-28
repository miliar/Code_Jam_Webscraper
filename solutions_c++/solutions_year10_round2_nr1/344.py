#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;


const	int	NN=100005,MM=155;
struct	Edge
{
	int	v,next;
} w[5000055];
char	name[NN][MM];
char	st[MM],st2[MM];
int	start[NN];
int	n,m,N,i,j,k,p,x,r,W,len,Ans,nn;
int	TEST,t;


inline	int	Find(char s[])
{
	for (int i=1;i<=N;++i) if (!strcmp(s,name[i])) return i;
	strcpy(name[++N],s); return N;
}

inline	void	AddEdge(int u,int v)
{
	w[++W].v=v; w[W].next=start[u]; start[u]=W;
}

int	main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	for (scanf("%d",&TEST),t=1;t<=TEST;++t)
	{
		scanf("%d%d",&m,&n);
		N=W=Ans=0;
		memset(start,0,sizeof(start));
		for (i=1;i<=m;++i)
		{
			scanf("%s",st+1); len=strlen(st+1);
			st[++len]='/';
			for (p=1,r=0,j=2;j<=len;++j)
			if (st[j]=='/')
			{
				for (k=1;k<j;++k) st2[k-1]=st[k];
				st2[j-1]=0;
				x=Find(st2);
				AddEdge(r,x);
				r=x; p=j;
			}
		}
		
		bool	flag;
		for (i=1;i<=n;++i)
		{
			scanf("%s",st+1); len=strlen(st+1);
			st[++len]='/';
			for (p=1,r=0,j=2;j<=len;++j)
			if (st[j]=='/')
			{
				for (k=1;k<j;++k) st2[k-1]=st[k];
				st2[j-1]=0;
				nn=N;
				x=Find(st2);
				if (nn==N) continue;
				AddEdge(r,x); ++Ans;
				r=x; p=j;
			}
		}
		printf("Case #%d: %d\n",t,Ans);
	}
	
	return 0;
}
