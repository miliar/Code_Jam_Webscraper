#include <iostream>
#include <string>

using namespace std;

bool check(char c, string* s)
{
	bool win = false;
	for(int i = 0; i < 4; i++)
	{
		bool winG = true, winV = true;
		for(int j = 0; j < 4; j++)
		{
			winG &= s[i][j] == c || s[i][j] == 'T';
			winV &= s[j][i] == c || s[i][j] == 'T';
		}
		win |= winG || winV;
	}
	bool winD = true;
	bool winP = true;
	for(int i = 0; i < 4; i++)
	{
		winD &= s[i][i] == c || s[i][i] == 'T';
		winP &= s[i][3 - i] == c || s[i][3 - i] == 'T';
	}
	win |= winD || winP;
	return win;
}

bool ended(string* s)
{
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(s[i][j] == '.')
				return false;
	return true;
}



int main()
{
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tcase = 1; tcase <= t; tcase++)
	{
		string* s = new string[4];
		for(int i = 0; i < 4; i++)
			cin >> s[i];
		cout << "Case #" << tcase << ": ";
		if(check('X', s))
		{
			cout << "X won" << endl;
			continue;
		}
		if(check('O', s))
		{
			cout << "O won" << endl;
			continue;
		}
		if(ended(s))
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;

	}

	return 0;
}