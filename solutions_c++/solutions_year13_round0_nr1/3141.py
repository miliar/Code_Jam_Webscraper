#include <vector>
#include <iostream>
#include <string>

using namespace std;

bool isComparable(char a, char b)
{
	if (a=='.' || b=='.')
		return false;
	else if (b==a || b=='T')
		return true;
	return false;
}

bool checkWin(char a, vector <string> & s)
{
	bool isWin;
	for (int i=0; i<4; i++)
	{
		isWin = true;
		for (int j=0; j<4; j++)
			if (!isComparable(a, s[i][j]))
				isWin =false;
		if (isWin)
			return true;
	}
	
	for (int i=0; i<4; i++)
	{
		isWin = true;
		for (int j=0; j<4; j++)
			if (!isComparable(a, s[j][i]))
				isWin =false;
		if (isWin)
			return true;
	}
	
	isWin = true;
	for (int i=0; i<4; i++)
		if (!isComparable(a, s[i][i]))
			isWin = false;
	if (isWin)
		return true;
		
	isWin = true;
	for (int i=0; i<4; i++)
		if (!isComparable(a, s[i][3-i]))
			isWin = false;
	if (isWin)
		return true;
	
	return false;
}

bool checkComplete(vector <string> & s)
{
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			if (s[i][j]=='.')
				return false;
	return true;
}

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		vector <string> t(4);
		for (int j=0; j<4; j++)
		{
			cin >> t[j];
		}
		
		cout << "Case #" << i+1 << ": ";
		if(checkWin('O', t))
			cout << "O won" << endl;
		else if (checkWin('X', t))
			cout << "X won" << endl;
		else if (!checkComplete(t))
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
}
		
		