#define _WELCOMETOGCJ
#ifdef _WELCOMETOGCJ
// Google Code Jam 2009 - Qualification Round (Welcome to Code Jam)

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

using namespace std;

int dp[551][25];

// welcome to code jam
// 0123456789012345678

string lineR;
string textR = "welcome to code jam";

int calc(int lineIdx, int textIdx) {
	if (textIdx >= textR.size()) return 1;
	if (lineIdx >= lineR.size()) return 0;
	if (dp[lineIdx][textIdx] != -1) return dp[lineIdx][textIdx];
	dp[lineIdx][textIdx] = 0;
	for (int i = lineIdx; i < lineR.size(); i++) {
		if (lineR[i] == textR[textIdx]) {
			dp[lineIdx][textIdx] = (dp[lineIdx][textIdx] + calc(i+1, textIdx+1)) % 10000;
		}
	}
	return dp[lineIdx][textIdx] % 10000;
}

int main() {
	int N;
	cin >> N;
	string dump; getline(cin,dump);
	for (int i = 0; i < N; i++) {
		memset(dp,-1,sizeof(dp));
		string line; getline(cin,line);
		lineR = line;
		int v = calc(0,0);
		ostringstream oss; oss << v;
		string output = oss.str();
		while (output.size() < 4) output = "0" + output;
		cout << "Case #" << (i+1) << ": " << output << "\n";
	}
	return 0;
}
#endif