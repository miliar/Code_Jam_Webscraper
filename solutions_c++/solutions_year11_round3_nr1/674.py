#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(int argc, char** args)
{
	int T;
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << (t+1) << ":" << endl;
		
		int	R, C;
		cin >> R >> C;
		
		char*	grid = new char[R * C];
		
		for (int i = 0; i < R * C; i++) cin >> grid[i];
		
		bool	possible = true;
		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				if (grid[c + r * C] == '#')
				{
					if (r == R - 1) {possible = false; break;}
					if (c == C - 1) {possible = false; break;}
					
					for (int pr = 0; pr < 2; pr++)
						for (int pc = 0; pc < 2; pc++)
						{
							if (grid[c + pc + (r + pr) * C] != '#') possible = false;
							grid[c + pc + (r + pr) * C] = (pr == pc) ? '/' : '\\';
						}
						
					if (!possible) break;
				}
			}
			if (!possible) break;
		}
		
		if (!possible)
		{
			cout << "Impossible" << endl;
			continue;
		}
		
		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
				cout << grid[c + r * C];
				cout << endl;
		}
	}
}

