#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <functional>
using namespace std;
int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N;
	fin >> N;
	string lookup[] = {"XT", "OT"};
	for (int cas = 0; cas < N; ++cas) {
		char field[4][4] = {};
		int left = 0;
		fout << "Case #" << cas + 1 << ": ";
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				fin >> field[i][j];
				if (field[i][j] == '.')
					++left;
			}
		string diag = left == 0 ? "Draw" : "Game has not completed";
		for (int side = 0; side < 2; ++side) {
			bool won = false;
			for (int i = 0; i < 4; ++i) {
				bool f = true, g = true;
				for (int j = 0; j < 4; ++j) {
					if (lookup[side].find(field[i][j]) == string::npos)
						f = false;
					if (lookup[side].find(field[j][i]) == string::npos)
						g = false;
				}
				won = won || f || g;
				if (won) break;
			}
			if (!won) {
				bool f = true, g = true;
				for (int i = 0; i < 4; ++i) {
					if (lookup[side].find(field[i][i]) == string::npos)
						f = false;
					if (lookup[side].find(field[i][3-i]) == string::npos)
						g = false;
				}
				won = won || f || g;
			}
			if (won) {
				diag = (side ? "O" : "X") + string(" won");
				break;
			}
		}
		fout << diag << endl;
	}
}