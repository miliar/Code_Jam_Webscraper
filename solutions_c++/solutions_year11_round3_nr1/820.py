#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
    //ifstream in("..//..//sample.in.txt");
	ifstream in("..//..//A-large-1.in.txt");
	if (!in)
	{
		cout << "Input file cannot be opened";
		return 1;
	}
	
	ofstream out("output.txt");
	if (!out) {
		cout << "Output file cannot be opened";
		in.close();
		return 1;
	}
	
	int T;
	in >> T;
	
	for (int t = 0; t < T; t++) {
		int R, C;
		in >> R >> C;
		
		char grid[R][C];
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				in >> grid[r][c];
			}
		}
		
		bool isImpossible = false;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (grid[r][c] == '#') {
					// check if 2x2 is BLUE
					if (r + 1 < R && c + 1 < C &&
						grid[r][c + 1] == '#' &&
						grid[r + 1][c] == '#' &&
						grid[r + 1][c + 1] == '#') {
						
						grid[r][c] = '/';
						grid[r][c + 1] = '\\';
						grid[r + 1][c] = '\\';
						grid[r + 1][c + 1] = '/';
					}
					else {
						isImpossible = true;
						break;
					}
				}
			}
			if (isImpossible)
				break;
		}		
		
		out << "Case #" << (t + 1) << ": " << endl;
		if (isImpossible) {
			out << "Impossible" << endl;
		}
		else {
			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					out << grid[r][c];
				}
				out << endl;
			}
		}
	}
	
	in.close();
	out.close();
	
    return 0;
}
