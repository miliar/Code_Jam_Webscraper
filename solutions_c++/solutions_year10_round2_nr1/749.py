#include <numeric>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

set<string> S;
int n, m, t, ans, l;
string st, c;

int main()            
{
	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		out << "Case #" << tt + 1 << ": ";
		in >> m >> n;
		ans = 0;
		getline(in, st);
		S.clear();
		for (int i = 0; i < m; ++i) {
			getline(in, st);
			st += "/";
			l = st.length();

			c = "/";
			for (int j = 1; j < l; ++j) {
				c += st[j];
				if (st[j] == '/') S.insert(c);
			}
		}
		for (int i = 0; i < n; ++i) {
			getline(in, st);
			st += "/";
			l = st.length();

			c = "/";
			for (int j = 1; j < l; ++j) {
				c += st[j];
				if (st[j] == '/') {
					if (S.find(c) == S.end()) {
						S.insert(c);
						ans++;
					}
				}
			}
		}
		out << ans << endl;
	}

	return 0;
}
