#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

string game[4];

char checkRow(int i)
{
	bool Xwon = true;
	bool Owon = true;
	for(int j = 0; j < 4; j++)
	{
		if(game[i][j] != 'X' && game[i][j] != 'T')
		{
			Xwon = false;
		}
		if(game[i][j] != 'O' && game[i][j] != 'T')
		{
			Owon = false;
		}
	}

	if(Xwon)
	{
		return 'X';
	}
	else if(Owon)
	{
		return 'O';
	}
	else
	{
		return 'N';
	}
}

char checkCol(int i)
{
	bool Xwon = true;
	bool Owon = true;
	for(int j = 0; j < 4; j++)
	{
		if(game[j][i] != 'X' && game[j][i] != 'T')
		{
			Xwon = false;
		}
		if(game[j][i] != 'O' && game[j][i] != 'T')
		{
			Owon = false;
		}
	}

	if(Xwon)
	{
		return 'X';
	}
	else if(Owon)
	{
		return 'O';
	}
	else
	{
		return 'N';
	}
}

char checkDiagonal()
{
	bool Xwon = true;
	bool Owon = true;
	for(int j = 0; j < 4; j++)
	{
		if(game[j][j] != 'X' && game[j][j] != 'T')
		{
			Xwon = false;
		}
		if(game[j][j] != 'O' && game[j][j] != 'T')
		{
			Owon = false;
		}
	}

	if(Xwon)
	{
		return 'X';
	}
	else if(Owon)
	{
		return 'O';
	}

	Xwon = true;
	Owon = true;
	for(int j = 0; j < 4; j++)
	{
		if(game[j][3-j] != 'X' && game[j][3-j] != 'T')
		{
			Xwon = false;
		}
		if(game[j][3-j] != 'O' && game[j][3-j] != 'T')
		{
			Owon = false;
		}
	}

	if(Xwon)
	{
		return 'X';
	}
	else if(Owon)
	{
		return 'O';
	}
	else
	{
		return 'N';
	}
	
}

bool isIncomplete()
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(game[i][j] == '.')
			{
				return true;
			}
		}
	}
	return false;
}


void eval(){
    for(int i=0; i<4; i++)
    {
        cin>>game[i];
    }
	
	// Check Rows
	for(int i = 0; i < 4; i++)
	{
		char temp = checkRow(i);
		if(temp == 'X')
		{
			cout<<"X won"<<endl;
			return;
		}
		if(temp == 'O')
		{
			cout<<"O won"<<endl;
			return;
		}	
	}
	
	// Check Cols
	for(int i = 0; i < 4; i++)
	{
		char temp = checkCol(i);
		if(temp == 'X')
		{
			cout<<"X won"<<endl;
			return;
		}
		if(temp == 'O')
		{
			cout<<"O won"<<endl;
			return;
		}	
	}
	
	char temp = checkDiagonal();
	if(temp == 'X')
	{
		cout<<"X won"<<endl;
		return;
	}
	if(temp == 'O')
	{
		cout<<"O won"<<endl;
		return;
	}		
	if(isIncomplete())
	{
		cout<<"Game has not completed"<<endl;	
	}
	else
	{
		cout<<"Draw"<<endl;
	}

}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
