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
#include <cstdlib>
#include <cctype>
#include <stdio.h>
#include <cstdlib>

using namespace std;

ifstream in("1.in");
ofstream out("1.out");

int t;
long long ans, q, b;
char c;
string st, ss = "0123456789qwertyuioplkjhgfdsazxcvbnm";

int main()
{
	in >> t;
	sort(ss.begin(), ss.end());
	getline(in, st);
	for (int tt = 0; tt < t; tt++) {
		out << "Case #" << tt + 1 << ": ";
		getline(in, st);

		map<char, char> M;
		M[st[0]] = '1';
		int k = -1;

		for (int i = 0; i < st.length(); i++) {
			if (M.find(st[i]) == M.end()) {
				k++;
				if (k == 1) k++;
				M[st[i]] = ss[k];
			}
			st[i] = M[st[i]];
		}

		c = '0';
		for (int i = 0; i < st.length(); i++) c = max(c, st[i]);
		b = ss.find(c) + 1;
		q = 1;
		ans = 0;

		for (int i = st.size() - 1; i >= 0; i--) {
			ans += q * ss.find(st[i]);
			q *= b;
		}

		out << ans << endl;
	}

	return 0;
}
