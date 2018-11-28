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

const int len = 20;
int em[len][510];
char wel[len] = "welcome to code jam"; 
char str[510];
int main() {
	freopen("C:\\in.txt", "r", stdin);
	freopen("C:\\out.txt", "w", stdout);
	int n;
	scanf("%d\n", &n);
	for (int t = 1; t <= n; ++t) {
		gets(str);
		memset(em, 0, sizeof(em));
		for (int i = 0; str[i] != 0; ++i)
			if (wel[0] == str[i]) {
				if (i - 1 >= 0 && em[0][i - 1])
					em[0][i] += em[0][i - 1] + 1;
				else 
					em[0][i] = 1;
			} else
				if (i - 1 >= 0)
					em[0][i] = em[0][i - 1];
		for (int i = 1; i < len; ++i) {
			for (int j = 0; str[j] != 0; ++j) {
				if (wel[i] == str[j]) {
					if (j - 1 >= 0)
						em[i][j] = (em[i][j - 1] + em[i - 1][j - 1]) % 10000;
				}else
					if (j - 1 >= 0)
						em[i][j] = em[i][j - 1];
			}
		}
		printf("Case #%d: %04d\n", t, em[len - 2][strlen(str) - 1]);
	}
	return 0;
}


