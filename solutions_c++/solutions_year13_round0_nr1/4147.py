/*
 * Problem A. Tic-Tac-Toe-Tomek.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: sara
 */

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int t;
	int c = 1;
	vector<string> board(4);
	string space;
	scanf("%d", &t);
	getline(cin, space);
	while (c <= t)
	{
		int X = 0;
		int O = 0;
		int T = 0;
		int dot = 0;
		bool xWon = false;
		bool oWon = false;

		for(int i = 0 ; i < 4; i++)
			{
				getline(cin, board[i]);
			}

		getline(cin, space);
		for(int i = 0 ; i < 4; i++)
		{
			X = 0;
			O = 0;
			T = 0;
			for(int j = 0 ; j < 4; j++)
			{
				if(board[i][j] == 'X') X++;
				else if(board[i][j] == 'O') O++;
				else if(board[i][j] == 'T') T++;
				else if (board[i][j] == '.') dot++;

			}
//			cout<<"i : "<<i<<"& c : "<<c<<endl;
//			cout<<X<<O<<T<<endl;
			if(X == 4 || X+ T == 4)
			{
				xWon = true;
				break;
			}
			else if (O == 4 || O +T == 4)
			{
				oWon = true;
				break;
			}

			X = 0;
			O = 0;
			T = 0;
			for(int j = 0 ; j < 4; j++)
			{
				if(board[j][i] == 'X') X++;
				else if(board[j][i] == 'O') O++;
				else if(board[j][i] == 'T') T++;
				else if (board[i][j] == '.') dot++;
			}
			if(X == 4 || X+ T == 4)
			{
				xWon = true;
				break;
			}
			else if (O == 4 || O +T == 4)
			{
				oWon = true;
				break;
			}
		}
		X = 0;
		O = 0;
		T = 0;
		for(int j = 0 ; j < 4 && !xWon && !oWon ; j++)
		{
			if(board[j][j] == 'X') X++;
			else if(board[j][j] == 'O') O++;
			else if(board[j][j] == 'T') T++;
		}
		if(X == 4 || X + T == 4)
			xWon = true;

		else if (O == 4 || O +T == 4)
			oWon = true;

		X = 0;
		O = 0;
		T = 0;
		for(int j = 0 ; j < 4 && !xWon && !oWon ; j++)
		{
			if(board[j][3-j] == 'X') X++;
			else if(board[j][3-j] == 'O') O++;
			else if(board[j][3-j] == 'T') T++;
		}
		if(X == 4 || X + T == 4)
			xWon = true;

		else if (O == 4 || O +T == 4)
			oWon = true;

		if(xWon)
			printf("Case #%d: X won\n", c);
		else if(oWon)
			printf("Case #%d: O won\n", c);
		else if (dot > 0)
			printf("Case #%d: Game has not completed\n", c);
		else
			printf("Case #%d: Draw\n", c);
		c++;
	}
	return 0;
}	
	













