#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>

using namespace std;

enum C
{
	O,
	X,
	T,
	Empty
};

enum S
{
	O_won,
	X_won,
	Draw,
	NotFinishedYet
};

C parse(char c)
{
	switch(c)
	{
		case 'O':
			return O;
		case 'X':
			return X;
		case 'T':
			return T;
		case '.':
			return Empty;
		default:
			throw exception();
	}
}

bool winning_line(C c, C line[])
{
	for(int j = 1; j < 4; ++j)
	{
		if(line[j] != c && line[j] != T)
			return false;
	}
	
	return true;
}

bool winning_column(C c, int j, C matrix[][4])
{
	for(int i = 1; i < 4; ++i)
	{
		if(matrix[i][j] != c && matrix[i][j] != T)
			return false;
	}

	return true;
}

bool winning_diagonal_00_33(C c, C matrix[][4])
{
	for(int i = 1; i < 4; ++i)
	{
		if(matrix[i][i] != c && matrix[i][i] != T)
			return false;
	}

	return true;
}


bool winning_diagonal_03_30(C c, C matrix[][4])
{
	for(int i = 1; i < 4; ++i)
	{
		if(matrix[i][3-i] != c && matrix[i][3-i] != T)
			return false;
	}
	
	return true;
}

S run_test(ifstream& is)
{
	C c[4][4];
	bool has_empty_cases = false;

	for(int i = 0; i < 4; ++i)
	{
		string line;
		while(line.length() != 4)
		getline(is, line);

		for(int j = 0; j < 4; ++j)
		{
			c[i][j] = parse(line[j]);
			if(c[i][j] == Empty)
				has_empty_cases = true;
		}
	}

	// check lines
	for(int i = 0; i < 4; ++i)
	{
		if(c[i][0] == Empty)
			continue;
		else if(c[i][0] == T)
		{
			if(c[i][1] == O && winning_line(O, c[i]))
				return O_won;
			else if(c[i][1] == X && winning_line(X, c[i]))
				return X_won;
		}
		else if(c[i][0] == O && winning_line(O, c[i]))
			return O_won;
		else if(c[i][0] == X && winning_line(X, c[i]))
			return X_won;
	}

	// check columns
	for(int j = 0; j < 4; ++j)
	{
		if(c[0][j] == Empty)
			continue;
		else if(c[O][j] == T)
		{
			if(c[1][j] == O && winning_column(O, j, c))
				return O_won;
			else if(c[1][j] == X && winning_column(X, j, c))
				return X_won;
		}
		else if(c[O][j] == O && winning_column(O, j, c))
			return O_won;
		else if(c[0][j] == X && winning_column(X, j, c))
			return X_won;
	}

	// check diagonal 00 -> 33
	if(c[0][0] == T)
	{
		if(c[1][1] == O && winning_diagonal_00_33(O, c))
			return O_won;
		else if(c[1][1] == X && winning_diagonal_00_33(X, c))
			return X_won;
	}
	else if(c[0][0] == O && winning_diagonal_00_33(O, c))
		return O_won;
	else if(c[0][0] == X && winning_diagonal_00_33(X, c))
		return X_won;

	// check diagonal 03 -> 30
	if(c[0][3] == T)
	{
		if(c[1][2] == O && winning_diagonal_03_30(O, c))
			return O_won;
		else if(c[1][2] == X && winning_diagonal_03_30(X, c))
			return X_won;
	}
	else if(c[0][3] == O && winning_diagonal_03_30(O, c))
		return O_won;
	else if(c[0][3] == X && winning_diagonal_03_30(X, c))
		return X_won;
	
	return has_empty_cases ? NotFinishedYet : Draw;
}
	
int main (int argc, char * const argv[])
{
	ifstream is("/Users/nathaniel/Dev/test.txt");
	
	string line;
	getline(is, line);
	istringstream iss(line);
	int n;
	iss >> n;
	
	for(int i = 0; i < n; ++i)
	{
		cout << "Case #" << (i + 1) << ": ";
		switch(run_test(is))
		{
			case O_won:
				cout << "O won";
				break;
			case X_won:
				cout << "X won";
				break;
			case Draw:
				cout << "Draw";
				break;
			case NotFinishedYet:
				cout << "Game has not completed";
				break;
		}
		cout << endl;
	}

	return 0;
}
