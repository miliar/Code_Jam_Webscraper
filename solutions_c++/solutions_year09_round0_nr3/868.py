#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;

vector< vector<long long> > dp;
string line;
string pat = "welcome to code jam";

long long recur(int let, int pos) {
	if(let == 19)
		return 1;
	if(dp[let][pos] != -1)
		return dp[let][pos];
	dp[let][pos] = 0;
	for(int i = pos; i < line.size(); i++)
		if(line[i] == pat[let]) {
			dp[let][pos] += recur(let+1, i+1);
			dp[let][pos] %= 10000;
		}
	return dp[let][pos];
}

int main() {
	int T;
	cin >> T;
	getline(cin, line);
	for(int nacho = 1; nacho <= T; nacho++) {
		getline(cin, line);
		dp = vector< vector<long long> >(20, vector<long long>(line.size()+2, -1));
		cout << "Case #" << nacho << ": " << setw(4) << setfill('0') << recur(0, 0) << endl;
	}
	return 0;
}
