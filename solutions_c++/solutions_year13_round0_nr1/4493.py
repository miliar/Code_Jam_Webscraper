#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool checkline(const string& line, char sym)
{
	for (size_t i = 0; i < line.size(); ++i)
		if (line[i] != sym && line[i] != 'T')
			return false;

	return true;
}

bool checkrow(const vector<string>& m, size_t i, char sym)
{
	return checkline(m[i], sym);
}

bool checkcol(const vector<string>& m, size_t i, char sym)
{
	string line;
	for (size_t j = 0; j < m.size(); ++j)
		line.append(1, m[j][i]);
	return checkline(line, sym);
}

bool checkdiags(const vector<string>& m, char sym)
{
	string left, right;
	for (size_t i = 0; i < m.size(); ++i)
		left.append(1, m[i][i]);
	for (size_t i = 0; i < m.size(); ++i)
		right.append(1, m[m.size() - 1 - i][i]);

	return checkline(left, sym) || checkline(right, sym);
}

string gameresult(const vector<string>& m)
{
	for (size_t i = 0; i < m.size(); ++i)
	{
		if (checkrow(m, i, 'X') || checkcol(m, i, 'X') || checkdiags(m, 'X'))
			return "X won";
		if (checkrow(m, i, 'O') || checkcol(m, i, 'O') || checkdiags(m, 'O'))
			return "O won";
	}

	for (size_t i = 0; i < m.size(); ++i)
		if (m[i].find('.') != string::npos)
			return "Game has not completed";

	return "Draw";
}

int main()
{
	size_t T = 0;
	cin >> T;
	for (size_t i = 0; i < T; ++i)
	{
		vector<string> m(4);
		cin >> m[0] >> m[1] >> m[2] >> m[3];
		cout << "Case #" << i+1 << ": " << gameresult(m) << endl;
	}

	return 0;
}