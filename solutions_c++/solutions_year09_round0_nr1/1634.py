#include <fstream>
#include <iostream>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int L, D, N;

const int MAXL = 15;
const int MAXD = 5000;
const int MAXN = 500;

char words[MAXD][MAXL];

int round = 1;

void Input() {
	memset(words, 0, sizeof(words));
	fin >> L >> D >> N;
	for (int i = 0; i < D; i++)
		for (int j = 0; j < L; j++)
			fin >> words[i][j];
}

char data[MAXL * (MAXL + 2)];
bool list[MAXL][26];

void DoIt() {
	memset(data, 0, sizeof(data));
	memset(list, 0, sizeof(list));
	fin.getline(data, sizeof(data));
	int current = 0;
	bool isin = false;
	for (int i = 0; i < strlen(data); i++) {
		if (data[i] == '(') {
			isin = true;
			continue;
		}
		if (data[i] == ')') {
			isin = false;
			current++;
			continue;
		}
		list[current][data[i] - 'a'] = 1;
		if (!isin) {
			current++;
		}
	}

	int total = 0;
	for (int i = 0; i < D; i++) {
		bool inc = true;
		for (int l = 0; l < L; l++) {
			if (list[l][words[i][l] - 'a'] == false) {
				inc = false;
				break;
			}
		}
		if (inc)
			total++;
	}
	fout << "Case #" << round++ << ": " << total << endl;
}

int main() {
	Input();
	fin.getline(data, sizeof(data));
	for (int i = 0; i < N; i++)
		DoIt();
	return 0;
}