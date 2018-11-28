#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define MAX 50

int a[MAX][MAX];
int n;

void swr(int x, int y) {
	int i, aux, j;
	for (i = 0; i < n; i++) {
		aux = a[y][i]; 
		for (j = y; j > x; j--) a[j][i] = a[j-1][i]; 
		a[x][i] = aux;
	}
}


int findr(int nn) {
	int i, k, j;
	for (i = n - nn; i < n; i++) {
		k = 0;
		for (j = n - nn + 1; j < n; j++) 
			if (a[i][j] == 1) k++;
		if (k > 0) continue;
		else return i;
	}
}

int main() {
	int i, j, k, sol, aux, t, nn;
	string s;
	ifstream fin("A-large.in");
	ofstream fout("test.out");

	fin >> t;
	for (k = 1; k <= t; k++) {
		fin >> n;
		fout << "Case #" << k << ": ";
		for (i = 0; i < n; i++) {
			fin >> s;
			for (j = 0; j < n; j++) a[i][j] = (int) (s[j] - '0');
		}
		sol = 0;
		nn = n;
		while (nn > 1) {
			aux = findr(nn);
			if (aux != n - nn) sol += aux - n + nn;
			swr(n - nn, aux);
		/*	aux = n - nn;
			for (i = n - nn + 1; i < n; i++) {
				if (a[0][i] == 1) aux = i;
			}
			if (aux != (n-nn)) {
				sol++;
				swc(n - nn, aux);
			}*/
			nn--;
		}
		fout << sol << "\n";
	}

	fin.close();
	fout.close();
	return 0;
}
