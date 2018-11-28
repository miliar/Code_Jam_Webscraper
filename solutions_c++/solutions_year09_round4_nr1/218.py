#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
//#include <cmath>
#include <map>
#include <set>

using namespace std;

int N, res;
string s[40];

void read_data()
{
	cin >> N;
	for (int i = 0; i < N; ++i)
		cin >> s[i];
}

void solve()
{
	res = 0;

	for (int i = 0; i < N; ++i) {
		for (int j = i; j < N; ++j) {
			bool ok = true;
			for (int k = i+1; k < N; ++k)
				if (s[j][k] == '1') { ok = false; break; }

			if (ok) {
				for (int k = j-1; k >= i; --k)
					s[k+1] = s[k];

				res += j-i;
				break;
			}
		}
	}

	cout << res << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		read_data();
		solve();
	}

	return 0;
}
