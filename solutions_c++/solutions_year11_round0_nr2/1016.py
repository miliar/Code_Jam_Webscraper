#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {

	freopen("input.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;

	for (int e=1; e<=t; e++) {
		int C,D; cin >> C;

		string c[44];
		string d[44];

		for (int i=0; i<C; i++)
			cin >> c[i];
		cin >> D;
		for (int i=0; i<D; i++)
			cin >> d[i];

		int n;
		cin >> n;

		set<char> used;

		string str;

		for (int i=0; i<n; i++) {
			char cur;
			cin >> cur;
			str += cur;
			if (str.size() >= 2) {
				while (str.size() >= 2) {
					char a = str[str.size()-2];
					char b = str[str.size()-1];
					bool find = false;

					for (int u=0; u<C; u++) {
						if (c[u][0] == a && c[u][1] == b || c[u][0] == b && c[u][1] == a) {
							str.erase(--str.end());
							str.erase(--str.end());
							str += c[u][2];
							find = true;
							break;
						}
					}

					if (!find) break;
				}

				used.clear();
				for (int u=0; u<str.size(); u++)
					used.insert(str[u]);

				if (str.size() > 1) {
					for (int u=0; u<D; u++) {
						if (d[u][0] == str[str.size()-1]) {
							if (used.count(d[u][1])) {
								str.clear();
								used.clear();
								break;
							}
						} else if (d[u][1] == str[str.size()-1]) {
							if (used.count(d[u][0])) {
								str.clear();
								used.clear();
								break;
							}
						}
					}
				}
			}
		}				

		printf("Case #%d: [", e);
		if (str.size() == 0) printf("]\n");
		for (int i=0; i<str.size(); i++)
			printf("%c%s", str[i], (i == str.size() - 1) ? "]\n" : ", ");
	}

	return 0;
}