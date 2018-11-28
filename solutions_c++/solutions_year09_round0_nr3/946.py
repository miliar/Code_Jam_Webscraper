#include <algorithm>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int N;
int res[501][20];
string s = "welcome to code jam";

void read_data()
{
	cin >> N;
}

void solve()
{
	int L1 = s.length();
	char temp[502];
	cin.getline(&temp[0], 501);

	for (int i = 0; i < N; ++i) {
		cin.getline(&temp[0], 501);
		string cur = temp;

		int L = cur.length();

		memset(res, 0, sizeof(res));

		for (int j = 0; j <= L; ++j)
			res[j][0] = 1;

		for (int j = 1; j <= L; ++j)
			for (int k = 1; k <= L1; ++k) {
				res[j][k] = res[j-1][k];
				if (cur[j-1] == s[k-1])
					res[j][k] = (res[j][k] + res[j-1][k-1]) % 10000;
			}

		cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) << res[L][L1] << endl;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	read_data();
	solve();

	return 0;
}
