#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int ans[1005][105];
#define INF 1000000000

int main ()
{
	int test, tests;
	char buf[1000];
	cin >> tests;
	for (test = 1; test <= tests; ++test) {
		int i, s, q, j, k;

		cin >> s;
		cin.getline(buf, 1000);

		map<string,int> names;
		vector<int> Q;

		for (i = 0; i < s; ++i) {
			cin.getline(buf, 1000);
			names[(string)buf] = i;
		}

		cin >> q;
		cin.getline(buf, 1000);

		for (i = 0; i < q; ++i) {
			cin.getline(buf, 1000);
			Q.push_back(names[(string)buf]);
		}

		memset(ans, 0, sizeof(ans));

		int Ans = INF;

		if (q > 0) {

		ans[0][Q[0]] = INF;
		for (i = 1; i < q; ++i)
			for (j = 0; j < s; ++j) {
				ans[i][j] = INF;
				if (Q[i] != j)
					ans[i][j] = ans[i-1][j];
				for (k = 0; k < s; ++k)
					if (k != j && ans[i-1][k] + 1 < ans[i][j])
						ans[i][j] = ans[i-1][k] + 1;
			}

		
		for (i = 0; i < s; ++i)
			Ans = min(Ans, ans[q-1][i]);
		}
		else
			Ans = 0;

		cout << "Case #" << test << ": " << Ans << endl;
	}
	return 0;
};