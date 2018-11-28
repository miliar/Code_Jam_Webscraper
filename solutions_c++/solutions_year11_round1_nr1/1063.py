#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input");
ofstream fout("output");

void solve()
{
	long long n;
	int pd, pg;
	fin >> n >> pd >> pg;
	if (pg == 0) {
		if (pd == 0) {
			fout << "Possible" << endl;
		}
		else {
			fout << "Broken" << endl;
		}
		return;
	}
	if (pg == 100) {
		if (pd == 100) {
			fout << "Possible" << endl;
		}
		else {
			fout << "Broken" << endl;
		}
		return;
	}
	if (pd == 0) {
		fout << "Possible" << endl;
		return;
	}
	int d = -1;
	for (int wd = 1; wd * 100 / pd <= n; wd++) {
		if ((wd * 100) % pd == 0) {
			d = wd * 100 / pd;
			break;
		}
	}
	if (d == -1) {
		fout << "Broken" << endl;
	}
	else {
		fout << "Possible" << endl;
	}
}

int main()
{
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
