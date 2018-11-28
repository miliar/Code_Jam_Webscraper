#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int ground[101][101];
char basin[101][101];
int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t1, t2, T;
	fin >> T;
	for(int g = 1; g <= T; g++) {
	fin >> t1 >> t2;
	for(int i = 1; i <= t1; i++)
		for(int u = 1; u <= t2; u++) {
			basin[i][u] = 0;
			fin >> ground[i][u];
		}
	// ...
	char nextc = 'a';
	for(int i = 1; i <= t1; i++)
		for(int u = 1; u <= t2; u++) {
			int c1=i, c2=u;
			if (basin[i][u] != 0)
				nextc--;
			while (basin[c1][c2] == 0) {
					basin[c1][c2] = nextc;
				int nc1=c1, nc2=c2;
				int imin = 10001;
				if (c1 > 1) {
					if (ground[c1-1][c2] < ground[c1][c2])
					if (ground[c1-1][c2] < imin) {
						nc1=c1; nc2=c2;
						nc1 = c1-1;
						imin = ground[c1-1][c2];
					}
				}
				if (c2 > 1) {
					if (ground[c1][c2-1] < ground[c1][c2])
					if (ground[c1][c2-1] < imin) {
						nc1=c1; nc2=c2;
						nc2 = c2-1;
						imin = ground[c1][c2-1];
					}
				}
				if (c2 < t2) {
					if (ground[c1][c2+1] < ground[c1][c2])
					if (ground[c1][c2+1] < imin) {
						nc1=c1; nc2=c2;
						nc2 = c2+1;
						imin = ground[c1][c2+1];
					}
				}
				if (c1 < t1) {
					if (ground[c1+1][c2] < ground[c1][c2])
					if (ground[c1+1][c2] < imin) {
						nc1=c1; nc2=c2;
						nc1 = c1+1;
						imin = ground[c1+1][c2];
					}
				}
				if (imin == 10001)
					break;
				if (basin[nc1][nc2] != 0) {
					for(int ii = 1; ii <= t1; ii++)
						for(int uu = 1; uu <= t2; uu++)
							if(basin[ii][uu] == nextc)
								basin[ii][uu] = basin[nc1][nc2];
					nextc--;
					break;
				}
				c1 = nc1;c2=nc2;
			}
			nextc++;
		}
	fout << "Case #" << g << ":" << endl;
	for(int i= 1; i <= t1; i++) {
		fout << basin[i][1];
		for(int u = 2; u <= t2; u++)
			fout << " " << basin[i][u];
		fout << endl;
	}
}
	fin.close();
	fout.close();
	return 0;
}
