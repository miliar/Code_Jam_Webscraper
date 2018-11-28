#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int N,M,K,F[100][100],O[10000][2];
int H[100][100];
int bas;

struct elem
{
	int i,j;
}p[10001];

bool comp(elem a,elem b)
{
	return F[a.i][a.j]<F[b.i][b.j];
}

int get_min(int i,int j)
{
	int a,b;
	a=b=-1;
	if(i>0 && F[i-1][j]<F[i][j])
	{
		a=0;
		b=F[i-1][j];
	}
	if(j>0 && F[i][j-1]<F[i][j] && (a==-1 || F[i][j-1]<b))
	{
		a=1;
		b=F[i][j-1];
	}
	if(j<M-1 && F[i][j+1]<F[i][j] && (a==-1 || F[i][j+1]<b))
	{
		a=2;
		b=F[i][j+1];
	}
	if(i<N-1 && F[i+1][j]<F[i][j] && (a==-1 || F[i+1][j]<b))
	{
		a=3;
		b=F[i+1][j];
	}
	return a;
}

void bfs(int si,int sj)
{
	int i,j,last=1,k,a;
	O[0][0]=si;
	O[0][1]=sj;
	H[si][sj]=bas;
	for(k=0;k<last;k++)
	{
		i=O[k][0];
		j=O[k][1];
		if(i>0 && H[i-1][j]>=0 && F[i-1][j]>F[i][j])
		{
			a=get_min(i-1,j);
			if(a==3)
			{
				H[i-1][j]=bas;
				O[last][0]=i-1;
				O[last][1]=j;
				last++;
			}
		}
		if(i<N-1 && H[i+1][j]>=0 && F[i+1][j]>F[i][j])
		{
			a=get_min(i+1,j);
			if(a==0)
			{
				H[i+1][j]=bas;
				O[last][0]=i+1;
				O[last][1]=j;
				last++;
			}
		}
		if(j>0 && H[i][j-1]>=0 && F[i][j-1]>F[i][j])
		{
			a=get_min(i,j-1);
			if(a==2)
			{
				H[i][j-1]=bas;
				O[last][0]=i;
				O[last][1]=j-1;
				last++;
			}
		}
		if(j<M-1 && H[i][j+1]>=0 && F[i][j+1]>F[i][j])
		{
			a=get_min(i,j+1);
			if(a==1)
			{
				H[i][j+1]=bas;
				O[last][0]=i;
				O[last][1]=j+1;
				last++;
			}
		}
	}
}

void bfs1(int si,int sj,int l)
{
	int i,j,last=1,k,con;
	O[0][0]=si;
	O[0][1]=sj;
	con=H[si][sj];
	H[si][sj]=l;
	for(k=0;k<last;k++)
	{
		i=O[k][0];
		j=O[k][1];
		if(i>0 && H[i-1][j]==con)
		{
			H[i-1][j]=l;
			O[last][0]=i-1;
			O[last][1]=j;
			last++;
		}
		if(i<N-1 && H[i+1][j]==con)
		{
			H[i+1][j]=l;
			O[last][0]=i+1;
			O[last][1]=j;
			last++;
		}
		if(j>0 && H[i][j-1]==con)
		{
			H[i][j-1]=l;
			O[last][0]=i;
			O[last][1]=j-1;
			last++;
		}
		if(j<M-1 && H[i][j+1]==con)
		{
			H[i][j+1]=l;
			O[last][0]=i;
			O[last][1]=j+1;
			last++;
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,i,j,s;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&N,&M);
		for(i=0;i<N;i++)
			for(j=0;j<M;j++) scanf("%d",&F[i][j]);
		K=0;
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
			{
				p[K].i=i;
				p[K].j=j;
				K++;
				H[i][j]=1;
			}
		sort(p,p+K,comp);
		bas=-1;
		for(i=0;i<K;i++)
			if(H[p[i].i][p[i].j]==1)
			{
				bfs(p[i].i,p[i].j);
				bas--;
			}
		int ks=0;
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				if(H[i][j]<0)
				{
					bfs1(i,j,ks);
					ks++;
				}
		printf("Case #%d:\n",t);
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
				printf("%c ",'a'+H[i][j]);
			printf("\n");
		}

	}
	return 0;
}