#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

vector<long long> B;
map<pair<int, long long>, long long> dp;

long long cnt(int idx, long long p)
{
	long long ans = 0;
	int i;
	
	if (dp.find(make_pair(idx, p) ) != dp.end() ) return dp[make_pair(idx, p)];
		
	for (i = idx; i < B.size(); i++) {
		if (B[i] > p) {
			ans += cnt(i, B[i]) + 1;
		}
	}
	
	if (ans > 1000000007) ans = ans % 1000000007;
	dp[make_pair(idx, p)] = ans;
	return ans;
}

void calc(int no)
{
	long long i;
	long long n, m, x, y, z;
	long long ans;
	
	cin >> n >> m >> x >> y >> z;
	
	vector<long long> A(m);
	B.resize(n);
	dp.clear();
	
	for (i = 0; i < m; i++) cin >> A[i];
	
	for (i = 0; i < n; i++) {
		B[i] = A[i % m];
		//cout << B[i] << endl;
		A[i % m] = (x * A[i % m] + y * (i + 1) ) % z;
	}
	
	ans = cnt(0, -1);
	
	printf("Case #%d: %llu\n", no, ans % 1000000007ll);
	
	return;
}

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i = 0; i < n; i++) {
		calc(i + 1);
	}
	
	return 0;
}
