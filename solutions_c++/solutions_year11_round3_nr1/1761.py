#include <iostream> // AUFGABE A
#include <fstream>

using namespace std;

const problem = 2;

int main(int argc, char** argv) {
	fstream in;
	fstream out;

	switch(problem) {
		case 0:
			in.open("D:\\A-test.in", ios::in);
			out.open("D:\\out.out", ios::out);
			break;
		case 1:
			in.open("D:\\Downloads\\A-small-attempt0.in", ios::in);
			out.open("D:\\out.out", ios::out);
			break;
		case 2:
			in.open("D:\\Downloads\\A-large.in", ios::in);
			out.open("D:\\out.out", ios::out);
			break;
	}

	int T, R, C;
	int tile[50][50];
	char ch;

    in >> T;
	
	

	for(int t=1; t<=T; t++) {
		in >> R >> C;

		bool possible = true;

		for(int i=0; i<R; i++) {
			for(int j=0; j<C; j++) {
				in >> ch;
				tile[i][j] = ch;
			}
		}

		for(int i=0; i<R; i++) {
			for(int j=0; j<C; j++) {
				if(tile[i][j] == 35) {
					if(i+1 == R || j+1 == C) {
						possible = false;
						break;
					}
					tile[i][j] = 47;
					if(tile[i+1][j] != 35 || tile[i+1][j+1] != 35 || tile[i][j+1] != 35) {
						possible = false;
						break;
					}
					tile[i][j+1] = 92;
					tile[i+1][j+1] = 47;
					tile[i+1][j] = 92;
				}
			}
			if(!possible) break;
		}

		out << "Case #" << t << ":" << endl;
		if(possible) {
			for(int i=0; i<R; i++) {
				for(int j=0; j<C; j++) {
					out << static_cast<char>(tile[i][j]);
				}
				out << endl;
			}
		} else out << "Impossible" << endl;
	}

    in.close();
	out.close();
}