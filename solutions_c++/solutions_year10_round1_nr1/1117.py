#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define MAX 100
using namespace std;

int N,K;
char grid[MAX][MAX];

bool read()
{
	memset(grid,0,sizeof grid);
	scanf("%d %d",&N,&K);
	for(int i=0;i<N;i++)
		scanf("%s",grid[i]);
	return true;
}

void print()
{
	for(int i=0;i<N;i++) puts(grid[i]);
	puts("");
}

void rotate()
{
	char tmp[MAX][MAX];
	memset(tmp,0,sizeof tmp);
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			tmp[i][j]=grid[N-j-1][i];
	memcpy(grid,tmp,sizeof tmp);
}

void gravity()
{
	// adjust columns
	for(int i=0;i<N;i++) // for each column
	{
		int sz=0;
		char tmp[MAX];
		memset(tmp,'.',sizeof tmp);
		for(int j=N-1;j>=0;j--)
			if(grid[j][i]!='.')
				tmp[sz++]=grid[j][i];
		for(int j=N-1,k=0;j>=0;j--,k++)
			grid[j][i]=tmp[k];
	}
}

bool search(char C)
{
	// horizontal
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(grid[i][j]==C)
			{
				int t=j;
				while(grid[i][j]==C) j++;
				if(j-t>=K)
				{
//					printf("Horizontal %c (%d,%d)\n",C,i,t);
					return true;
				}
				j=t;
			}
		}
	}

	// vertical
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(grid[i][j]==C)
			{
				int t=i;
				while(grid[i][j]==C) i++;
				if(i-t>=K)
				{
//					printf("vertical %c (%d,%d)\n",C,i,t);
					return true;
				}
				i=t;
			}
		}	
	}
	
	// diagonal
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(grid[i][j]==C)
			{
				int x=i,y=j;
				while(grid[i][j]==C)
				{
					i++;
					j++;
				}
				if(i-x>=K)
				{
//					printf("diag %c (%d,%d)\n",C,x,y);
					return true;
				}
				i=x;j=y;

				while(i>=0 && j>=0 && grid[i][j]==C)
				{
					i++;
					j--;
				}
				if(i-x>=K)
				{
//					printf("diag %c (%d,%d)\n",C,x,y);
					return true;
				}
				i=x;j=y;
			}
		}
	}		
	
	return false;
}

int main()
{
	int cases,iD=1;

	for(scanf("%d",&cases);cases--;)
	{
		read();
		rotate();
		gravity();
//		print();
		printf("Case #%d: ",iD++);
		bool blue=search('B');
		bool red=search('R');
//		printf("%d %d\n",blue,red);
		if(blue && red) puts("Both");
		else if(blue) puts("Blue");
		else if(red) puts("Red");
		else puts("Neither");
	}

	return 0;
}
