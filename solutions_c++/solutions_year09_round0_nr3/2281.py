#include <fstream>
#include <vector>
#include <cstring>
#include <iomanip>
#include <iostream>
using namespace std;

int mem[1001][30];

int main() {

	ifstream fin("c.in");
	ofstream fout("c.out");

	int n;
	char buffer[1001];
	fin.getline(buffer, 1000);
	sscanf(buffer, "%d", &n);

	string word = "welcome to code jam";
	for (int test = 0; test < n; ++test) {

		memset(mem, 0, sizeof(mem));
		fin.getline(buffer, 1000);

		int bufLen = strlen(buffer);

		for (int t = 0; t < bufLen; ++t)
			if (buffer[t] == 'w') mem[t][0] = 1;

		for (int k = 1; k <= int(word.size()); ++k) {
			for (int t = 0; t < bufLen; ++t) {
				if (word[k - 1] == buffer[t])
					mem[t][k] = (mem[t][k - 1] + mem[t - 1][k]) % 10000;
				else
					mem[t][k] = mem[t - 1][k];
			}
		}
		fout << "Case #" << test + 1 << ": " << setw(4) << setfill('0') << mem[strlen(buffer) - 1][word.size()] << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
