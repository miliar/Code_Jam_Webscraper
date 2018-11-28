#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctype.h>
#include <bitset>

using namespace std;

bool doForOne(vector<string> &Maze)
{
	for(int i=0;i<Maze.size();i++)
	{
		for(int j=0;j<Maze[i].size();j++)
		{
			if(Maze[i][j]=='#')
			{
				if(i>=Maze.size()-1 || j>=Maze[i].size()-1)
					return false;
				if(Maze[i+1][j]!='#' || Maze[i][j+1]!='#' || Maze[i+1][j+1]!='#')
					return false;
				Maze[i][j] = '/';
				Maze[i+1][j] = '\\';
				Maze[i][j+1] = '\\';
				Maze[i+1][j+1] = '/';
			}
		}
	}
	return true;
}
int main()
{
	freopen("A-large.in","r",stdin);
	
	int T;
	cin>>T;
	int R,C;
	for(int i=1;i<=T;i++)
	{
		int N;vector<int> X;
		cin>>R>>C;
		vector<string> Maze;

		for(int j=0;j<R;j++)
		{
			string temp;
			cin>>temp;
			Maze.push_back(temp);
		}
		bool val = doForOne(Maze);
		printf("Case #%d:\n",i);
		if(val==false)
			printf("Impossible\n");
		else
			for(int i=0;i<Maze.size();i++)
			{
				cout<<Maze[i];
				if(i!=Maze.size()-1)
					cout<<endl;
			}
		if(i!=T)
			printf("\n");
	}
	return 0;
}
