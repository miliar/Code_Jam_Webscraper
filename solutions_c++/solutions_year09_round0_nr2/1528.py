#include<cstdio>
#define NMAX 100
using namespace std;
int A[NMAX][NMAX],L[NMAX][NMAX],C[NMAX][NMAX],T,N,M;
int Dx[]={-1,0,0,1},Dy[]={0,-1,1,0};
char Ans[NMAX][NMAX];

void fill(int i, int j, char c)
{
	int d,x,y;

	Ans[i][j]=c;
	if(!Ans[L[i][j]][C[i][j]])
		fill(L[i][j],C[i][j],c);

	for(d=0;d<4;++d)
	{
		x=i+Dx[d]; y=j+Dy[d];
		if(x>=0 && y>=0 && x<N && y<M && L[x][y]==i && C[x][y]==j && !Ans[x][y])
			fill(x,y,c);
	}
}

int main()
{
	char ch;
	int i,j,t,l,c,d,x,y;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&T);
	for(t=1;t<=T;++t)
	{
		scanf("%d%d",&N,&M);
		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				scanf("%d",&A[i][j]), Ans[i][j]=0;

		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
			{
				l=i; c=j;
				for(d=0;d<4;++d)
				{
					x=i+Dx[d]; y=j+Dy[d];
					if(x>=0 && y>=0 && x<N && y<M && A[x][y]<A[l][c])
						l=x, c=y;
				}
				L[i][j]=l; C[i][j]=c;
			}

		ch='a';
		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				if(!Ans[i][j])
					fill(i,j,ch++);

		printf("Case #%d:\n",t);
		for(i=0;i<N;++i)
		{
			for(j=0;j<M-1;++j)
				printf("%c ",Ans[i][j]);
			printf("%c\n",Ans[i][j]);
		}
	}

	return 0;
}
