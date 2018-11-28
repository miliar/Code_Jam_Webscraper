#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int L, D, N;
string words[5000];

void read_data()
{
	cin >> L >> D >> N;

	for (int i = 0; i < D; ++i)
		cin >> words[i];
}

void solve()
{
	for (int i = 0; i < N; ++i) {
		string cur;
		cin >> cur;
		int res = 0;

		for (int j = 0; j < D; ++j) {
			int p = 0;
			bool good1 = true;

			for (int k = 0; k < L; ++k) {
				bool good2 = false;

				if (cur[p] != '(') {
					if (cur[p] != words[j][k]) { good1 = false; break; }
				} else {
					while (cur[++p] != ')')
						if (cur[p] == words[j][k]) good2 = true;

					if (!good2) { good1 = false; break; }
				}
			
				++p;
			}

			if (good1) ++res;
		}

		cout << "Case #" << i+1 << ": " << res << endl;
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
