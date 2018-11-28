#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

string whowin(const vector<string> &vs) {

	int X = 0, O = 0, T = 0, D = 0;
	bool x3 = false;
	bool o3 = false;
	for (int i = 0; i < 4; i++) {
		if (vs[i][i] == 'X')
			X++;
		if (vs[i][i] == 'O')
			O++;
		if (vs[i][i] == 'T')
			T++;
		if (vs[i][i] == '.')
			D++;
	}
	if (X == 4) return "X won";
		if (O == 4) return "O won";
		if (X== 3 && (T==1 || D==1))	return "X won";
		if (O== 3 && (T==1 || D==1))	return "O won";
	if (O == 3) o3= true;
	if (X == 3) x3 = true;

	X = 0, O = 0, T = 0, D=0;
	for (int i = 0; i < 4; i++) {
		if (vs[i][3-i] == 'X')
			X++;
		if (vs[i][3-i] == 'O')
			O++;
		if (vs[i][3-i] == 'T')
			T++;
		if (vs[i][3-i] == '.')
			D++;
	}
	if (X == 4) return "X won";
		if (O == 4) return "O won";
		if (X== 3 && (T==1 || D==1))	return "X won";
		if (O== 3 && (T==1 || D==1))	return "O won";
	if (O == 3) o3= true;
	if (X == 3) x3 = true;

	//check vertical
	bool dot = false;
	bool x3p = false, o3p = false;
	for (int i = 0; i < 4; i++) {
		X = 0, O = 0, T = 0, D=0;
		for (int j = 0; j < 4; j++) {
			if (vs[i][j] == 'X')
				X++;
			if (vs[i][j] == 'O')
				O++;
			if (vs[i][j] == 'T')
				T++;
			if (vs[i][j] == '.') {
				D++;
				dot = true;
			}
		}
		if (X == 4) return "X won";
		if (O == 4) return "O won";
		if (X== 3 && (T==1 || D==1))	x3p = true;
		if (O== 3 && (T==1 || D==1))	o3p = true;
		if (O == 3) o3= true;
		if (X == 3) x3 = true;
	}
	if (x3p) return "X won";
	if (o3p) return "O won";

	
	//reset  test Horizontal
	for (int i = 0; i < 4; i++) {
		X = 0, O = 0, T = 0, D=0;
		for (int j = 0; j < 4; j++) {
			if (vs[j][i] == 'X')
				X++;
			if (vs[j][i] == 'O')
				O++;
			if (vs[j][i] == 'T')
				T++;
			if (vs[i][i] == '.')
				D++;
		}
		if (X == 4) return "X won";
		if (O == 4) return "O won";
		if (X== 3 && (T==1 || D==1)) x3p = true;
		if (O== 3 && (T==1 || D==1)) o3p = true;
		if (O == 3) o3= true;
		if (X == 3) x3 = true;
	}
	if (x3p) return "X won";
	if (o3p) return "O won";


	if (dot == false && x3 && o3) return "Draw";

	return "Game has not completed";
}

int main() {
	fstream in, out;
	in.open("proba.in", fstream::in);
	out.open("proba.out", fstream::out);

	int line_no;
	in >> line_no;
	for (int l = 1; l <=line_no; ++l) {

		vector<string> vs(4, string(4, ' '));
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				char vsi;
				in >> vsi;
				vs[i][j] =  vsi;
			}
		}
		string result = whowin(vs);

		out << "Case #" << l << ": " << result.c_str() << endl;
	}

	in.close();
	out.close();
	return 0;

}