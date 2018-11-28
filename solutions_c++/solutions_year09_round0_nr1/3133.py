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

ifstream in("input.txt");
ofstream out("output.txt");

int l, d, n;
string s[5500], st;
bool w[600][20][255];

int main()
{
	in >> l >> d >> n;
	getline(in, s[0]);
	for (int i = 0; i < d; i++) getline(in, s[i]);

	memset(w, 0, sizeof(w));

	for (int i = 0; i < n; i++) {
		getline(in, st);
		int j = 0, k = 0;
		while (k < l) {
			if (st[j] == '(') {
				do {					
					j++;
					w[i][k][int(st[j])] = true;
				} while (st[j] != ')');
				j++;
			}
			else {
				w[i][k][int(st[j])] = true;
				j++;
			}
			k++;
		}
	}
	for (int i = 0; i < n; i++) {
		out << "Case #" << i + 1 << ": ";
		int ans = 0;
		for (int j = 0; j < d; j++) {
			bool flag = true;
			for (int k = 0; k < l; k++)
				if (!w[i][k][int(s[j][k])]) {flag = false; break;}
			if (flag) ans++;
		}
		out << ans << endl;
	}

	return 0;
}
