#include<iostream>
#include<fstream>

using namespace std;

int main() {
	long long rr, kk, g[1050], jump[1050], earn[1050];
	int testcase, n;
//	ifstream fin("C-large.in");
//	ofstream fout("C-large.out");
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	fin >> testcase;
	for (int t = 0; t < testcase; ++t) {
		fin >> rr >> kk >> n;
		fout << "Case #" << t+1 << ": ";
		for (int i = 1; i <= n; ++i) {
			fin >> g[i];
		}
		int now = 1;
		long long tot = 0;
		for (int i = 1; i <= n; ++i) {
			while (tot + g[now] <= kk) {
				tot += g[now];
				now ++;
				if (now > n) now = 1;
				if (now == i) break;
			}
			jump[i] = now;
			earn[i] = tot;
			tot -= g[i];
		}
		double total = 0;
		now = 1;
		for (int i = 1; i <= rr; ++i) {
			total += earn[now];
			now = jump[now];
		}
		fout << total << endl;
	}
	fin.close();
	fout.close();
	return 0;

}