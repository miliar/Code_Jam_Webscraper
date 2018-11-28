#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

string str(int i) 
{
	char s[100];
	sprintf(s, "%d", i);
	return string(s); 
}

int main()
{
	int cases;
	cin >> cases;
	for(int cs = 0; cs < cases; ++cs)
	{
		string lines[4];
		for(int i = 0; i < 4; ++i)
			cin >> lines[i];

		int rowX[4], colX[4], rowO[4], colO[4], diagX[2], diagO[2];
		for(int i = 0; i < 4; ++i)
			rowX[i] = colX[i] = rowO[i] = colO[i] = 0;
		for(int i = 0; i < 2; ++i)
			diagX[i] = diagO[i] = 0;

		bool empty = false;
		for(int i = 0; i < 4; ++i) 
		{
			for(int j = 0; j < 4; ++j) 
			{
				if(lines[i][j] == '.')
					empty = true;
				if(lines[i][j] == 'X') {
					++rowX[i];
					++colX[j];
				}
				if(lines[i][j] == 'O') {
					++rowO[i];
					++colO[j];
				}
				if(lines[i][j] == 'T') {
					++rowO[i];
					++colO[j];
					++rowX[i];
					++colX[j];
				}
			}
		}

		for(int i = 0; i < 4; ++i) 
		{
			if(lines[i][i] == 'O')
				++diagO[0];
			if(lines[i][3-i] == 'O')
				++diagO[1];
			if(lines[i][i] == 'X')
				++diagX[0];
			if(lines[i][3-i] == 'X')
				++diagX[1];
			if(lines[i][i] == 'T') {
				++diagX[0];
				++diagO[0];
			}
			if(lines[i][3-i] == 'T') {
				++diagX[1];
				++diagO[1];
			}
		}

		bool done = false;
		for(int i = 0; i < 4; ++i)
		{
			if(rowX[i] == 4 || colX[i] == 4 || diagX[i] == 4) {
				cout << "Case #" << cs+1 << ": " << "X won" << endl;
				done = true;
				break;
			}
			if(rowO[i] == 4 || colO[i] == 4 || diagO[i] == 4) {
				cout << "Case #" << cs+1 << ": " << "O won" << endl;	
				done = true;
				break;
			}
		}
		if(done)
			continue;
		
		if(empty)
			cout << "Case #" << cs+1 << ": " << "Game has not completed" << endl;	
		else
			cout << "Case #" << cs+1 << ": " << "Draw" << endl;	


	}
	return 0;
}