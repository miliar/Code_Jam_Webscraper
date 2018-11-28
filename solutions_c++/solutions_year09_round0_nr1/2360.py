#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;

string words[5001];
string unknown[501];

bool itis[501][16]['z'];

int main() {
	ifstream fin("input.txt"); 
	ofstream fout("output.txt");
	int L, D, N;
	fin >> L >> D >> N;
	for(int i = 1; i <= D; i++)
		fin >> words[i];
	for(int i = 1; i <= N; i++)
		fin >> unknown[i];
	for(int i = 1; i <= N; i++) {
		for(int u = 0; u <= 16; u++)
			for(int o = 0; o <= 'z'; o++)
				itis[i][u][o] = false;
		int poz = 0;
		for(int u = 0; u < unknown[i].size(); u++) {
			if (unknown[i][u] == '(') {
				while (unknown[i][u] != ')') {
					u++;
					itis[i][poz][unknown[i][u]] = true;
				}
				poz++;
			} else {
				itis[i][poz][unknown[i][u]] = true;
				 poz++;
			}
		}
	}
	// Count;
	for(int i = 1; i <= N; i++) {
		int rez = 0;
		for(int u = 1; u <= D; u++) {
			bool OK = true;
			for(int o = 0; o < L; o++)
				if (!itis[i][o][words[u][o]]) {
					OK = false;
					break;
				}
			if (OK)
				rez++;
		}
		fout << "Case #" << i << ": " << rez << endl;
	}
	return 0;
}
