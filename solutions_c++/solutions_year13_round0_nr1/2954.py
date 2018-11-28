#include <cstdio>
#include <cstdlib>
#include <iostream>

#define forl(i,a,b) for(int i = a; i < b; ++i)

using namespace std;

char masks[][4][4] = {
	{
		{ '!', '.', '.', '.' },
		{ '!', '.', '.', '.' },
		{ '!', '.', '.', '.' },
		{ '!', '.', '.', '.' }
	},
	{
		{ '.', '!', '.', '.' },
		{ '.', '!', '.', '.' },
		{ '.', '!', '.', '.' },
		{ '.', '!', '.', '.' }
	},
	{
		{ '.', '.', '!', '.' },
		{ '.', '.', '!', '.' },
		{ '.', '.', '!', '.' },
		{ '.', '.', '!', '.' }
	},
	{
		{ '.', '.', '.', '!' },
		{ '.', '.', '.', '!' },
		{ '.', '.', '.', '!' },
		{ '.', '.', '.', '!' }
	},
	{
		{ '!', '!', '!', '!' },
		{ '.', '.', '.', '.' },
		{ '.', '.', '.', '.' },
		{ '.', '.', '.', '.' }
	},
	{
		{ '.', '.', '.', '.' },
		{ '!', '!', '!', '!' },
		{ '.', '.', '.', '.' },
		{ '.', '.', '.', '.' }
	},
	{
		{ '.', '.', '.', '.' },
		{ '.', '.', '.', '.' },
		{ '!', '!', '!', '!' },
		{ '.', '.', '.', '.' }
	},
	{
		{ '.', '.', '.', '.' },
		{ '.', '.', '.', '.' },
		{ '.', '.', '.', '.' },
		{ '!', '!', '!', '!' }
	},
	{
		{ '!', '.', '.', '.' },
		{ '.', '!', '.', '.' },
		{ '.', '.', '!', '.' },
		{ '.', '.', '.', '!' }
	},
	{
		{ '.', '.', '.', '!' },
		{ '.', '.', '!', '.' },
		{ '.', '!', '.', '.' },
		{ '!', '.', '.', '.' }
	}
};


int main(int argc, char **argv)
{
	int numGames = 0;
	cin >> numGames;
	forl(game,1,numGames+1)
	{
		char board[4][4];
		forl(y,0,4)
		{
			string s;
			cin >> s;
			forl(x,0,4)
			{
				board[x][y] = s[x];
			}
		}
		bool owon = false;
		bool xwon = false;

		forl(mask,0,10)
		{
			bool badx = false;
			bool bado = false;
			forl(y,0,4)
			{
				forl(x,0,4)
				{
					if (masks[mask][y][x] == '!')
					{
						//cerr << "Checking (" << x << ", " << y << "): \'" << masks[mask][y][x] << "\' vs \'" << board[x][y] << "\'\n";
						if (board[x][y] != 'X' && board[x][y] != 'T')
						{
							badx = true;
						}
						if (board[x][y] != 'O' && board[x][y] != 'T')
						{
							bado = true;
						}
					}

				}
			}
			if (!badx)
			{
				xwon = true;
				break;
			}
			if (!bado)
			{
				owon = true;
				break;
			}
		}
		cout << "Case #" << game << ": ";
		if (xwon)
		{
			cout << "X won" << endl;
			continue;
		}
		else if (owon)
		{
			cout << "O won" << endl;
			continue;
		}
		else
		{
			bool fullboard = true;
			forl(x,0,4)
			{
				forl(y,0,4)
				{
					if (board[x][y] == '.')
					{
						fullboard = false;
						break;
					}
				}
			}
			if (!fullboard)
			{
				cout << "Game has not completed" << endl;
			}
			else
			{
				cout << "Draw" << endl;
			}
		}
	}


}
