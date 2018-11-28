#include<iostream>
#include<queue>
using namespace std;

#define MAXN 128
#define INF 1<<30
int M,N,mat[MAXN][MAXN],lab[MAXN][MAXN],mv[4][2]={-1,0,0,-1,0,1,1,0};
void init ( )
{
	scanf("%d%d",&N,&M);
	for ( int i=0 ; i<N ; i++ )
		for ( int j=0 ; j<M ; j++ )
			scanf("%d",&mat[i][j]);
	memset(lab,-1,sizeof(lab));
}

bool in ( int tr , int tc )
{
	return  tr>=0 && tr<N && tc>=0 && tc<M;
}
void floodfill ( int r, int c , int& v )
{
	int k,tr,tc,i,Min;
	for ( Min=INF,i=0 ; i<4 ; i++ )
	{
		tr=r+mv[i][0],tc=c+mv[i][1];
		if ( in(tr,tc) && mat[tr][tc]<mat[r][c] && Min>mat[tr][tc] )
		{
			Min=mat[tr][tc];
			k=i;
		}
	}
	if ( Min!=INF )
	{
		tr=r+mv[k][0],tc=c+mv[k][1];
		if ( lab[tr][tc]!=-1 )
		{
			v=lab[tr][tc];
			lab[r][c]=v;
			return;
		}
		floodfill(tr,tc,v);
		lab[r][c]=v;
	}
	else
	{
		if ( lab[r][c]==-1 )
			lab[r][c]=v;
		else
		{
			lab[r][c]=min(v,lab[r][c]);
			v=lab[r][c];
		}
		return;
	}
}


int main ( )
{
	int i,j,k,cas,tot,t;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cas);
	for ( k=1;  k<=cas; k++ )
	{
		init();
		for ( tot=-1,i=0 ; i<N ; i++ )
			for ( j=0 ; j<M ; j++ )
			{
				if ( lab[i][j]==-1 )
				{
					tot++;
					t=tot;
					floodfill(i,j,t);
					if ( t<tot )
						tot--;
				}
			}
		printf("Case #%d:\n",k);
		for ( i=0 ; i<N ; i++ )
		{
			for ( j=0 ; j<M ; j++ )
			{
				if ( j )
					printf(" ");
				printf("%c",lab[i][j]+'a');
			}
			printf("\n");
		}

	}
}

/*
a a a
b a a 
b b a
*/