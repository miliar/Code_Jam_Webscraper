#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int f[550][22];
char c[20] = "welcome to code jam";

int main() {
	int n;
	char s[550];
	ifstream fin("C-large.in");
	ofstream fout("cout.txt");
	fin >> n;
	for (int t = 0; t < n; t++) {
		fin.getline(s, 1000);
		while (!strcmp(s, ""))
			fin.getline(s, 1000);
		memset(f, 0, sizeof(f));
		f[0][0] = 1;
		int ans = 0;
		for (int i = 0; i < strlen(s); i++) {
			for (int j = 0; j < 20; j++) {
				if (f[i][j] == 0)
					continue;
				f[i+1][j] += f[i][j];
				f[i+1][j] %= 10000;
				if (s[i] != c[j])
					continue;
				f[i+1][j+1] += f[i][j];
				f[i+1][j+1] %= 10000;
			}
		}
		ans = f[strlen(s)][19];

		fout << "Case #" << t+1 << ": ";
		if (ans < 1000) fout << 0;
		if (ans < 100) fout << 0;
		if (ans < 10) fout << 0;
		fout << ans << endl;
	}
	return 0;
}
