#include<iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

#define maxn 55

char Maze[maxn][maxn];
char Temp_Maze[maxn][maxn];

bool blue,red;
int Test,N,K;

int dir[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

inline bool Illegal(int i,int j)
{
	return i>=1 && i<=N && j>=1 && j<=N;
}

void FindK();

void Solve();

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int i,j;
	int Cases=1;
	scanf("%d",&Test);
	while( Test--)
	{
		scanf("%d%d",&N,&K);
		for(int i=N;i>=1;i--)
		{
			scanf(" %s",Temp_Maze[i]+1);
		}

		for(int i=1;i<=N;i++)
		{
			for(int j=1;j<=N;j++)
			{
				Maze[N-j+1][i]=Temp_Maze[i][j];
			}
		}

		Solve();

		blue=red=false;

		FindK();

		printf("Case #%d: ",Cases++);
		if( red && blue )
			puts("Both");
		else if( !red && !blue) 
			puts("Neither");
		else if( red ) 
			puts("Red");
		else 
			puts("Blue");
	}
}


void FindK()
{
	int i,j;
	for(i=1;i<=N;i++)
	{
		for(j=1;j<=N;j++)
		{
			if( Maze[i][j]=='B')
			{
				if( blue ) continue;
				for(int in=0;in<8;in++)
				{
					bool can=true;
					int k=K;
					while( k-- )
					{
						int x=i+dir[in][0]*k;
						int y=j+dir[in][1]*k;
						if( Illegal(x,y) && Maze[x][y]=='B') continue;
						else can=false;
					}
					if( can ) blue=true;
				}
			}
			if( Maze[i][j]=='R') 
			{
				if( red ) continue;
				for(int in=0;in<8;in++)
				{
					bool can=true;
					int k=K;
					while( k-- )
					{
						int x=i+dir[in][0]*k;
						int y=j+dir[in][1]*k;
						if( Illegal(x,y) && Maze[x][y]=='R') continue;
						else can=false;
					}
					if( can ) red=true;
				}
			}
		}
	}
}

void Solve()
{
	int i,j;
	for(j=1;j<=N;j++)
	{
		int ind=1;
		for(i=1;i<=N;i++)
			if( Maze[i][j]!='.') 
				Maze[ind++][j]=Maze[i][j];
		while(ind<=N) Maze[ind++][j]='.';
	}
}