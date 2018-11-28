#include <iostream>
#include <fstream>

using namespace std;

#define MAX 10010

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};


int a[110][110], n, m, b[110][110];

void lee(int x, int y, int *val) {
	int min, i, j;
	if (b[x][y] != 0) {
		for (i = 1; i <= n; i++) 
			for (j = 1; j <= m; j++) 
				if (b[i][j] == *val) b[i][j] = b[x][y];
		(*val)--;
	} else {
		b[x][y] = *val;
		min = 0;
		for (j = 1; j <= 3; j++) 
			if (a[x + dx[min]][y + dy[min]] > a[x + dx[j]][y + dy[j]]) 
				min = j;
		if (a[x][y] > a[x + dx[min]][y + dy[min]]) lee (x + dx[min], y + dy[min], val);
	}
}



int main() {
	int t, val, i, j, k;
	
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("out.txt");

	fin >> t;
	for (i = 1; i <= t; i++) {
		val = 0;
		fin >> n >> m;
		for (j = 1; j <= n; j++)
			for (k = 1; k <= m; k++) fin >> a[j][k];
		
		for (j = 0; j <= n+1; j++) a[j][0] = a[j][m+1] = MAX;
		for (j = 0; j <= m+1; j++) a[0][j] = a[n+1][j] = MAX;
		for (j = 0; j <= n+1; j++) 
			for (k = 0; k <= m+1; k++) b[j][k] = 0;
		for (j = 1; j <= n; j++)
			for (k = 1; k <= m; k++) 
				if (b[j][k] == 0) {
					val++;
					lee(j, k, &val);
				};
		fout << "Case #" << i << ":\n";
		for (j = 1; j <= n; j++) {
			for (k = 1; k <=m; k++) fout << (char)(b[j][k] + 96) << " ";
			fout << "\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}
