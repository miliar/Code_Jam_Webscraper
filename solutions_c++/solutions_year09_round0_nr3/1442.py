#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream cin("C-large.in");
	ofstream cout("file.out");
	
	string str = "welcome to code jam";
	int N;
	cin >> N;
	string cur;
	getline(cin, cur);
	for (int i = 0; i < N; ++i) {
		getline(cin, cur);
		int S = cur.size();
		vector<vector<int> > dp(S+1, vector<int>(str.size()));

		for (int j = 0; j < S; ++j) {
			dp[j+1][0] = dp[j][0];
			if (cur[j] == str[0])
				dp[j+1][0] += 1;
		}

		for (int j = 1; j < str.size(); ++j) {
			for (int k = 1; k <= S; ++k) {
				dp[k][j] = dp[k-1][j];
				if (cur[k-1] == str[j])
					dp[k][j] += dp[k][j-1];
				dp[k][j] %= 10000;
			}
		}

		cout << "Case #" << i+1 << ": ";
		int result = dp[S][str.size()-1];
		if (result < 10)
			cout << 0;
		if (result < 100)
			cout << 0;
		if (result < 1000)
			cout << 0;
		cout << result << endl;
	}

	return 0;
}
