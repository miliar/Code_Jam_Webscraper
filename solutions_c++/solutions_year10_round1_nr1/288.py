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
char grid[52][52], gr[52][52];
int len[52];
int main()
{
	FILE *in=fopen("rotin.txt", "r");
	FILE *out=fopen("rotout.txt", "w");
	int T;
	fscanf(in, "%d", &T);
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<52; i++)
			for(int j=0; j<52; j++)
				gr[i][j]='.';
		int N, K;
		bool red=false, blue=false;
		char rem;
		fscanf(in, "%d%d%c", &N, &K, &rem);
		for(int i=0; i<52; i++)
			len[i]=N-1;
		for(int i=0; i<N; i++)	//i is vertical
		{
			for(int j=0; j<N; j++)
			{
				fscanf(in, "%c", &grid[i][j]);
			}
			
			fscanf(in, "%c", &rem);
		}
		for(int i=0; i<N; i++)	//i is vertical
		{
			for(int j=N-1; j>=0; j--)
			{
				if(grid[i][j]!='.')
				{
					gr[i][len[i]]=grid[i][j];
					len[i]--;
				}
			}
		}	//the grid gr now holds the rotated result, albeit in original position
		fprintf(out, "Case #%d: ", t+1);
		for(int i=0; i<52; i++)
			for(int j=0; j<52; j++)
			{
				bool is=true;
				for(int k=0; k<K; k++)
					if(i+k>=52 || gr[i+k][j]!=gr[i][j])
						is=false;
				bool ist=true;
				for(int k=0; k<K; k++)
					if(j+k>=52 || gr[i][j+k]!=gr[i][j])
						ist=false;
				if(ist==true)
					is=true;
				ist=true;
				for(int k=0; k<K; k++)
					if(j+k>=52 || i+k>=52 || gr[i+k][j+k]!=gr[i][j])
						ist=false;
				if(ist==true)
					is=true;
				ist=true;
				for(int k=0; k<K; k++)
					if(j+k>=52 || i-k<0 || gr[i-k][j+k]!=gr[i][j])
						ist=false;
				if(ist==true)
					is=true;
				if(is)
				{
					if(gr[i][j]=='R')
						red=true;
					else if(gr[i][j]=='B')
						blue=true;
				}
			}
		
		if(red&&blue)
			fprintf(out, "Both\n");
		else if(red)
			fprintf(out, "Red\n");
		else if(blue)
			fprintf(out, "Blue\n");
		else
			fprintf(out, "Neither\n");
	}
	return 0;
}
