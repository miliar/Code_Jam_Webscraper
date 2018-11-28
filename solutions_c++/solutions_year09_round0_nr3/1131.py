#include <iostream>
#include <string>
using namespace std;

const int MAX_N = 512;
string w = "welcome to code jam";
string s;
int t;
int opt[64][MAX_N];

int main() {
	cin >> t;
	getline(cin, s);
	for (int ti = 0; ti < t; ti++) {
		getline(cin, s);
		
		int cnt = 0;
		memset(opt, 0, sizeof(opt));
		for (int i = 1; i <= w.length(); i++)
			for (int j = 1; j <= s.length(); j++) {
				if (i == 1) {
					if (w[i-1] == s[j-1])
						opt[i][j] = 1;
				}
				else {
					if (w[i-1] == s[j-1]) {
						for (int k = 1; k < j; k++)
							if (w[i-2] == s[k-1])
								opt[i][j] = (opt[i][j] + opt[i-1][k]) % 10000;
					}
				}
//				if (opt[i][j] > 0)
//					printf("%d, %d: %d\n", i, j, opt[i][j]);
			}
		for (int j = 1; j <= s.length(); j++)
			cnt = (cnt + opt[w.length()][j]) % 10000;
		printf("Case #%d: ", ti+1);
		if (cnt < 10)
			printf("0");
		if (cnt < 100)
			printf("0");
		if (cnt < 1000)
			printf("0");
		printf("%d\n", cnt);
	}
}
