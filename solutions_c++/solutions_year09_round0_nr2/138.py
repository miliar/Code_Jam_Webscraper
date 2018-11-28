#include<stdio.h>
#include<map>
using namespace std;

#define N 10001

int n,m;
int a[101][101];

int parent[N],rank[N];
int find(int x)
{
	int r=x,q;
	while (r!=parent[r]) r=parent[r];
	while (x!=r) {
		q=parent[x];parent[x]=r;x=q;
	}
	return r;
}

void Union(int a,int b)
{ 
	//如果空间不够rank数组可以不用,此时union(a,b)等价于parent[find(a)]=find(b);
	int i,j;
	i=find(a); j=find(b);
	if(rank[i]>rank[j]) parent[j]=i;
	else 
	{
		parent[i]=j;
		if (rank[i]==rank[j]) rank[j]++;
	}
}

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

map<int,char> tree;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T,T1,i,j,dir;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d",&n,&m);
		
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		
		for (i=1;i<=n*m;i++) 
		{
			parent[i]=i;
			rank[i]=0;
		} //初始化

		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				int min=10001;
				int min_x,min_y;
				for(dir=0;dir<=3;dir++)
				{
					int x=i+dx[dir];
					int y=j+dy[dir];

					if(x<=0 || x>=n+1 || y<=0 || y>=m+1) continue;
					if(a[x][y]<min) 
					{
						min=a[x][y];
						min_x=x;
						min_y=y;
					}
				}
				if(min<a[i][j])
				{
					int tx=(i-1)*m+j;
					int ty=(min_x-1)*m+min_y;
					if (find(tx)!=find(ty))	Union(tx,ty);
				}
			}
		}		

		tree.clear();
		printf("Case #%d:\n",T1);
		char cur_char='a';
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				int t=(i-1)*m+j;
				int tnum=find(t);
				if(!tree[tnum]) tree[tnum]=cur_char++;


				if(j==m) printf("%c\n",tree[tnum]);
				else printf("%c ",tree[tnum]);
			}
		}
	}
	return 0;
}