#include <iostream>
#include <fstream>
#include <stack>
#include <iterator>
#include <sstream>
#include <vector>

using namespace std;
	
int runs = 0;
ifstream infile;
string str;

string test(int run) {
	int x[5][5];
	int o[5][5];
	bool draw = true;

for (int a = 0; a < 5; ++a) {
	for (int b = 0; b < 5; ++b)
	{
		x[a][b] = 0;
		o[a][b] = 0;
	}
}
	for (int i = 0; i < 4; ++i) {
		getline(infile, str);
		// cout << str << endl;
		
		for (int j = 0; j < 4; ++j) 
		{
			if (str[j] == '.') draw = false;
			else if (str[j] == 'T') { x[i][j] = 1; o[i][j] = 1; }
			else if (str[j] == 'X') x[i][j] = 1;
			else if (str[j] == 'O') o[i][j] = 1;
			
		}
	}

	for (int a = 0; a < 4; ++a) {
		x[0][4] += x[0][a];
		x[1][4] += x[1][a];
		x[2][4] += x[2][a];
		x[3][4] += x[3][a];

		o[0][4] += o[0][a];
		o[1][4] += o[1][a];
		o[2][4] += o[2][a];
		o[3][4] += o[3][a];

		x[4][0] += x[a][0];
		x[4][1] += x[a][1];
		x[4][2] += x[a][2];
		x[4][3] += x[a][3];

		o[4][0] += o[a][0];
		o[4][1] += o[a][1];
		o[4][2] += o[a][2];
		o[4][3] += o[a][3];
	}

	for (int a = 0; a < 4; ++a) {
		if (x[a][4] == 4) return "X won";  
		if (x[4][a] == 4) return "X won";
		if (x[0][0] + x[1][1] + x[2][2] + x[3][3] == 4) return "X won"; 
		if (x[0][3] + x[1][2] + x[2][1] + x[3][0] == 4) return "X won";

		if (o[a][4] == 4) return "O won";
		if (o[4][a] == 4) return "O won";
		if (o[0][0] + o[1][1] + o[2][2] + o[3][3] == 4) return "O won"; 
		if (o[0][3] + o[1][2] + o[2][1] + o[3][0] == 4) return "O won";
	}

	if (!draw) return "Game has not completed";
	return "Draw";
	
}

int main() {
	infile.open("A.in");
	infile >> runs;
	infile.ignore(100, '\n');

	for (int i = 0; i < runs; ++i) {
		cout << "Case #" << i+1 << ": " << test(i) << endl; //<< endl;
		getline(infile, str);
	}
	return 0;
}