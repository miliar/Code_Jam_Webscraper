#include <iostream>
#include <fstream>

using namespace std;



ifstream in;
ofstream out;
int R,C;
string g[51];

void pr();
bool work();
bool dfs(int r, int c);
int main()
{
	int t;
	in.open("small.in");
	out.open("small.out");
	in>>t;
	for (int i = 0; i < t; i++)
	{
		in>>R>>C;
		for (int j = 0; j < R; j++)
		{
			string tmp;
			in>>tmp;
			g[j] = tmp;
		}
		out<<"Case #"<<i + 1<<":"<<endl;
		if (work())
		{
			for (int j = 0; j < R; j++)
				out<<g[j]<<endl;			
		}
		else
			out<<"Impossible"<<endl;

	}
	return 0;
}
bool dfs(int r, int c)
{
	if (r + 1 >= R) return false;
	if (c + 1 >= C) return false;
	if (g[r][c] != '#' || g[r+1][c] != '#' 
			|| g[r][c+1] != '#' || g[r+1][c+1] != '#')
		return false;
	g[r][c] = '/';
	g[r + 1][c + 1] = '/';
	g[r + 1][c] = '\\';
	g[r][c + 1] = '\\';
	return true;
}
bool work()
{
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (g[i][j] == '#')
				if (!dfs(i, j))
					return false;
		}
	}
	return true;
}
void pr()
{
	cout<<R<<endl;
	for (int i = 0; i < R; i++)
		cout<<g[i]<<endl;
	cout<<endl;
}
