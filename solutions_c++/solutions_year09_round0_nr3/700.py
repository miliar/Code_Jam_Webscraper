#include <fstream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

const int LMAX = 600;
const int MOD = 10000;
const int MSIZE = 25;
const string message = "welcome to code jam";

char line[LMAX];

int mat[LMAX][MSIZE];

int main() {
	ifstream fin("input.txt");
	FILE* fout = fopen("output.txt", "w");
	fin.getline(line, LMAX);
	int n;
	sscanf (line, "%d", &n);
	for (int nt = 1; nt <= n; ++nt) {
		fin.getline(line, LMAX);
		int l = strlen(line);
		if (line[l - 1] == '\n') 
			l--;

		memset(mat, 0, sizeof(mat));
		mat[0][0] = 1;
		for (int i = 1; i <= l; ++i) {
			mat[i][0] = 1;
			for (int j = 1; j <= message.size(); ++j) {
				mat[i][j] = mat[i - 1][j];
				if (line[i - 1] == message[j - 1])
					mat[i][j] = (mat[i][j] + mat[i - 1][j - 1]) % MOD;
			}
		}
		fprintf (fout, "Case #%d: ", nt);
		int val = mat[l][message.size()];
		if (val < 1000) fprintf (fout, "0");
		if (val < 100) fprintf (fout, "0");
		if (val < 10) fprintf (fout, "0");
		fprintf (fout, "%d\n", val);
	}
	fclose(fout);
	return 0;
}