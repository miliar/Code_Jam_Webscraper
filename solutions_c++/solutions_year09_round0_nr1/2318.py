#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cstring>
using namespace std;
#define all(c) c.begin(), c.end()

char em[5010][20];
char tm[410];
int l, d, n;

int main() {
	freopen("C:\\in.txt", "r", stdin);
	freopen("C:\\out.txt", "w", stdout);
	scanf("%d %d %d\n", &l, &d, &n);
	for (int i = 0; i < d; ++i)
		gets(em[i]);
	for (int i = 1; i <= n; ++i) {
		gets(tm);
		int res = 0;	
		for (int j = 0; j < d; ++j) {
			bool pl = true;
			for (int k = 0, t = 0; k < l; ++k, ++t) {
				if (tm[t] == '(') {
					bool ok = false;
					while (tm[t++] != ')') {
						if (em[j][k] == tm[t])
							ok = true;
					}
					if (ok == false) {
						pl = false;
						break;
					}
					t--;
					continue;
				}
				if (em[j][k] != tm[t]) { 
					pl = false;
					break;
				}
			}
			if (pl == true)
				res++;
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}


