#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>

using namespace std;


int n;
vector <long long> l, d, dp;

void Solve()
{
	cin >> n;
	l.resize(n+1);
	d.resize(n+1);
	dp.resize(n+1);
	int i;
	for (i = 0; i < n; i++) {
		dp[i] = 0;
		cin >> d[i] >> l[i];
	}
	cin >> d[n];
	l[n] = 1;
	dp[0] = d[0];
	dp[n] = 0;

	int j;
	for (i = 0; i < n; i++) {
		long long mx = d[i] + dp[i];
		//cerr << i << " can reach " << mx << "\n";
		for (j = i+1; j <= n && d[j] <= mx; j++) {
			long long cur = min(d[j] - d[i], l[j]);
			if (dp[j] < cur)
				dp[j] = cur;
		}	
	}
	if (dp[n] != 0) cout << "YES\n";
	else cout << "NO\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Solve(); 
	}
	return 0;
}
