#include <iostream>
#include <algorithm>

using namespace std;

int a[505], b[27], c[27];

int main() {
	freopen("input", "r", stdin);
	int N;
	scanf("%d\n", &N);
	for (int i = 1; i <= N; ++i) {
		string s;
		getline(cin, s);
		memset(a, 0, sizeof(a));
		int kol = 0;
		for (int j = 0; j < s.size(); ++j) {
			if (s[j] == 'w') {
				b[1]++;
			}
			if (s[j] == 'e') {
				b[2] += b[1];
				b[8] += b[7];
				b[16] += b[15];
//				b[1] = 0;
//				b[7] = 0;
//				b[15] = 0;
			}
			if (s[j] == 'l') {
				b[4] += b[2];
				b[3] += b[2];
//				b[2] = 0;
//				b[3] = 0;
			}
			if (s[j] == 'c') {
				b[5] += b[4];
				b[13] += b[12];
//				b[4] = 0;
//				b[12] = 0;
			}
			if (s[j] == 'o') {
			     b[6] += b[5];
			     b[11] += b[10];
			     b[14] += b[13];
//			     b[5] = 0;
//			     b[10] = 0;
//			     b[13] = 0;
			}
			if (s[j] == 'm') {
				b[7] += b[6];
				b[20] += b[19];
//				b[6] = 0;
//				b[19] = 0;
			}
			if (s[j] == ' ') {
				b[9] += b[8];
				b[12] += b[11];
				b[17] += b[16];
//				b[8] = 0;
//				b[11] = 0;
//				b[16] = 0;
			}
			if (s[j] == 't') {
				b[10] += b[9];
//				b[9] = 0;
			}
			if (s[j] == 'd') {
			     b[15] += b[14];
//			     b[14] = 0;
			}
			if (s[j] == 'j') {
				b[18] += b[17];
//				b[17] = 0;
			}
			if (s[j] == 'a') {
				b[19] += b[18];
//				b[18] = 0;
			}
			for (int j = 1; j <= 20; ++j)
				b[j] %= 1000000;
		}
		int res = b[20] % 10000;
		s = "";
		while (res != 0) {
			s = char(res % 10 + '0') + s;
			res /= 10;
		}
		int len = s.size();
		for (int j = 0; j < 4 - len; ++j) s = '0' + s;
		printf("Case #%d: ", i); cout << s << "\n";
		memset(b, 0, sizeof(b));
	}

	return 0;
}
