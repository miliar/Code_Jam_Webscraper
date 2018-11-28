#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int main() {
	int T;
	const int N = 4;

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		string h[N];
		string v[N];
		string x[2];
		string s;

		for (int i = 0; i < N; ++i)
		{
			cin >> h[i];
			s += h[i];
		}
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
				v[j].push_back(h[i][j]);	
			x[0].push_back(h[i][i]);
			x[1].push_back(h[i][N-1-i]);
		}

		char winner = 'D';
		if (s.find('.') != string::npos)
			winner = 'T';

		for (int i = 0; i < N; ++i) {
			if (h[i].find('.') != string::npos)
				continue;
			if (h[i].find('X') != string::npos && h[i].find('O') != string::npos)
				continue;
			if (h[i].find('X') != string::npos)
				winner = 'X';
			else
				winner = 'O';
			goto output;		
		}

		for (int i = 0; i < N; ++i) {
			if (v[i].find('.') != string::npos)
				continue;
			if (v[i].find('X') != string::npos && v[i].find('O') != string::npos)
				continue;
			if (v[i].find('X') != string::npos)
				winner = 'X';
			else
				winner = 'O';
			goto output;
		}
		for (int i = 0; i < N; ++i) {
			if (x[i].find('.') != string::npos)
				continue;
			if (x[i].find('X') != string::npos && x[i].find('O') != string::npos)
				continue;
			if (x[i].find('X') != string::npos)
				winner = 'X';
			else
				winner = 'O';
			goto output;
		}
output:
		cout << "Case #" << t << ": "; 
		switch (winner) {
		case 'D':
			cout << "Draw\n";
			break;
		case 'T':
			cout << "Game has not completed\n";
			break;
		case 'X':
			cout << "X won\n";
			break;
		case 'O':
			cout << "O won\n";
			break;
		}
	}


	return 0;
}

