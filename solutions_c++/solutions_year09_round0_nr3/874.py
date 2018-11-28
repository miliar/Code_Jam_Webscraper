#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string.h>
#include <climits>
#include <vector>
#include <queue>
#include <stack>
#include <err.h>
using namespace std;

static const int LMAX = 500;
static const int MOD = 10000;
static const string mes = "welcome to code jam";
static const int MESSIZE = 19;
int cnt[MESSIZE][LMAX];

int
main()
{
	int N, sum;
	int mdown, mup;
	string s;

	cin >> N;
	getline(cin, s); // get rid of '\n'
	for (int cas = 1; cas <= N; cas++) {
		getline(cin, s);

		for (size_t i = 0; i < s.size(); i++) {
			if (s[i] == mes[mes.size() - 1])
				cnt[0][i] = 1;
			else
				cnt[0][i] = 0;
		}
		for (mdown = mes.size() - 2, mup = 1; mdown >= 0; mdown--, mup++) {
			sum = 0;
			for (int i = s.size() - 1; i >= 0; i--) {
				sum = (sum + cnt[mup-1][i]) % MOD;
				if (s[i] == mes[mdown]) {
					cnt[mup][i] = sum;
				} else {
					cnt[mup][i] = 0;
				}
			}
		}

		sum = 0;
		for (size_t i = 0; i < s.size(); i++)
			sum = (sum + cnt[mes.size() - 1][i]) % MOD;

		printf("Case #%d: %04d\n", cas, sum);
	}

	return 0;
}
