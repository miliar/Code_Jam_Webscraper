#include<fstream>
#include<iostream>
#include<cmath>
#include<limits>
#include<vector>
#include<algorithm>
#include<deque>
#include<list>
using namespace std;

ifstream lettura ("input.txt");
ofstream scrittura ("output.txt");

long t, n, m;

vector< vector<bool> > board;
vector< vector<bool> > removed;
vector< vector<bool> > valid;
vector< pair<int,int> > found;

void leggi ()
{
	lettura >> m >> n;
	board.assign (m, vector<bool> (n, false));
	removed.assign (m, vector<bool> (n, false));
	
	char a;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n/4; j++)
		{
			lettura >> a;
			if (a == '1')
			{
				board[i][4*j+3] = true;
			}
			else if (a == '2')
			{
				board[i][4*j+2] = true;
			}
			else if (a == '3')
			{
				board[i][4*j+2] = true;
				board[i][4*j+3] = true;
			}
			else if (a == '4')
			{
				board[i][4*j+1] = true;
			}
			else if (a == '5')
			{
				board[i][4*j+1] = true;
				board[i][4*j+3] = true;
			}
			else if (a == '6')
			{
				board[i][4*j+1] = true;
				board[i][4*j+2] = true;
			}
			else if (a == '7')
			{
				board[i][4*j+1] = true;
				board[i][4*j+2] = true;
				board[i][4*j+3] = true;
			}
			else if (a == '8')
			{
				board[i][4*j] = true;
			}
			else if (a == '9')
			{
				board[i][4*j] = true;
				board[i][4*j+3] = true;
			}
			else if (a == 'A')
			{
				board[i][4*j] = true;
				board[i][4*j+2] = true;
			}
			else if (a == 'B')
			{
				board[i][4*j] = true;
				board[i][4*j+2] = true;
				board[i][4*j+3] = true;
			}
			else if (a == 'C')
			{
				board[i][4*j] = true;
				board[i][4*j+1] = true;
			}
			else if (a == 'D')
			{
				board[i][4*j] = true;
				board[i][4*j+1] = true;
				board[i][4*j+3] = true;
			}
			else if (a == 'E')
			{
				board[i][4*j] = true;
				board[i][4*j+1] = true;
				board[i][4*j+2] = true;
			}
			else if (a == 'F')
			{
				board[i][4*j] = true;
				board[i][4*j+1] = true;
				board[i][4*j+2] = true;
				board[i][4*j+3] = true;
			}
		}
	}
}

void debug ()
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (board[i][j])
				cout << "1";
			else
				cout << "0";
		}
		cout << endl;
	}
}

void slide (int row, int size)
{
	int seq = !removed[row][0] ? 1 : 0;
	for (int i = 1; i < n; i++)
	{
		if (board[row][i] != board[row][i-1] && !removed[row][i])
			seq ++;
		else
			seq = !removed[row][i] ? 1 : 0;
		if (seq == size)
		{
			valid[row][i-size+1] = true;
			seq --;
		}
	}
}

void combine (int column, int size)
{
	int seq = valid[0][column] && !removed[0][column] ? 1 : 0;
	for (int i = 1; i < m; i++)
	{
		if (board[i][column] != board[i-1][column] && valid[i][column] && !removed[i][column])
			seq ++;
		else
			seq = valid[i][column] && !removed[i][column] ? 1 : 0;
		if (seq == size)
		{
			found.push_back (make_pair (i-size+1, column));
			seq --;
		}
	}
}

void rimuovi (int x, int y, int size)
{
	for (int i = y; i < y + size; i++)
	{
		for (int j = x; j < x + size; j++)
		{
			removed[i][j] = true;
		}
	}
}

void debugr ()
{
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (removed[i][j])
				cout << "1";
			else
				cout << "0";
		}
		cout << endl;
	}
}

vector<int> total;

int elabora (int caso)
{
	int rimangono = m*n;
	total.assign (min(n, m)+1, 0);
	
	for (int i = min(n, m); i > 1; i--)
	{
//		cout << "+++ provo con " << i << endl;
		valid.assign (m, vector<bool> (n, false));
		found.clear ();
		
		for (int j = 0; j < m; j++)
			slide (j, i);
		for (int j = 0; j < n; j++)
			combine (j, i);
		
		if (found.size () > 0)
		{
			sort (found.begin(), found.end());
			
//			cout << " +  trovato con " << i << " in " << found[0].first << " " << found[0].second << endl;
			
			rimuovi (found[0].second, found[0].first, i);
//			debugr();
			
			total[i]++;
			rimangono -= i*i;
		
			if (found.size() > 1)
				i++;
		}
	}
	total[1] = rimangono;
	
	int totale = 0;
	for (int i = min(n, m); i > 0; i--)
	{
		if (total[i] > 0)
			totale ++;
	}
	
	scrittura << "Case #" << caso << ": " << totale << endl;
	for (int i = min(n, m); i > 0; i--)
	{
		if (total[i] > 0)
			scrittura << i << " " << total[i] << endl;
	}
}

int main ()
{
	lettura >> t;
	for (int i = 0; i < t; i++)
	{
		leggi ();
//		debug ();
		elabora (i+1);
	}
}
