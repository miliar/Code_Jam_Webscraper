#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define PII pair<int, int>
#define X first
#define Y second

int aabs(int a) { return (a<0)?-a:a; }
int mmax(int a, int b) { return (a>b)?a:b; }
int mmin(int a, int b) { return (a<b)?a:b; }

int main(void)
{
	int T;
	string board[4];
	cin >> T;
	for (int caso=0; caso<T; caso++)
	{
		for (int i = 0; i < 4; ++i)
		{
			cin >> board[i];
		}

		int o=0, x=0, p=0, t=0;
		string win="";
		for (int i = 0; i < 4; ++i)
		{
			// test ith row
			o=0, x=0, t=0;
			for (int j = 0; j < 4; ++j)
			{
				if (board[i][j] == 'O') o++;
				else if (board[i][j] == 'X') x++;
				else if (board[i][j] == 'T') t++;
				else p++;
			}
			if (o+t == 4) {
				win = "O";
				break;
			} else if (x+t == 4) {
				win = "X";
				break;
			}

			// test ith column
			o=0, x=0, t=0;
			for (int j = 0; j < 4; ++j)
			{
				if (board[j][i] == 'O') o++;
				else if (board[j][i] == 'X') x++;
				else if (board[j][i] == 'T') t++;
			}
			if (o+t == 4) {
				win = "O";
				break;
			} else if (x+t == 4) {
				win = "X";
				break;
			}
		}

		if(win == "") {
			o=0, x=0, t=0;
			for (int i = 0; i < 4; ++i)
			{
				if (board[i][i] == 'O') o++;
				else if (board[i][i] == 'X') x++;
				else if (board[i][i] == 'T') t++;
			}
			if (o+t == 4) {
				win = "O";
			} else if (x+t == 4) {
				win = "X";
			}
		}

		if(win == "") {
			o=0, x=0, t=0;
			for (int i = 0; i < 4; ++i)
			{
				if (board[3-i][i] == 'O') o++;
				else if (board[3-i][i] == 'X') x++;
				else if (board[3-i][i] == 'T') t++;
			}
			if (o+t == 4) {
				win = "O";
			} else if (x+t == 4) {
				win = "X";
			}
		}

		cout << "Case #" << caso+1 << ": ";
		if(win == "O") cout << "O won";
		else if(win == "X") cout << "X won";
		else if(win == "" and p > 0) cout << "Game has not completed";
		else cout << "Draw";
		cout << endl;
	}


	return 0;
}