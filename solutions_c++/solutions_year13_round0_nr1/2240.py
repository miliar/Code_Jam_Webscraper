#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;
const long long million = 1000 * 1000;
const long long size_mas = 46;
int mas[million];
vector<vector<int> > v;
const string X_WIN = "X won";
const string O_WIN = "O won";
const string DRAW  =  "Draw";
const string GHNC  =  "Game has not completed";
string field[4];
bool find_won(char ch)
{
	int cnt;
	for (int i = 0; i < 4; i++)
	{
		cnt = 0;
		for (int j = 0; j < 4; j++)
		{
			if (field[i][j] == 'T' || field[i][j] == ch)
				cnt++;
		}
		if (cnt == 4)
			return true;
		cnt = 0;
		for (int j = 0; j < 4; j++)
		{
			if (field[j][i] == 'T' || field[j][i] == ch)
				cnt++;
		}
		if (cnt == 4)
			return true;
	}
	cnt = 0;
	for (int i = 0; i < 4; i++)
		if (field[i][i] == 'T' || field[i][i] == ch)
				cnt++;

	if (cnt == 4)
		return true;

	cnt = 0;
	for (int i = 0; i < 4; i++)
		if (field[i][3 - i] == 'T' || field[i][3 - i] == ch)
			cnt++;

	if (cnt == 4)
		return true;
	return false;
}
string solve()
{
	 for (int i = 0; i < 4; i++)
	 {
		 cin >> field[i];
	 }
	 if (find_won('X'))
		 return X_WIN;
	 if (find_won('O'))
		 return O_WIN;
	 for (int i = 0; i < 4; i++)
		 for (int j = 0; j < 4; j++)
			 if (field[i][j] == '.')
				 return GHNC;
	 return DRAW;
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int TEST_COUNT;
	cin >> TEST_COUNT;
	for (int t = 1;t <= TEST_COUNT; t++)
	{
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}