#include <algorithm>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
using namespace std;

#define MAXLEN 21

int cnt[MAXLEN][10];

string solve(string num) {
	int dcnt[10] = { 0 };
	memset(cnt, 0, sizeof cnt);

	reverse(num.begin(), num.end());
	int len = num.length();

	for (int i = 0; i < len; ++i) {
		int digit = num[i]-'0';

		cnt[i][digit]++;
		if (i > 0)
			for (int j = 0; j < 10; ++j)
				cnt[i][j] += cnt[i-1][j];
	}

	for (int i = 1; i < len; ++i) {
		int digit = num[i]-'0';
		for (int ndigit = digit+1; ndigit < 10; ++ndigit)
			if (cnt[i][ndigit] > 0) {
				cnt[i][ndigit]--;

				num[i] = ndigit + '0';
				for (int j = i-1; j >= 0; --j) {
					for (int k = 0; k < 10; ++k)
						if (cnt[i][k] > 0) {
							cnt[i][k]--;
							num[j] = k + '0';

							break;
						}
				}

				reverse(num.begin(), num.end());
				return num;
			}
	}

	string ret = "";
	int *d = cnt[len-1];
	for (int i = 1; i < 10; ++i)
		if (d[i] > 0) {
			ret += i+'0';
			d[i]--;
			break;
		}
	ret += '0';

	while (1) {
		bool ok = false;

		for (int i = 0; i < 10; ++i) {
			if (d[i] > 0) {
				d[i]--;
				ret += i+'0';

				ok = true;
				break;
			}
		}

		if (!ok)
			break;
	}

	return ret;
}

int main() {
	int n;

	cin >> n;
	for (int tc = 1; tc <= n; ++tc) {
		string num;

		cin >> num;

		int zpos = 0;
		while (num[zpos] == '0')
			zpos++;

		num = num.substr(zpos);

		cout << "Case #" << tc << ": " << solve(num) << endl;
	}

	return EXIT_SUCCESS;
}
