#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef enum {DRAW, NOTCOMP, X, O} Status;

Status check_line(string line) {
	int xc, oc, tc, ec;
	xc=0; oc=0; tc=0; ec=0;
	for (int i=0; i<4; i++) {
		if (line[i] == 'X')
			xc++;
		else if (line[i] == 'O')
			oc++;
		else if (line[i] == 'T')
			tc++;
		else if (line[i] == '.')
			ec++;
	}
	
	if (xc == 4 || (xc == 3 && tc == 1)) 
		return X;
	else if (oc == 4 || (oc == 3 && tc == 1)) 
		return O;
	else if (ec > 0)
		return NOTCOMP;
	else
		return DRAW;
}

string winner(Status s) {
	string x = "X won";
	string o = "O won";
	string d = "Draw";
	string n = "Game has not completed";
	if (s == X)
		return x;
	else if (s == O)
		return o;
	else if (s == DRAW)
		return d;
	else
		return n;
}

Status check_grid(string lines[]) {
	Status gs;
	gs = DRAW;
	string all[10];
	
	for (int i=0; i < 4; i++) {
		std::stringstream ss;
		for( int j = 0; j < 4; j++) 
			ss << lines[j][i];
		all[i+4] = ss.str();
	}
	std::stringstream col1, col2;
	col1 << lines[0][0];
	col1 << lines[1][1];
	col1 << lines[2][2];
	col1 << lines[3][3];
	
	col2 << lines[0][3];
	col2 << lines[1][2];
	col2 << lines[2][1];
	col2 << lines[3][0];
		
	all[8] = col1.str();
	all[9] = col2.str();
	
	for (int i=0; i < 4; i++) {
		all[i] = lines[i];
	}
	
	for (int i=0; i < 10; i++) {
		Status s = check_line(all[i]) ;
		//cout << "Checked line[" << i << "] " << all[i] << " " << winner(s) << endl; 
		if (s == X || s == O)
			return s;
		if (s == NOTCOMP)
			gs = NOTCOMP;
	}
	
	return gs;
}

int main(int argc, char *argv[]) {
	string line;
	int n;
	getline(cin, line);
	stringstream nstream(line);
	nstream >> n;
	//cout << "Test cases are " << n << endl;
	
	for (int i = 0; i < n; ++i) {
		string lines[4];
		for (int j=0; j < 4; j++) {
			getline(cin, lines[j]);
		}
		
		int tnum = i + 1;
		cout <<"Case #"<< tnum << ": "<< winner(check_grid(lines)) << endl;
		getline(cin, line);
	}
	return 0;
		
}