#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

string input = "D-small-attempt0.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

int n, m;
bool mp[12][12];
int e[12][2];

string judge()
{
	int p[12];

	for (int i = 1; i <= n; i++) {
		p[i] = i;
	}
	do {
		bool f = true;
		for (int i = 1; i < m; i++) {
			if (!mp[p[e[i][0]]][p[e[i][1]]]) {
				f = false;
				break;
			}
		}
		if (f) {
			return "YES";
		}
	} while (next_permutation(p + 1, p + n + 1));

	return "NO";
}

int main(void)
{
	int re;
	int a, b;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		ifs >> n;
		memset(mp, 0, sizeof(mp));
		for (int i = 1; i < n; i++) {
			ifs >> a >> b;
			mp[a][b] = mp[b][a] = true;
		}
		ifs >> m;
		for (int i = 1; i < m; i++) {
			ifs >> e[i][0] >> e[i][1];
		}
		// output
		cerr << ri << endl;
		ofs << "Case #" << ri <<": ";
		ofs << judge()  << endl;
	}

	return 0;
}

