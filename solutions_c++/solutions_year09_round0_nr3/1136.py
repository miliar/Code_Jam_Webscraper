#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	int n, i, j, k, r[510][30], nr;
	string s, input = "welcome to code jam";
	char ss[510];
	ifstream fin;
	ofstream fout;
	fin.open("C-large.in");
	fout.open("out.txt");
	
	fin >> n;
	fin.getline(ss, 510);
	for (k = 1; k <= n; k++) {
		fin.getline(ss, 510);
		s = ss;
		for (i = 0; i < s.length(); i++) 
			for (j = 0; j < input.length(); j++)
				r[i][j] = 0;
		if (s[0] == input[0]) r[0][0] = 1;
		for (i = 1; i < s.length(); i++) 
			for (j = 0; j < input.length(); j++) {
				r[i][j] = r[i-1][j];
				if (s[i] == input[j]) r[i][j] += (j > 0) ? r[i][j-1] : 1;
				r[i][j] %= 10000;
			};
		nr = r[s.length() - 1][input.length() - 1];
		fout << "Case #" << k << ": ";
		if (nr < 10) fout << "000";
		else if (nr < 100) fout << "00";
		else if (nr < 1000) fout << "0";
		fout << r[s.length() - 1][input.length() - 1] << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}