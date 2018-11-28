#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#define ll long long

using namespace std;

int main() {
    ofstream fout ("2A.out");
    ifstream fin ("2A.in");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		int N;
		fin >> N;
		vector<pair<long long, long long> > vines;
		for (int i = 0; i < N; i++) {
			long long a,b;
			fin >> a >> b;
			vines.push_back(make_pair(a,b));
		}
		long long D;
		fin >> D;
		vines.push_back(make_pair(D,0));
		long long dp[10001];
		memset(dp,-1,sizeof(dp));
		dp[0] = vines[0].first;
		for (int i = 0; i < N; i++) {
			long long maximum = vines[i].first + min(dp[i],vines[i].second);
			for (int j = i+1; j <= N; j++) {
				if (vines[j].first <= maximum) {
					dp[j] = max(dp[j],vines[j].first-vines[i].first);
				}
				else break;
			}
			if (dp[N] != -1) break;
		}
		fout << "Case #" << t << ": ";
		if (dp[N] != -1) fout << "YES" << endl;
		else fout << "NO" << endl;
	}
    return 0;
}