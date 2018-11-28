#include <iostream>
#include <string>
#include <vector>


using namespace std;


// 'O' -> 0; 'X' -> 1; 'T' -> 10; empty -> -1
void readBox(vector<vector<int>> &box, bool &isFull) {
	string readLine;
	//Number of empty cells in the box
	int empty = 0;

	for(int li = 0; li < 4; ++li) {
		getline(cin, readLine);
		for(int ri = 0; ri < 4; ++ri) {
			if(readLine[ri] == 'O') {
				box[li][ri] = 0;
				continue;
			}
			if(readLine[ri] == 'X') {
				box[li][ri] = 1;
				continue;
			}
			if(readLine[ri] == 'T') {
				box[li][ri] = 10;
				continue;
			}
			box[li][ri] = -1;
			++empty;
		}
	}
	getline(cin, readLine);
	if(empty == 0)
		isFull = true;
}

// 'O' winner = 0; 'X' winner = 1; no winners = -1;
int checkLine(vector<vector<int>> &box, int l1, int r1, int l2, int r2) {
	int owner;
	if(box[l1][r1] == 10)
		owner = box[l2][r2];
	else
		owner = box[l1][r1];
	if(owner < 0)
		return -1;
	int lstep = (l2 - l1) / 3;
	int rstep = (r2 - r1) / 3;
	int li, ri, i;
	for(li = l1, ri = r1, i = 0; i < 4; ++i, li += lstep, ri += rstep ) {
		if(box[li][ri] == owner || box[li][ri] == 10)
			continue;
		else
			return -1;
	}
	return owner;
}

// 'O' winner = 0; 'X' winner = 1; no winners = -1;
int checkWinner(vector<vector<int>> &box) {
	// Lines
	int candidate = checkLine(box, 0, 0, 0, 3);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 1, 0, 1, 3);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 2, 0, 2, 3);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 3, 0, 3, 3);
	if(candidate != -1)
		return candidate;

	// Rows
	candidate = checkLine(box, 0, 0, 3, 0);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 0, 1, 3, 1);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 0, 2, 3, 2);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 0, 3, 3, 3);
	if(candidate != -1)
		return candidate;

	// Diagonals
	candidate = checkLine(box, 0, 0, 3, 3);
	if(candidate != -1)
		return candidate;
	candidate = checkLine(box, 0, 3, 3, 0);
	if(candidate != -1)
		return candidate;
	return -1;
}


void printWinner(int ti, int winner, bool isFull) {
	cout << "Case #" << ti << ": ";
	switch(winner) {
		case 0:
			cout << "O won" << endl;
			break;
		case 1:
			cout << "X won" << endl;
			break;
		default:
			if(isFull)
				cout << "Draw" << endl;
			else
				cout << "Game has not completed" << endl;
	}
}



int main()
{
	freopen("A-large.txt", "rt", stdin);
	freopen("out-A-large.txt", "wt", stdout);
	
	string readLine;

	// Number of tests
	int T;
	getline(cin, readLine);
	T = atof(readLine.c_str());
	
	for(int ti = 1; ti <= T; ++ti) {
		vector<vector<int>> box = vector<vector<int>>(4, vector<int>(4, 0));
		bool isFull = false;
		readBox(box, isFull);
		int winner = checkWinner(box);
		printWinner(ti, winner, isFull);

	}

	
	return 0;
}