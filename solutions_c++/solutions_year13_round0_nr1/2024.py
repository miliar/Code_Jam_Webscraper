#include "stdafx.h"
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

bool check(const string& s, bool& xWon, bool& oWon)
{
		bool empty = s.find('.') != string::npos;
		if(!empty)
		{
			xWon = s.find('O') == string::npos;
			oWon = s.find('X') == string::npos;
			if(oWon || xWon)
				return true;
		}
		return false;
}

bool check(const vector<string>& field, bool& xWon, bool& oWon)
{
	for(int row=0; row<4; ++row)
	{
		const string& s = field[row];
		if(check(s, xWon, oWon))
			return true;
	}
	return false;
}

bool checkDiagonal(const vector<string>& field, int delta, bool& xWon, bool& oWon)
{
	int col = delta == 1 ? 0 : 3;
	string s;
	for(int row=0; row<4; ++row, col += delta)
		s.push_back(field[row][col]);
	return check(s, xWon, oWon);
}

vector<string> transpose(const vector<string>& field)
{
	vector<string> t;
	for(int col=0; col<4; ++col)
	{
		string s;
		for(int row =0; row < 4;++row)
			s.push_back(field[row][col]);
		t.push_back(s);
	}
	return t;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int t=0; t<T; ++t)
	{
		vector<string> field;
		copy_n(istream_iterator<string>(cin), 4, back_inserter(field));
		// string e;
		// cin >> e;
		bool incomplete = find_if(field.begin(), field.end(), [](const string& s) { return s.find('.') != string::npos;}) != field.end();
		bool xWon = false, oWon = false;
		if(!check(field, xWon, oWon))
		{
			field = transpose(field);
			if(!check(field, xWon, oWon))
			{
				if(!checkDiagonal(field, 1, xWon, oWon))
					checkDiagonal(field, -1, xWon, oWon);
			}
		}
		cout << "Case #" << t+1 << ": ";
		if(oWon) cout << "O won";
		else if(xWon) cout << "X won";
		else if(incomplete) cout << "Game has not completed";
		else cout << "Draw";
		cout << endl;
	}
	return 0;
}


