#include <stdio.h> 
#include <vector> 
#include <list>
#include <string>
#include <set>
#include <algorithm> 
#include <fstream> 
#include <iostream> 
using namespace std; 
int main() 
{ 
	int T;
	cin >> T;
	
	for (int test = 1; test <= T; ++test)
	{
		int n, btime=0, otime = 0;
		int BluePos = 1;
		int OrangePos = 1;
		int R, C;
		cin >> R >> C;
		string grid[60];
		for (int i = 0; i < R; ++i)
		{
			cin >> grid[i];
		}
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j)
			{
				if (grid[i][j] == '#')
				{
					if (i!=R-1 && j!= C-1 && grid[i+1][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j+1] == '#')
					{
						grid[i+1][j+1] = grid[i][j] = '/'; grid[i+1][j] = '\\';	grid[i][j+1]='\\';
					}
					else
					{
						goto nope;
					}
				}
			}

	   	cout << "Case #" << test << ":\n";
		for (int i = 0; i < R; ++i)
		{
			cout << grid[i] << "\n";
		}
		continue;
	nope:
		cout << "Case #" << test << ":\n" << "Impossible" << "\n";
	}
#ifndef ONLINE_JUDGE
#ifndef FULLREDIRECT
	ifstream console("CONIN$");
	char fdasfadsfdasfdsa;
	console.getline(&fdasfadsfdasfdsa,1);
	console.close();
#endif
#endif
	return 0; 
}