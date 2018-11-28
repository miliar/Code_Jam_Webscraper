#include <iostream>

using namespace std;

char table[4][4], win;

bool valid(const int l, const int c, const char v)
{
	return table[l][c] == v || table[l][c] == 'T';
}

int main(int argc, char* argv[])
{
	int n;
	cin>>n;
	bool finished;
	for (int t = 1; t <= n; t++)
	{
		finished = true;
		cout<<"Case #"<<t<<": ";
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>table[i][j];
			}
			finished = finished && table[i][0] != '.' && table[i][1] != '.' && table[i][2] != '.' && table[i][3] != '.';
		}
		if ((valid(0, 0, 'X') && valid(0, 1, 'X') && valid(0, 2, 'X') && valid(0, 3, 'X')) || 
			(valid(1, 0, 'X') && valid(1, 1, 'X') && valid(1, 2, 'X') && valid(1, 3, 'X')) ||
			(valid(2, 0, 'X') && valid(2, 1, 'X') && valid(2, 2, 'X') && valid(2, 3, 'X')) ||
			(valid(3, 0, 'X') && valid(3, 1, 'X') && valid(3, 2, 'X') && valid(3, 3, 'X')) ||
		    (valid(0, 0, 'X') && valid(1, 0, 'X') && valid(2, 0, 'X') && valid(3, 0, 'X')) || 
			(valid(0, 1, 'X') && valid(1, 1, 'X') && valid(2, 1, 'X') && valid(3, 1, 'X')) ||
			(valid(0, 2, 'X') && valid(1, 2, 'X') && valid(2, 2, 'X') && valid(3, 2, 'X')) ||
			(valid(0, 3, 'X') && valid(1, 3, 'X') && valid(2, 3, 'X') && valid(3, 3, 'X')) ||
			(valid(0, 0, 'X') && valid(1, 1, 'X') && valid(2, 2, 'X') && valid(3, 3, 'X')) ||
			(valid(0, 3, 'X') && valid(1, 2, 'X') && valid(2, 1, 'X') && valid(3, 0, 'X')))
			cout<<"X won";
		else if ((valid(0, 0, 'O') && valid(0, 1, 'O') && valid(0, 2, 'O') && valid(0, 3, 'O')) || 
			(valid(1, 0, 'O') && valid(1, 1, 'O') && valid(1, 2, 'O') && valid(1, 3, 'O')) ||
			(valid(2, 0, 'O') && valid(2, 1, 'O') && valid(2, 2, 'O') && valid(2, 3, 'O')) ||
			(valid(3, 0, 'O') && valid(3, 1, 'O') && valid(3, 2, 'O') && valid(3, 3, 'O')) ||
		    (valid(0, 0, 'O') && valid(1, 0, 'O') && valid(2, 0, 'O') && valid(3, 0, 'O')) || 
			(valid(0, 1, 'O') && valid(1, 1, 'O') && valid(2, 1, 'O') && valid(3, 1, 'O')) ||
			(valid(0, 2, 'O') && valid(1, 2, 'O') && valid(2, 2, 'O') && valid(3, 2, 'O')) ||
			(valid(0, 3, 'O') && valid(1, 3, 'O') && valid(2, 3, 'O') && valid(3, 3, 'O')) ||
			(valid(0, 0, 'O') && valid(1, 1, 'O') && valid(2, 2, 'O') && valid(3, 3, 'O')) ||
			(valid(0, 3, 'O') && valid(1, 2, 'O') && valid(2, 1, 'O') && valid(3, 0, 'O')))
			cout<<"O won";
		else if (finished)
			cout<<"Draw";
		else
			cout<<"Game has not completed";
		cout<<endl;
	}
	return 0;
}

