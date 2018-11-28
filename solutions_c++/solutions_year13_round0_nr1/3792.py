#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <string.h>

using namespace std;

string s1, s2, s3, s4;

int T;

bool xwon()
{
	if ((s1[0] == 'X' || s1[0] == 'T') && (s1[1] == 'X' || s1[1] == 'T') 
		&& (s1[2] == 'X' || s1[2] == 'T') && (s1[3] == 'X' || s1[3] == 'T'))
		return true;

	if ((s2[0] == 'X' || s2[0] == 'T') && (s2[1] == 'X' || s2[1] == 'T') 
		&& (s2[2] == 'X' || s2[2] == 'T') && (s2[3] == 'X' || s2[3] == 'T'))
		return true;

	if ((s3[0] == 'X' || s3[0] == 'T') && (s3[1] == 'X' || s3[1] == 'T') 
		&& (s3[2] == 'X' || s3[2] == 'T') && (s3[3] == 'X' || s3[3] == 'T'))
		return true;

	if ((s4[0] == 'X' || s4[0] == 'T') && (s4[1] == 'X' || s4[1] == 'T') 
		&& (s4[2] == 'X' || s4[2] == 'T') && (s4[3] == 'X' || s4[3] == 'T'))
		return true;

	if ((s1[0] == 'X' || s1[0] == 'T') && (s2[0] == 'X' || s2[0] == 'T') 
		&& (s3[0] == 'X' || s3[0] == 'T') && (s4[0] == 'X' || s4[0] == 'T'))
		return true;

	if ((s1[1] == 'X' || s1[1] == 'T') && (s2[1] == 'X' || s2[1] == 'T') 
		&& (s3[1] == 'X' || s3[1] == 'T') && (s4[1] == 'X' || s4[1] == 'T'))
		return true;

	if ((s1[2] == 'X' || s1[2] == 'T') && (s2[2] == 'X' || s2[2] == 'T') 
		&& (s3[2] == 'X' || s3[2] == 'T') && (s4[2] == 'X' || s4[2] == 'T'))
		return true;

	if ((s1[3] == 'X' || s1[3] == 'T') && (s2[3] == 'X' || s2[3] == 'T') 
		&& (s3[3] == 'X' || s3[3] == 'T') && (s4[3] == 'X' || s4[3] == 'T'))
		return true;

	if ((s1[0] == 'X' || s1[0] == 'T') && (s2[1] == 'X' || s2[1] == 'T')
		&& (s3[2] == 'X' || s3[2] == 'T') && (s4[3] == 'X' || s4[3] == 'T'))
		return true;

	if ((s1[3] == 'X' || s1[3] == 'T') && (s2[2] == 'X' || s2[2] == 'T')
		&& (s3[1] == 'X' || s3[1] == 'T') && (s4[0] == 'X' || s4[0] == 'T'))
		return true;
	return false;
}

bool owon()
{
	if ((s1[0] == 'O' || s1[0] == 'T') && (s1[1] == 'O' || s1[1] == 'T') 
		&& (s1[2] == 'O' || s1[2] == 'T') && (s1[3] == 'O' || s1[3] == 'T'))
		return true;

	if ((s2[0] == 'O' || s2[0] == 'T') && (s2[1] == 'O' || s2[1] == 'T') 
		&& (s2[2] == 'O' || s2[2] == 'T') && (s2[3] == 'O' || s2[3] == 'T'))
		return true;

	if ((s3[0] == 'O' || s3[0] == 'T') && (s3[1] == 'O' || s3[1] == 'T') 
		&& (s3[2] == 'O' || s3[2] == 'T') && (s3[3] == 'O' || s3[3] == 'T'))
		return true;

	if ((s4[0] == 'O' || s4[0] == 'T') && (s4[1] == 'O' || s4[1] == 'T') 
		&& (s4[2] == 'O' || s4[2] == 'T') && (s4[3] == 'O' || s4[3] == 'T'))
		return true;

	if ((s1[0] == 'O' || s1[0] == 'T') && (s2[0] == 'O' || s2[0] == 'T') 
		&& (s3[0] == 'O' || s3[0] == 'T') && (s4[0] == 'O' || s4[0] == 'T'))
		return true;

	if ((s1[1] == 'O' || s1[1] == 'T') && (s2[1] == 'O' || s2[1] == 'T') 
		&& (s3[1] == 'O' || s3[1] == 'T') && (s4[1] == 'O' || s4[1] == 'T'))
		return true;

	if ((s1[2] == 'O' || s1[2] == 'T') && (s2[2] == 'O' || s2[2] == 'T') 
		&& (s3[2] == 'O' || s3[2] == 'T') && (s4[2] == 'O' || s4[2] == 'T'))
		return true;

	if ((s1[3] == 'O' || s1[3] == 'T') && (s2[3] == 'O' || s2[3] == 'T') 
		&& (s3[3] == 'O' || s3[3] == 'T') && (s4[3] == 'O' || s4[3] == 'T'))
		return true;

	if ((s1[0] == 'O' || s1[0] == 'T') && (s2[1] == 'O' || s2[1] == 'T')
		&& (s3[2] == 'O' || s3[2] == 'T') && (s4[3] == 'O' || s4[3] == 'T'))
		return true;

	if ((s1[3] == 'O' || s1[3] == 'T') && (s2[2] == 'O' || s2[2] == 'T')
		&& (s3[1] == 'O' || s3[1] == 'T') && (s4[0] == 'O' || s4[0] == 'T'))
		return true;
	return false;
}

bool _i()
{
	return (s1[0] == '.' || s1[1] == '.' || s1[2] == '.' || s1[3] == '.'
		|| s2[0] == '.' || s2[1] == '.' || s2[2] == '.' || s2[3] == '.'
		|| s3[0] == '.' || s3[1] == '.' || s3[2] == '.' || s3[3] == '.'
		|| s4[0] == '.' || s4[1] == '.' || s4[2] == '.' || s4[3] == '.');
}

string i_to_s(int x)
{
	string s = "";
	while (x)
	{
		s = char(x % 10 + '0') + s;
		x /= 10;
	}
	return s;
}

void get_ans(int x, int res)
{
	string s = "Case #" + i_to_s(x) + ": ";
	if (res == 1)
		s = s + "X won";
	if (res == 2)
		s = s + "O won";
	if (res == 3)
		s = s + "Draw";
	if (res == 4)
		s = s + "Game has not completed";
	cout << s << endl;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin >> T;
	getline(cin, s1);
	for (int i = 1; i <= T; ++i)
	{
		getline(cin, s1);
		getline(cin, s2);
		getline(cin, s3);
		getline(cin, s4);
		
		int res = -1;
		
		if (res == -1 && xwon())
			res = 1;
		
		if (res == -1 && owon())
			res = 2;

		if (res == -1)
		{
			if(_i())
				res = 4;
			else
				res = 3;
		}
		get_ans(i, res);
		getline(cin, s1);
	}
}