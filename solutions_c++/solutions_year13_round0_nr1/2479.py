#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <functional>
#include <algorithm>
using namespace std;

typedef long long ll;
#define MOD 1000000007

int main(void)
{
	std::ios_base::sync_with_stdio(false);
	fstream input("A-small-attempt0.in", fstream::in);
	fstream output("output.txt", fstream::out | fstream::trunc);

	string line, board[4];
	string::iterator itr;
	stringstream stream;

	int t, i, j, k, row[4], col[4], diag, diag2, dots, tx, ty;
	char ch;

	getline(input, line);
	stream << line;
	stream >> t;

	for(i=1; i<=t; ++i)
	{
		getline(input, board[0]);
		getline(input, board[1]);
		getline(input, board[2]);
		getline(input, board[3]);
		fill(col, col+4, 0);
		fill(row, row+4, 0);
		dots = 0;
		diag = 0;
		diag2 = 0;

		for(j=0; j<4; ++j)
		{
			for(k=0; k<4; ++k)
			{
				ch = board[j][k];
				if(ch == 'X'){
					++row[j];
					++col[k];
				}
				else if(ch == 'O'){
					--row[j];
					--col[k];
				}
				else if(ch == 'T'){
					tx = j;
					ty = k;
				}
				else
				{
					++dots;
				}
			}
		}
		for(j=0; j<4; ++j)
		{
			ch = board[j][j];
			if(ch == 'X'){
				++diag;
			}
			else if(ch == 'O'){
				--diag;
			}

			ch = board[j][3-j];
			if(ch == 'X'){
				++diag2;
			}
			else if(ch == 'O'){
				--diag2;
			}

		}

		++row[tx];
		++col[ty];
		if(tx == ty)
		{
			++diag;
		}
		if(tx ==  3-ty)
		{
			++diag2;
		}

		if(row[0] == 4 || row[1] == 4 || row[2] == 4 || row[3] == 4
			|| col[0] == 4 || col[1] == 4 || col[2] == 4 || col[3] == 4
			|| diag == 4 || diag2 == 4)
		{
			output << "Case #" << i << ": X won\n";
			getline(input, line);
			continue;
		}

		row[tx] -= 2;
		col[ty] -= 2;
		if(tx == ty)
		{
			diag -= 2;
		}
		if(tx ==  3-ty)
		{
			diag2 -= 2;
		}

		if(row[0] == -4 || row[1] == -4 || row[2] == -4 || row[3] == -4
			|| col[0] == -4 || col[1] == -4 || col[2] == -4 || col[3] == -4
			|| diag == -4 || diag2 == -4)
		{
			output << "Case #" << i << ": O won\n";
			getline(input, line);
			continue;
		}

		if(dots == 0)
		{
			output << "Case #" << i << ": Draw\n";
		}
		else
		{
			output << "Case #" << i << ": Game has not completed\n";
		}
		getline(input, line);
	}

	return 0;
}