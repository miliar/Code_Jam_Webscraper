#include <fstream>
#include <iostream>

using namespace std;


char board[4][4];

bool check(char ch)
{
	//check rows
	int i, j;
	bool hasT, pass;
	int cnt;
	
	for(i = 0; i < 4; i ++)
	{
		hasT = false;
		cnt = 0;
		pass = false;
		for(j = 0; j < 4; j ++)
		{
			if(board[i][j] == ch)
				cnt ++;
			else if(board[i][j] == 'T')
				hasT = true;
			else
			{
				pass = true;
				break;
			}	
		}
		
		if(!pass)
		{
			if(cnt == 4 || (cnt == 3 && hasT))
				return true;
		}
	}
	
	// check columns
	for(i = 0; i < 4; i ++)
	{
		hasT = false;
		cnt = 0;
		pass = false;
		for(j = 0; j < 4; j ++)
		{
			if(board[j][i] == ch)
				cnt ++;
			else if(board[j][i] == 'T')
				hasT = true;
			else
			{
				pass = true;
				break;
			}	
		}
		
		if(!pass)
		{
			if(cnt == 4 || (cnt == 3 && hasT))
				return true;
		}
	}

	// check diagonal1
	hasT = false;
	cnt = 0;
	pass = false;
	
	for(j = 0; j < 4; j ++)
	{
		if(board[j][j] == ch)
			cnt ++;
		else if(board[j][j] == 'T')
			hasT = true;
		else
		{
			pass = true;
			break;	
		}
	}
	
	if(!pass)
	{
		if(cnt == 4 || (cnt == 3 && hasT))
				return true;
	}
	
	// check diagonal2
	hasT = false;
	cnt = 0;
	pass = false;
	
	for(j = 0; j < 4; j ++)
	{
		if(board[j][3 - j] == ch)
			cnt ++;
		else if(board[j][3 - j] == 'T')
			hasT = true;
		else
		{
			pass = true;
			break;	
		}
	}
	
	if(!pass)
	{
		if(cnt == 4 || (cnt == 3 && hasT))
				return true;
	}
	
	return false;

}

bool checkFinish()
{
	int i, j;
	
	for(i = 0; i < 4; i ++)
	{
		for(j = 0; j < 4; j ++)
		{
			if(board[i][j] == '.')
				return false;
		}
	}
	
	return true;
}

void solve(int game)
{
	if(check('X'))
	{
		cout <<"Case #" << game << ": X won" << endl;
		return;
	}
	
	if(check('O'))
	{
		cout <<"Case #" << game << ": O won" << endl;
		return;
	}
	
	if(!checkFinish())
	{
		cout <<"Case #" << game << ": Game has not completed" << endl;
		return;
	}
	
	cout <<"Case #" << game << ": Draw" << endl;
}

int main()
{
	ifstream fin;
	
	fin.open("small.in");
	
	int n, i, j, k;
	char ch;
	
	fin >> n;
	
	for(i = 0; i < n ; i ++)
	{
		for(j = 0; j < 4; j ++)
		{
			for(k = 0; k < 4; k ++)
			{
				fin >> board[j][k];
				
				//cout << board[j][k] << " ";
			}
			//cout << endl;
		}
		solve(i + 1);
		//cout << endl;
	}
	
	
	
	
	fin.close();
	
	
}
