#include <iostream>
#include <algorithm>
#include "stdio.h"


using namespace std;


bool check(char s[4][4], char ch)
{
	int i;
	for(i = 0; i < 4; i ++)
	{
		if(s[i][0] == ch && s[i][1] == ch && s[i][2] == ch && s[i][3] == ch)
			return true;
		if(s[0][i] == ch && s[1][i] == ch && s[2][i] == ch && s[3][i] == ch)
			return true;
	}
	if(s[0][0] == ch && s[1][1] == ch && s[2][2] == ch && s[3][3] == ch)
		return true;
	if(s[0][3] == ch && s[1][2] == ch && s[2][1] == ch && s[3][0] == ch)
		return true;
	return false;
}

int main()
{
	int t;
	cin >> t;
	
	for(int CASE = 1; CASE <= t; CASE ++)
	{
		int i, j;
		string s;
		for(i = 0; i < 4; i ++)
		{
			string temp;
			cin >> temp;
			s = s+temp;
		}
		char x[4][4], o[4][4];
		bool flag = false;
		for(i = 0; i < 4; i ++)
		{
			for(j = 0; j < 4; j ++)
			{
				x[i][j] = s[i*4+j];
				o[i][j] = s[i*4+j];
				if(x[i][j] == 'T')
				{
					x[i][j] = 'X';
					o[i][j] = 'O';
				}
				if(x[i][j] == '.')
					flag = true;
			}
		}
		
		bool xx = check(x, 'X');
		bool oo = check(o, 'O');
		if(xx)
			printf("Case #%d: X won\n", CASE);
		else if(oo)
			printf("Case #%d: O won\n", CASE);
		else if(flag)
			printf("Case #%d: Game has not completed\n", CASE);
		else
			printf("Case #%d: Draw\n", CASE);
	}
	return 0;
	
}