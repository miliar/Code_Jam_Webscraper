#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int f[2][110];

int main() {
	ifstream fin("alarge.in");
	ofstream fout("outlargea.txt");
	int n;
	fin >> n;
	vector<string> engines;
	vector<int> queries;

	for (int t = 1; t <= n; t++) {
		engines.clear();
		int s, q;
		fin >> s;
		for (int i = 0; i < s; i++) {
			string name;
			getline(fin, name);
			while (name.length() == 0)
				getline(fin, name);
			engines.push_back(name);
		}
		queries.clear();
		fin >> q;
		memset(f, 0, sizeof(f));
		int flag = 0;
		for (int k = 0; k < q; k++) {
			string name;
			getline(fin, name);
			while (name.length() == 0)
				getline(fin, name);
			int now = -1;
			for (int i = 0; i < s; i++) {
				if (engines[i] == name) {
					now = i;
					break;
				}
			}
			if (now == -1)
				continue;
			f[1-flag][now] = -1;
			for (int i = 0; i < s; i++) {
				if (i == now)
					continue;
				int x = f[flag][i];
				for (int j = 0; j < s; j++) {
					if (j == i)
						continue;
					if (f[flag][j] != -1 && (x == -1 || x > f[flag][j] + 1))
						x = f[flag][j] + 1;
				}
				f[1-flag][i] = x;
			}
			flag = 1-flag;
			if (k > 0 && k % 100 == 0)
				cout << "  " << k << endl;
		}
		int ans = q+1;
		for (int i = 0; i < s; i++) {
			if (f[flag][i] != -1 && ans > f[flag][i])
				ans = f[flag][i];
		}
		cout << t << " sets completed" << endl;
		fout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
