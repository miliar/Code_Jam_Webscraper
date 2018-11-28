#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace std;

#ifdef WIN32
//ifstream in("C-small.in");
ifstream in("C-large.in");
#define cin in
//ofstream out("C-small.out");
ofstream out("C-large.out");
#define cout out
#endif

int main()
{
	int T, ca = 0;
	int dp[21][510];
	string line, z = "welcome to code jam";
	for (cin >> T, getline(cin, line); T; --T) {
		getline(cin, line);
		memset(dp, 0, sizeof(dp));

		for (int i = 0; i < z.size(); ++i) {
			for (int j = 0; j < line.size(); ++j) {
				if (line[j] == z[i]) {
					if (i) {
						for (int k = 0; k < j; ++k) {
							if (line[k] == z[i - 1]) {
								dp[i][j] += dp[i - 1][k];
								dp[i][j] %= 10000;
							}
						}
					} else {
						dp[i][j] = 1;
					}
				}
			}
		}

		int ret = 0;
		for (int i = 0; i < line.size(); ++i) {
			ret += dp[z.size() - 1][i];
		}
		ret %= 10000;

		cout << "Case #" << ++ca << ": " << ret/1000<<ret%1000/100<<ret%100/10<<ret%10 << endl;
	}

	return 0;
}
