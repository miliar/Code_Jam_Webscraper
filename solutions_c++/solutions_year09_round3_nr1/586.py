#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int T;
string Cases[101];
int Numbers[62][101];

void input() {
	ifstream fin("input.txt");
	fin >> T;
	for(int i = 1; i <= T; i++)
		fin >> Cases[i];
	fin.close();
}

long long power(int a, int b) {
	if (b == 0)
		return 1;
	long long rez = a;
	for(int i = 2; i <= b; i++)
		rez *= a;
	return rez;
}
long long sums[101];
void solve() {
	for(int i = 1; i <= T; i++) {
		for(int u = 0; u <= 61; u++)
			Numbers[u][i] = -1;
		int current = 1;
		for(int u = 0; u < Cases[i].size(); u++) {
			char searchable;
			if (Numbers[u][i] == -1) {
				searchable = Cases[i][u];
				for(int o = u; o < Cases[i].size(); o++)
					if (Cases[i][o] == searchable)
						Numbers[o][i] = current;
				if (current == 1)
					current = 0;
				else if (current == 0)
					current = 2;
				else
					current++;
			}
		}
	int mode = 2;
	if (current > 2) {
		mode = current;
	// Convert number
	}
	sums[i] = 0;
	for(int u = 0; u < Cases[i].size(); u++) {
		sums[i] += Numbers[Cases[i].size()-1-u][i]*power(mode,u);
	}
}
}

void output() {
	ofstream fout("output.txt");
	for(int i = 1; i <= T; i++) {
		fout << "Case #" << i << ": " << sums[i] << endl;
	}
	fout.close();
}

int main() {
	input();
	solve();
	output();
	return 0;
}
