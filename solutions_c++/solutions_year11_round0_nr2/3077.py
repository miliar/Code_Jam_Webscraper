#include <cstdio>
#include <vector>
using namespace std;

char combine[42][5];
char destroy[42][5];
char input[142];

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int c, d, n;
		scanf("%d", &c);
		for (int i = 0; i < c; ++i) scanf("%s", combine[i]);
		scanf("%d", &d);
		for (int i = 0; i < d; ++i) scanf("%s", destroy[i]);
		scanf("%d %s", &n, input);

		vector<char> v;
		for (int i = 0; i < n; ++i) {
			v.push_back(input[i]);

			// combine
			char a = v[v.size()-1], b = v[v.size()-2];
			for (int j = 0; j < c; ++j) {
				if (a == combine[j][0] && b == combine[j][1]
						|| a == combine[j][1] && b == combine[j][0]) {
					v.pop_back();
					v.pop_back();
					v.push_back(combine[j][2]);
					break;
				}
			}

			// destroy
			a = v[v.size()-1];
			for (int j = 0; j < d; ++j) {
				for (int ii = 0; ii < v.size()-1; ++ii) {
					b = v[ii];
					if (a == destroy[j][0] && b == destroy[j][1]
							|| a == destroy[j][1] && b == destroy[j][0]) {
						v.clear();
						goto end;
					}
				}
			}
			end:;
		}

		printf("Case #%d: [", tt);
		for (int i = 0; i < v.size(); ++i) {
			if (i) printf(", ");
			putchar(v[i]);
		}
		printf("]\n");
	}
}
