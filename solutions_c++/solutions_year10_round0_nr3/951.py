#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <cctype>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("out.txt");

int groups[1000], s[1000], next[1000];
int s1, n1, s2, n2, l;

void compute() {
	bool visit[1000] = {false};
	int i;
	l = 0;
	while (!visit[l]) {
		visit[l] = true;
		l = next[l];
	}
	s1 = 0;
	n1 = 0;
	for (i = 0; i != l; i = next[i]) {
		s1 += s[i];
		++n1;
	}
	s2 = 0;
	n2 = 0;
	do {
		s2 += s[i];
		++n2;
		i = next[i];
	} while (i != l);
}

int goover(int start, int num) {
	int sum = 0;
	for (int i = 0; i < num; ++i, start = next[start])
		sum += s[start];
	return sum;
}

int main() {
	int t, r, k, n;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		fout << "Case #" << i << ": ";
		fin >> r >> k >> n;
		for (int j = 0; j < n; ++j) fin >> groups[j];
		for (int j = 0; j < n; ++j) {
			s[j] = 0;
			int jj = j;
			while (s[j] + groups[jj] <= k) {
				s[j] += groups[jj++];
				if (jj >= n) jj %= n;
				if (jj == j) break;
			}
			next[j] = jj;
		}
		compute();
		if (r <= n1) fout << goover(0, r) << endl;
		else fout << s1 + s2 * ((r - n1) / n2) + goover(l, (r - n1) % n2) << endl;
	}
	return 0;
}
