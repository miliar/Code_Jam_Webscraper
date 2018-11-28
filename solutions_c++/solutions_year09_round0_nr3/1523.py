#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

const string target = "welcome to code jam";

int main() {
	int N;
	cin >> N;
	string line;
	getline(cin, line);
	for (int test_case = 1; test_case <= N; test_case++) {
		getline(cin, line);
		vector<vector<int> > dp;
		dp.resize(line.length());
		for (int i = 0; i < line.length(); i++) {
//cout << line[i] << ":\t";
			dp[i].resize(target.length());
			for (int j = 0; j < target.length(); j++) {
				dp[i][j] = 0;
				if (line[i] == target[j]) {
					if (line[i] == target[0])
						dp[i][j] = 1;
					if (i > 0)
						dp[i][j] += dp[i - 1][j];
					if (i > 0 && j > 0)
						dp[i][j] += dp[i - 1][j - 1];
				}
				else if (i > 0) {
					dp[i][j] = dp[i - 1][j];
				}
				dp[i][j] = dp[i][j] % 10000;
//cout << dp[i][j] << "\t";
			}
//cout << endl;
		}
//cout << endl;
		cout << "Case #" << test_case << ": " << setfill('0') << setw(4) << dp[line.length() - 1][target.length() - 1] << endl;
	}
}
