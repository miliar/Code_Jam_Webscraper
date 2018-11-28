#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;
vector <vector <int> > grid, old;
int main()
{
	int T;
	FILE *in=fopen("bactin.txt", "r");
	FILE *out=fopen("bactout.txt", "w");
	fscanf(in, "%d", &T);
	for(int t=0; t<T; t++)
	{
		int n=0;
		grid.resize(0);
		int r;
		fscanf(in, "%d", &r);
		grid.resize(102);
		for(int i=0; i<102; i++)
			grid[i].resize(102, 0);
		for(int i=0; i<101; i++)
			for(int j=0; j<101; j++)
				grid[i][j]=0;	//Just to be certain
		int X1, Y1, X2, Y2;
		for(int i=0; i<r; i++)
		{
			fscanf(in, "%d%d%d%d", &X1, &Y1, &X2, &Y2);
			for(int j=X1; j<=X2; j++)
				for(int k=Y1; k<=Y2; k++)
					grid[j][k]=1;
		}
		bool tf=false;
		while(!tf)
		{
			n++;
			old=grid;
			tf=true;
			for(int i=0; i<101; i++)
			{
				for(int j=0; j<101; j++)
				{
					if((i==0 || old[i-1][j]==0) && (j==0 || old[i][j-1]==0))
						grid[i][j]=0;
					if((i!=0 && old[i-1][j]==1) && (j!=0 && old[i][j-1]==1))
						grid[i][j]=1;
				}
			}
			for(int i=0; i<101; i++)
				for(int j=0; j<101; j++)
					if(grid[i][j]==1)
						tf=false;
		}
		fprintf(out, "Case #%d: %d\n", t+1, n);
	}
	
	return 0;
}
