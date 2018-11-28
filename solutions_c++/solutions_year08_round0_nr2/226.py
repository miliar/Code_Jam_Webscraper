#include <iostream>
#include <vector>
#define MAXN 500
using namespace std;
typedef vector<vector<int> > graph;
graph map;


int nx,ny,matx[MAXN],maty[MAXN],fy[MAXN];

int path(int u)
{
	int v;
	for(int i=0;i<map[u].size();++i)
	{
		v=map[u][i];
		if(!fy[v])
		{
			fy[v]=1;
			if((maty[v]<0)||(path(maty[v])))
			{
				matx[u]=v;
				maty[v]=u;
				return 1;
			}
		}
	}
	return 0;
}

int hungary()
{
	int ret=0;
	memset(matx,0xff,sizeof(matx));
	memset(maty,0xff,sizeof(maty));
	for(int i=0;i<nx;++i)
	{
		if(matx[i]<0)
		{
			memset(fy,0,sizeof(fy));
			ret+=path(i);
		}
	}
	return ret;
}

int NA,NB,T;

struct node
{
	int s;
	int e;
};

node nodes[MAXN];
int ind[MAXN];

void work()
{
	int mat,res,ra,rb;
	memset(ind,0,sizeof(ind));
	for(int i=0;i<NA;++i)
		for(int j=NA;j<NA+NB;++j)
			if(nodes[i].e+T<=nodes[j].s)
				map[i].push_back(j);
	for(int i=NA;i<NA+NB;++i)
		for(int j=0;j<NA;++j)
			if(nodes[i].e+T<=nodes[j].s)
				map[i].push_back(j);
	nx=NA+NB;
	ny=NA+NB;
	mat=hungary();
	res=nx-mat;
	ra=0;
	for(int i=NA;i<NA+NB;++i)
		ind[matx[i]]++;
	for(int i=0;i<NA;++i)
		if(!ind[i]) ++ra;
	rb=res-ra;
	printf("%d %d\n",ra,rb);

}

int main()
{
	int n;
	int h,m;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%d%d%d",&T,&NA,&NB);
		map=graph(NA+NB);
		for(int j=0;j<NA+NB;++j)
		{
			scanf("%d:%d",&h,&m);
			nodes[j].s=h*60+m;
			scanf("%d:%d",&h,&m);
			nodes[j].e=h*60+m;
		}
		printf("Case #%d: ",i+1);
		work();
	}
	return 0;
}


