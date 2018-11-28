#include <cstdio>
#include <cstring>
#include <algorithm>
#define Sort sort

using namespace std;

const int Maxn=1010;

int r[Maxn];
int line;
int id[Maxn];
int ans[Maxn][2];
int res[Maxn][2];
int n,m,Test,w,l;
bool Find;

bool Cmp(int A,int B)
{
	return r[A]<r[B];
}

void Work()
{
	int node=0;
	line=0;
	int j=0;
	res[node][0]=0;res[node][1]=0;
	line=j=r[id[node]]/2;++node;
	for (;j+r[id[node]]/2<=l && node<n;++node) 
	{
		res[node][0]=0;res[node][1]=j+r[id[node]]/2;
		line=max(line,r[id[node]]/2);
		j+=r[id[node]];
	}
	for (;node<n;)
	{
		int u=line;
		res[node][0]=u+r[id[node]]/2;
		res[node][1]=0;
		line=u+r[id[node]];j=r[id[node]]/2;++node;
		for (;j+r[id[node]]/2<=l && node<n;++node)
		{
			res[node][0]=u+r[id[node]]/2;
			res[node][1]=j+r[id[node]]/2;
			line=max(line,u+r[id[node]]);
			j+=r[id[node]];
		}
	}
	bool mark=true;
	for (int i=0;i<n;++i)
		if (res[i][0]>w) mark=false;
	if (mark)
	{
		Find=true;
		for (int i=0;i<n;++i) 
		{
			ans[id[i]][0]=res[i][0];
			ans[id[i]][1]=res[i][1];
		}
		for (int i=0;i<n;++i) printf(" %d %d",ans[i][0],ans[i][1]);
		printf("\n");
	}
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	scanf("%d",&Test);
	//printf("%d\n",Test);
	for (int ii=1;ii<=Test;++ii)
	{
		printf("Case #%d:",ii);
		scanf("%d%d%d",&n,&w,&l);
		//printf("%d %d %d\n",n,w,l);
		for (int i=0;i<n;++i)
		{
			scanf("%d",&r[i]);
			//printf("%d ",r[i]);
			r[i]*=2;
		}
		//printf("\n");
		for (int i=0;i<n;++i) id[i]=i;
		Sort(id,id+n,Cmp);
		
		Find=false;
		Work();
		if (Find) continue;
		for (;!Find;)
		{
			for (int i=0;i<10000;++i)
			{
				int x=rand() % n;
				int y=rand() % n;
				swap(id[x],id[y]);
			}
			Work();
		}
	}
	
	return 0;
}
		
		