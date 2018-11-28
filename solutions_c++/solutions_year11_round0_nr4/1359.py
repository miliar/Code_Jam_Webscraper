#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>
#include<iomanip>
using namespace std;
#define NONE 10000
#define MA 10000
double table1[100];
double point[100] = { 0 };
bool isT[100] = { false };
int m, n;

int main() {
	ifstream fin("test.in");
	ofstream fout("test.out");

	fin >> m;

	//fout.precision(6);
	for (int i = 0; i < m; i++) {
		fin >> n;
		double all = 0;
		for (int j = 1; j <= n; j++) {
			int temp;
			fin >> temp;
			if (temp != j)
				all += 1;
		}

		fout << "Case #" << i + 1 << ": " <<setiosflags(ios::fixed) <<setprecision(6)
				<< all << endl;
	}

	return 1;
}

