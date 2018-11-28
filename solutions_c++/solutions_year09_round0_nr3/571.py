#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int dp[500][50];
int M = 10000;

string wel = "welcome to code jam";

int main () {
	int i, j, k, x, n;
	cin >> n;
	string line;
	getline(cin, line);
	for (i=0; i<n; i++) {
		getline(cin, line);
		for (j=0; j<500; j++) {
			for (k=0; k<50; k++) dp[j][k] = 0;
		}
		for (j=0; j<line.size(); j++) {
			if (line[j] == wel[0]) dp[j][0] = 1;
			for (k=1; k<wel.size(); k++) {
				if (line[j] == wel[k]) {
					for (x=0; x<j; x++) {
						dp[j][k] += dp[x][k-1];
						dp[j][k] %= M;
					}
				}
			}
		}
		int ans = 0;
		for (j=0; j<line.size(); j++) {
			ans += dp[j][wel.size()-1];
			ans %= M;
		}
		cout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << ans << endl;
	}
	return 0;
}
