#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <set>
#include <vector>
using namespace std;
const long long MOD = 1000000007;
const int MAX = 700000;

string ans(int x)
{
	if (x == 1)
		return "Game has not completed";
	if (x == 2)
		return "Draw";
	if (x == 3)
		return "X won";
	if (x == 4)
		return "O won";
	throw 1;
}

string a[4];

bool FFull()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (a[i][j] == '.')
				return false;

	return true;
}

bool FWon(char c)
{
	for (int i = 0; i < 4; ++i)
	{
		bool fFail = false;
		for (int j = 0; j < 4; ++j)
			fFail = fFail || a[i][j] != c && a[i][j] != 'T';
		if (!fFail)
			return true;
	}
	for (int i = 0; i < 4; ++i)
	{
		bool fFail = false;
		for (int j = 0; j < 4; ++j)
			fFail = fFail || a[j][i] != c && a[j][i] != 'T';
		if (!fFail)
			return true;
	}
	bool fFail = false;
	for (int i = 0; i < 4; ++i)
		fFail = fFail || a[i][i] != c && a[i][i] != 'T';
	if (!fFail)
		return true;
	fFail = false;
	for (int i = 0; i < 4; ++i)
		fFail = fFail || a[3-i][i] != c && a[3-i][i] != 'T';
	
	if (!fFail)
		return true;

	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	
	for (int t = 0; t < tt; ++t)
	{
		int res = 0; // 1 - not compl; 2 - draw; 3- x; 4 - O

		
		for (int i = 0; i < 4; ++i)
			cin >> a[i];

		bool fwonx = FWon('X');
		bool fwony = FWon('O');

		if (fwonx)
			res = 3;
		if (fwony)
			res = 4;
		if (fwonx && fwony)
			throw 2;

		if (!fwonx && !fwony)
		{
			if (FFull())
				res = 2;
			else
				res = 1;
		}


		cout << "Case #"<< t+1 << ": " << ans(res) << endl;		
	}
	return 0;
}