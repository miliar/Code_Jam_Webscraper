#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main() {
	int tot;
	fin >> tot;
	for (int ntot = 1; ntot <= tot; ++ntot) {
		int a[100], n, d, m;
		bool flag = 0;
		fin >> n >> d >> m;
		for (int i = 0; i < n; ++i) fin >> a[i];
		sort(a, a + n);
		fout << "Case #" << ntot << ": ";
		for (int i = n - 1; i >= 0; --i) {
			if (a[i] >= m * 3) continue;
			else if (a[i] >= m * 3 - 2 && m - 1 >= 0) continue;
			else if (d && a[i] >= m * 3 - 4 && m - 2 >= 0) --d;
			else {
				fout << n - 1 - i << endl;
				flag = 1;
				break;
			}
		}
		if (!flag) fout << n << endl;
	}
}
