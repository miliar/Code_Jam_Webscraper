#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

using namespace std;

#define pb push_back
#define sz(x) ((int) (x).size())
#define forn(i, n) for (int i = 0; i < (n); i++)
#define rforn(i, n) for (int i = (n) - 1; i >= 0; i--)
#define clr(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef long long ll;
typedef pair<ll,ll> pll;

char tomek = 'T';

bool IsItVictory(char a, char b, char c, char d, char what)
{
	if ((a == what || a == tomek) &&
		(b == what || b == tomek) &&
		(c == what || c == tomek) &&
		(d == what || d == tomek))
		return true;
	else
		return false;
		
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	forn(casenum,T)
	{
		string answer = "";
		
		string table[4];
		for (int i = 0; i < 4; ++i)
		{
			cin >> table[i];
		}

		for (int i = 0; i < 4 && answer.empty(); ++i)
		{
			if (IsItVictory(table[i][0],table[i][1],table[i][2],table[i][3],'O'))
				answer = "O won";
			if (IsItVictory(table[i][0],table[i][1],table[i][2],table[i][3],'X'))
				answer = "X won";
			if (IsItVictory(table[0][i],table[1][i],table[2][i],table[3][i],'O'))
				answer = "O won";
			if (IsItVictory(table[0][i],table[1][i],table[2][i],table[3][i],'X'))
				answer = "X won";
		}

		if (answer.empty())
		{
			if (IsItVictory(table[0][0],table[1][1],table[2][2],table[3][3],'O'))
				answer = "O won";
			else if (IsItVictory(table[0][0],table[1][1],table[2][2],table[3][3],'X'))
				answer = "X won";
			else if (IsItVictory(table[0][3],table[1][2],table[2][1],table[3][0],'O'))
				answer = "O won";
			else if (IsItVictory(table[0][3],table[1][2],table[2][1],table[3][0],'X'))
				answer = "X won";
		}

		if (answer.empty())
		{
			forn(i,4)
			{
				forn(j,4)
				{
					if (table[i][j] == '.')
					{
						answer = "Game has not completed";
					}
				}
			}
		}

		if (answer.empty())
		{
			answer = "Draw";
		}

		cout << "Case #" << casenum + 1 << ": "<< answer << endl;
	}

	return 0;
}