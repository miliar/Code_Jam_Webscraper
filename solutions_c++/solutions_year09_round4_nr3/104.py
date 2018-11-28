#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int n, k;
int a[110][110], g[110][110];
int p[110];
bool v[110];

bool find(int k) {
	for (int i = 0; i < n; i++) {
		if (g[k][i] == 1 && !v[i]) {
			v[i] = true;
			if (p[i] < 0 || find(p[i])) {
				p[i] = k;
				return true;
			}
		}
	}
	return false;
}

int main() {
	ifstream fin("C-large.in");
	ofstream fout("cout.txt");

	fin >> T;
	for (int t = 0; t < T; t++) {
		fout << "Case #" << t+1 << ": ";
		fin >> n >> k;

		vector<pair<int, int> > s;
		s.clear();

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k; j++) {
				fin >> a[i][j];
			}
			s.push_back(make_pair(a[i][0], i));			
		}
		sort(s.begin(), s.end());

		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; i++) {
			for (int j = i+1; j < n; j++) {
				bool ok = true;
				for (int x = 0; x < k; x++) {
					if (a[s[i].second][x] >= a[s[j].second][x]) {
						ok = false;
						break;
					}
				}
				if (ok) g[i][j] = 1;
			}
		}

		memset(p, 0xff, sizeof(p));
		int ans = 0;
		for (int i = 0; i < n; i++) {
			memset(v, 0, sizeof(v));
			if (find(i))
				ans++;
		}
		fout << n - ans << endl;
	}
	return 0;
}
