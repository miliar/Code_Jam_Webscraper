#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

typedef vector<char> line;

typedef struct {
	int filled_pos;
	vector<line> table;
} board;

char lineFinished(board b) {
	for(int i = 0; i < b.table.size(); i++) {
		if(b.table[i][0] == '.')
			continue;

		short countX = 0;
		short countO = 0;
		short countT = 0;

		for(int j = 0; j < b.table[i].size(); j++) {

			if(b.table[i][j] == '.')
				break;

			switch(b.table[i][j]) {
				case 'X':
					countX++;
					break;
				case 'O':
					countO++;
					break;
				case 'T':
					countT++;
					break;
			}
		}

		if(countX == 4 || (countX == 3 && countT == 1))
			return 'X';
		else if(countO == 4 || (countO == 3 && countT == 1))
			return 'O';
	}

	return '\0';
}

char colFinished(board b) {
	for(int i = 0; i < 4; i++) {
		short countX = 0;
		short countO = 0;
		short countT = 0;

		for(int j = 0; j < 4; j++) {
			if(b.table[j][i] == '.')
				break;

			switch(b.table[j][i]) {
				case 'X':
					countX++;
					break;
				case 'O':
					countO++;
					break;
				case 'T':
					countT++;
					break;
			}
		}		

		if(countX == 4 || (countX == 3 && countT == 1))
			return 'X';
		else if(countO == 4 || (countO == 3 && countT == 1))
			return 'O';
	}

	return '\0';
}

char diagonalFinished(board b) {

	short countX = 0;
	short countO = 0;
	short countT = 0;

	for(int i = 0; i < b.table.size(); i++) {
		if(b.table[i][i] == '.')
			break;

		switch(b.table[i][i]) {
			case 'X':
				countX++;
				break;
			case 'O':
				countO++;
				break;
			case 'T':
				countT++;
				break;
		}

	}
	
	if(countX == 4 || (countX == 3 && countT == 1))
		return 'X';
	else if(countO == 4 || (countO == 3 && countT == 1))
		return 'O';

	countX = 0;
	countO = 0;
	countT = 0;

	for(int i = 0, j = 3; i < b.table.size() && j >= 0; i++, j--) {
		if(b.table[i][j] == '.')
			return '\0';

		switch(b.table[i][j]) {
			case 'X':
				countX++;
				break;
			case 'O':
				countO++;
				break;
			case 'T':
				countT++;
				break;
		}

	}

	cout << endl;
	
	if(countX == 4 || (countX == 3 && countT == 1))
		return 'X';
	else if(countO == 4 || (countO == 3 && countT == 1))
		return 'O';

	return '\0';
}


vector<board> readInput() {
	ifstream fin("A-large.in");

	vector<board> boards;

	int n = 0;

	fin >> n;

	for(int i = 0 ; i < n; i++) {
		char words[5];

		fin.getline(words, 5, '\n');

		if(strlen(words) == 0) {
			--i;
			continue;
		}

		board b;
		b.filled_pos = 0;

		for(int j = 0 ; j < 4; j++) {
			line l;
			string s(words);

			for(int k = 0; k < 4; k++) {
				if(s[k] != '.')
					b.filled_pos++;

				l.push_back(s[k]);
			}

			b.table.push_back(l);
			
			fin.getline(words, 5, '\n');
		}

		boards.push_back(b);

		if(boards.size() == n)
			break;
		
	}

	fin.close();

	return boards;
}

int main() {
	vector<board> boards = readInput();

	for(int i = 0; i < boards.size(); i++) {
		for(int k = 0; k < boards[i].table.size(); k++) {
			for(int j = 0; j < boards[i].table[k].size(); j++) {
				cout << boards[i].table[k][j] << " ";
			}
			cout << endl;
		}

		cout << endl;
	}

	ofstream fout("A-large.out");

	for(int i = 0; i < boards.size(); i++) {
		char c = lineFinished(boards[i]);

		if(c == '\0')
			c = colFinished(boards[i]);

		if(c == '\0')
			c = diagonalFinished(boards[i]);

		fout << "Case #" << i + 1 << ": ";

		if(c != '\0')
			 fout << c << " won";
		else {
			if(boards[i].filled_pos == 16)
				fout << "Draw";
			else
				fout << "Game has not completed";
		}

		fout << endl; 
	}
	fout.close();
}
