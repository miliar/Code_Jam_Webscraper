//Watersheds

#include <iostream> 
#include <cmath> 
#include <vector> 
#include <string> 
#include <map> 
#include <iomanip>

using namespace std;

int north = 1;
int west = 2;
int east = 3;
int south = 4;

int matrix[110][110];
char labels[110][110];
int H,W;
char start = 'a';

void DFS(int i, int j)
{
	int h = matrix[i][j];
	int min = 100000;
	int direc = 0;
	int x,y;
	if(labels[i][j] != ' ') return;
	
	
	x = 0; y = 0;
	if(i > 0 && h > matrix[i-1][j] && matrix[i-1][j] < min)
	{
		x = 0; y = 0;
		direc = north;
		min = matrix[i-1][j];
		x--;
	}
	if(j > 0 && h > matrix[i][j-1] && matrix[i][j-1] < min)
	{
		x = 0; y = 0;
		direc = east;
		min = matrix[i][j-1];
		y--;
	}
	if(j < W - 1 && h > matrix[i][j+1] && matrix[i][j+1] < min)
	{
		x = 0; y = 0;
		direc = west;
		min = matrix[i][j+1];
		y++;
	}
	if(i < H - 1 && h > matrix[i+1][j] && matrix[i+1][j] < min)
	{
		x = 0; y = 0;
		direc = south;
		min = matrix[i+1][j];
		x++;
	}
	
	
	
	if(x == 0 && y == 0)
	{
		labels[i][j] = start;
		start++;
	}
	else
	{
		DFS(i + x, j + y);
		labels[i][j] = labels[i+x][j+y];
	}
	
	//labels[i][j] = labels[i+x][j+y];
	return;
}

int main()
{
	int nCases;
	cin>>nCases;
	
	for(int i = 0; i < nCases; i++)
	{
		cin>>H>>W;
		memset(labels, ' ', sizeof(labels));
		start = 'a';
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				cin>>matrix[j][k];
			}	
		}
		cout<<"Case #"<<i+1<<":"<<endl;
		
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				DFS(j,k);
				cout<<labels[j][k];
				if(k < W - 1) cout<<" ";
			}
			cout<<endl;
		}
	}	
}
