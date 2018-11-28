#include <iostream>

using namespace std;

char p[4][4];

bool row(int i, char c)
{
	for(int j=0;j<4;j++)
	{
		if (p[i][j] != c && p[i][j] !='T')
			return false;
	}
	return true;	
}


bool col(int j, char c)
{
	for(int i=0;i<4;i++)
	{
		if (p[i][j] != c && p[i][j] !='T')
			return false;
	}
	return true;	
}

bool diag1(char c)
{
	for(int i=0;i<4;i++)
	{
		if (p[i][i] != c && p[i][i] !='T')
			return false;
	}
	return true;	
}

bool diag2(char c)
{
	for(int i=0;i<4;i++)
	{
		if (p[i][4-1-i] != c && p[i][4-1-i] !='T')
			return false;
	}
	return true;	
}

bool win(char c)
{
		if (diag1(c) || diag2(c))
			return true;
		for(int i=0;i<4;i++)
		{
			if (row(i, c) || col (i,c))
			{
				return true;
			}
		}
		return false;
}


int main(int argc, char* argv[])
{

	int N;
	cin >> N;

	for (int c=0;c<N;c++)
	{
		int dots=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				char x;
				cin >> p[i][j];
				if (p[i][j]=='.')
					dots++;
			}
			char newl;
		}

		if (win('X'))
		{
			cout << "Case #" << c+1 << ": X won" << endl;
			goto solved;
		}
		if (win('O'))
		{
			cout << "Case #" << c+1 << ": O won" << endl;
			goto solved;
		}
		if (dots > 0)
		{
			cout << "Case #" << c+1 << ": Game has not completed" << endl;
			goto solved;			
		}
		cout << "Case #" << c+1 << ": Draw" << endl;
solved: ;
	}
	return 0;
}
