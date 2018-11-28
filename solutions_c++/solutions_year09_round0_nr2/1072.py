#include <iostream>
#include <string>
#include <cassert>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <algorithm>
#include <fstream>
#include <cmath>
using namespace std;

int T;
int H, W;
int altitudes[101][101];
char label[101][101];
int parent[10001];
queue<int> children[10001];

//获取关系图，建立树结构
void getRelate()
{
	memset( parent, -1, sizeof(parent) );
	for ( int i = 0; i < H; i++ )
	{
		for ( int j = 0; j < W; j++ )
		{
			int alti = altitudes[i][j];
			pair<int, int> temp;
			if( i > 0 && altitudes[i-1][j] < alti )
			{
				alti = altitudes[i-1][j];
				temp.first = i-1;
				temp.second = j;
			}
			if ( j > 0 && altitudes[i][j-1] < alti)
			{
				alti = altitudes[i][j-1];
				temp.first = i;
				temp.second = j-1;
			}
			if ( j < W-1 && altitudes[i][j+1] < alti )
			{
				alti = altitudes[i][j+1];
				temp.first = i;
				temp.second = j+1;
			}
			if ( i < H-1 && altitudes[i+1][j] < alti )
			{
				alti = altitudes[i+1][j];
				temp.first = i+1;
				temp.second = j;
			}
			int from = i * W + j;
			int to = temp.first * W + temp.second;
			if( alti != altitudes[i][j] )
			{
				parent[from] = to;
				children[to].push(from);
			}
		}
	}
}

//标记一个cell
void labelACell( int point, char lab)
{
	label[point/W][point%W] = lab;
}

//标记一个Basin
void labelABasin( int start, char lab )
{
	while ( parent[start] != -1 )
	{
		start = parent[start];
	}
	queue<int> help;
	help.push(start);
	while ( !help.empty() )
	{
		int temp = help.front();
		help.pop();
		while( !children[temp].empty() )
		{
			help.push(children[temp].front());
			children[temp].pop();
		}
		labelACell( temp, lab );
	}
}

void doLabel()
{
	memset( label, 0, sizeof(label) );
	char lab = 'a';
	for ( int i = 0; i < H; i++ )
	{
		for ( int j = 0; j < W; j++ )
		{
			if( label[i][j] != 0 )continue;
			labelABasin( i*W+j, lab );
			lab += 1;
		}
	}

}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	fin >> T;
	for ( int i = 1; i <= T; i++ )
	{
		fin >> H >> W;
		for ( int l = 0; l < H; l++ )
		{
			for ( int c = 0; c < W; c++ )
			{
				fin >> altitudes[l][c];
			}
		}
		getRelate();
		doLabel();
		fout << "Case #" << i << ": " << endl;
		for ( int l = 0; l < H; l++ )
		{
			for ( int c = 0; c < W; c++ )
			{
				fout << label[l][c] << " ";
			}
			fout << endl;
		}
	}		

	return 0;
}
