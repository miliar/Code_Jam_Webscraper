#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <deque>
#include <utility>
#include <sstream>

#define clear(a) memset(a, 0, sizeof(a))
#define initNeg(a) memset(a, -1, sizeof(a))
#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<=int(b); i++)
#define REP(i, b) for(int i=0; i<=int(b); i++)
#define p2(b) (1 << (b))

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

template <typename T> string toString(T n){ostringstream ss; ss << n; return ss.str();}
template <typename T> T toNum(const string &Text){istringstream ss(Text); T result; return ss >> result ? result : 0;}

int main()
{
	//freopen("input.txt", "r", stdin);

	int T;
	cin >> T;
	for(int tc = 1; tc <= T; tc++)
	{
		string game[4];
		REP(i, 3)
		{
			cin >> game[i];
		}

		cout << "Case #" << tc << ": ";

		bool containsPoint = false;
		bool foundWinner = false;
		FOR(i, 0, 3)
		{
			bool allXROW = true, allXCOL = true;
			bool allOROW = true, allOCOL = true;
			FOR(j, 0, 3)
			{
				if(game[i][j] != 'T')
				{
					if(game[i][j] != 'X')
						allXROW &= false;
					if(game[i][j] != 'O')
						allOROW &= false;
				}

				if(game[j][i] != 'T')
				{
					if(game[j][i] != 'X')
						allXCOL &= false;
					if(game[j][i] != 'O')
						allOCOL &= false;
				}

				if(game[i][j] == '.')
					containsPoint |= true;
			}

			if(!foundWinner)
			{
				if(allXROW || allXCOL)
				{
					foundWinner = 1;
					cout << "X won" << endl;
				}if(allOROW || allOCOL)
				{
					foundWinner = 1;
					cout << "O won" << endl;
				}
			}
		}

		if(!foundWinner && (game[0][0] == 'O' || game[0][0] == 'T') && (game[1][1] == 'O' || game[1][1] == 'T') && (game[2][2] == 'O' || game[2][2] == 'T') && (game[3][3] == 'O' || game[3][3] == 'T'))
		{
			foundWinner = true;
			cout << "O won" << endl;
		}

		if(!foundWinner && (game[0][0] == 'X' || game[0][0] == 'T') && (game[1][1] == 'X' || game[1][1] == 'T') && (game[2][2] == 'X' || game[2][2] == 'T') && (game[3][3] == 'X' || game[3][3] == 'T'))
		{
			foundWinner = true;
			cout << "X won" << endl;
		}

		if(!foundWinner && (game[0][3] == 'O' || game[0][3] == 'T') && (game[1][2] == 'O' || game[1][2] == 'T') && (game[2][1] == 'O' || game[2][1] == 'T') && (game[3][0] == 'O' || game[3][0] == 'T'))
		{
			foundWinner = true;
			cout << "O won" << endl;
		}

		if(!foundWinner && (game[0][3] == 'X' || game[0][3] == 'T') && (game[1][2] == 'X' || game[1][2] == 'T') && (game[2][1] == 'X' || game[2][1] == 'T') && (game[3][0] == 'X' || game[3][0] == 'T'))
		{
			foundWinner = true;
			cout << "X won" << endl;
		}

		if(!foundWinner)
		{
			if(containsPoint)
				cout << "Game has not completed" << endl;
			else
				cout << "Draw" << endl;
		}

		

	}

}