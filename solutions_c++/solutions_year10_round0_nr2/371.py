#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <cctype>
using namespace std;

int times[1000][100], temp[100];
int sizes[1000], stemp;

ifstream fin("B-large.in");
ofstream fout("out.txt");

void readnum(int *num, int &size) {
	while (!isdigit(fin.peek())) fin.ignore();
	size = 0;
	do {
		num[size++] = fin.peek() - '0';
		fin.ignore();
	} while (isdigit(fin.peek()));
	for (int j = 0; j < size - 1 - j; ++j) {
		int t = num[j];
		num[j] = num[size - 1 - j];
		num[size - 1 - j] = t;
	}
	while (size > 0 && num[size - 1] == 0) --size;
}

void sub(int *num1, int &size1, int *num2, int &size2) {
	int j;
	for (j = 0; j < size1 && j < size2; ++j) num1[j] -= num2[j];
	for (; j < size2; ++j) num1[j] = -num2[j];
	if (size1 < size2) size1 = size2;
	for (j = 0; j < size1 - 1; ++j) if (num1[j] < 0) {
			num1[j + 1] -= (-num1[j] + 9) / 10;
			num1[j] += (-num1[j] + 9) / 10 * 10;
		}
	if (num1[size1 - 1] < 0) {
		for (j = 0; j < size1; ++j) num1[j] = -num1[j];
		for (j = 0; j < size1 - 1; ++j) if (num1[j] < 0) {
				num1[j + 1] -= (-num1[j] + 9) / 10;
				num1[j] += (-num1[j] + 9) / 10 * 10;
			}
	}
	while (size1 > 0 && num1[size1 - 1] == 0) --size1;
}

void mod(int *num1, int &size1, int *num2, int &size2) {
	if (size1 < size2 || size2 == 0) return;
	int ssize = size1 - 1;
	mod(num1 + 1, ssize, num2, size2);
	size1 = ssize + 1;
	while (size1 > 0 && num1[size1 - 1] == 0) --size1;
	for (;;) {
		if (size1 < size2) return;
		if (size1 == size2)
			for (int j = size1 - 1; j >= 0; --j) {
				if (num1[j] < num2[j]) return;
				if (num1[j] > num2[j]) break;
			}
		for (int j = 0; j < size2; ++j) num1[j] -= num2[j];
		for (int j = 0; j < size1 - 1; ++j) if (num1[j] < 0) {
				num1[j + 1] -= (-num1[j] + 9) / 10;
				num1[j] += (-num1[j] + 9) / 10 * 10;
			}
		while (size1 > 0 && num1[size1 - 1] == 0) --size1;
	}
}

void gcd(int *num1, int &size1, int *num2, int &size2) {
	while (size1 > 0 && size2 > 0) {
		mod(num1, size1, num2, size2);
		mod(num2, size2, num1, size1);
	}
	if (size1 == 0) {
		for (int j = 0; j < size2; ++j) num1[j] = num2[j];
		size1 = size2;
	}
}

int main() {
	int c, n;
	fin >> c;
	for (int i = 1; i <= c; ++i) {
		fout << "Case #" << i << ": ";
		fin >> n;
		/*int tnum[1000], g;
		for (int j = 0; j < n; ++j) fin >> tnum[j];
		for (int j = 0; j < n - 1; ++j) {
			tnum[j] -= tnum[j + 1];
			if (tnum[j] < 0) tnum[j] = -tnum[j];
		}
		g = tnum[0];
		for (int j = 1; j < n - 1; ++j) {
			while (g != 0 && tnum[j] != 0) {
				g %= tnum[j];
				if (g != 0) tnum[j] %= g;
			}
			if (g == 0) g = tnum[j];
		}
		tnum[n - 1] %= g;
		fout << (g - tnum[n - 1]) % g << endl;
		continue;*/
		for (int j = 0; j < n; ++j) readnum(times[j], sizes[j]);
		for (int j = 0; j < n - 1; ++j) sub(times[j], sizes[j], times[j + 1], sizes[j + 1]);
		for (int j = 0; j < sizes[0]; ++j) temp[j] = times[0][j];
		stemp = sizes[0];
		for (int j = 1; j < n - 1; ++j) gcd(temp, stemp, times[j], sizes[j]);
		mod(times[n - 1], sizes[n - 1], temp, stemp);
		if (sizes[n - 1] == 0) fout << 0 << endl;
		else {
			sub(temp, stemp, times[n - 1], sizes[n - 1]);
			for (int j = stemp - 1; j >= 0; --j) fout << temp[j];
			fout << endl;
		}
	}
	return 0;
}
