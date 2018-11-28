#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>

using namespace std;

#define REP(i, n) for(int i = 0; i < n; ++i)

int conv(char c)
{
	if(c == 'O') return 0;
	if(c == 'X') return 1;
	if(c == '.') return 2;
	return 3;
}

int main()
{
	int n;
	cin >> n;
	for(int in = 1; in <= n; ++in)
	{
		char a[4][4];
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> a[i][j];

		int row[4][4];
		int col[4][4];
		REP(i, 4) REP(j, 4) {row[i][j] = 0; col[i][j] = 0;}
		int diag[2][4];
		REP(i, 2) REP(j, 4) {diag[i][j] = 0;}

		REP(i, 4) REP(j, 4){
			int e = conv(a[i][j]);
			++row[i][e];
			++col[j][e];
			if(i == j) ++diag[0][e];
			if(i == 3-j) ++diag[1][e];
		}
		bool oWon = false;
		bool xWon = false;
		bool draw = false;
		bool notFinished = false;
		REP(i, 4){
			if( row[i][conv('.')] ||
				col[i][conv('.')])
				{notFinished = true; break;}
		}
		REP(i, 4){
			if(  row[i][conv('O')] == 4 ||
				(row[i][conv('O')] == 3 && row[i][conv('T')] == 1))
				oWon = true;
			if(  row[i][conv('X')] == 4 ||
				(row[i][conv('X')] == 3 && row[i][conv('T')] == 1))
				xWon = true;
			if(  col[i][conv('O')] == 4 ||
				(col[i][conv('O')] == 3 && col[i][conv('T')] == 1))
				oWon = true;
			if(  col[i][conv('X')] == 4 ||
				(col[i][conv('X')] == 3 && col[i][conv('T')] == 1))
				xWon = true;
		}
		REP(i, 2){
			if(  diag[i][conv('O')] == 4 ||
				(diag[i][conv('O')] == 3 && diag[i][conv('T')] == 1))
				oWon = true;
			if(  diag[i][conv('X')] == 4 ||
				(diag[i][conv('X')] == 3 && diag[i][conv('T')] == 1))
				xWon = true;
		}
		cout << "Case #" << in << ": ";
		if(notFinished && !oWon && !xWon)
			cout << "Game has not completed";
		else if(oWon && xWon)
			cout << "Draw";
		else if(oWon)
			cout << "O won";
		else if(xWon)
			cout << "X won";
		else if(!notFinished)
			cout << "Draw";
		cout << endl;
	}
	return 0;
}
