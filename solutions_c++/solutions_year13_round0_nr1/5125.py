#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

char checkWin(char c1, char c2, char c3, char c4)
{
	vector<char> vec;
	vec.push_back(c1);
	vec.push_back(c2);
	vec.push_back(c3);
	vec.push_back(c4);
	sort(vec.begin(), vec.end());
	if (find(vec.begin(), vec.end(), '.') != vec.end())
		return 0;
	vector<char>::iterator ti = find(vec.begin(), vec.end(), 'T');
	if (ti != vec.end())
		vec.erase(ti);
	if (vec.front() == vec.back())
		return vec.front();
	return 0;
}

string winstr(char c)
{
	string toret(1, c);
	toret.append(" won");
	return toret;
}

string processCase(istream &in)
{
	string board[4];
	for (int row=0; row<4; ++row)
	{
		in >> board[row];
	}
	int i;
	char toret;
	for (i=0; i<4; ++i)
	{
		toret = checkWin(board[i][0], board[i][1], board[i][2], board[i][3]);
		if (toret) return winstr(toret);
	}
	for (i=0; i<4; ++i)
	{
		toret = checkWin(board[0][i], board[1][i], board[2][i], board[3][i]);
		if (toret) return winstr(toret);
	}
	toret = checkWin(board[0][0], board[1][1], board[2][2], board[3][3]);
	if (toret) return winstr(toret);
	toret = checkWin(board[0][3], board[1][2], board[2][1], board[3][0]);
	if (toret) return winstr(toret);
	for (i=0; i<4; ++i)
		for (int j=0; j<4; ++j)
			if (board[i][j] == '.')
				return "Game has not completed";
	return "Draw";
}

void process(istream &in, ostream &out)
{
	int cases;
	in >> cases;
	for (int i=1; i<=cases; ++i)
	{
		out << "Case #" << i << ": " << processCase(in) << endl;
	}
}

int main(int argc, char* argv[])
{
	if (argc == 1)
	{
		process(cin, cout);
	}
	else if (argc == 2)
	{
		ifstream in(argv[1], ifstream::in);
		process(in, cout);
	}
	return 0;
}
