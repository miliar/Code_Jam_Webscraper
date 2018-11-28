#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#define sz size()
#define MP make_pair
#define eps (1e-9)
using namespace std;
typedef unsigned long long int64;
int main() {	   
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d", &n);
	string p = "welcome to code jam";
	string s = "";
	getline(cin, s);
	for (int i = 0; i < n; i++) {
		getline(cin, s);
		vector <int> dp(p.size(), 0);
		for (int j = 0; j < s.size(); ++j) {
			for (int k = p.size() - 1; k >= 0; k--) {
				if (s[j] == p[k]) {
					if (k == 0) dp[k] = (dp[k] + 1) % 10000; else dp[k] = (dp[k] + dp[k - 1]) % 10000;
				}
			}
		}
		s = "";
		ostringstream is(s);		
		is << dp[p.size() - 1];
		s = is.str();
		while (s.size() < 4) s = "0" + s;
		printf("Case #%d: ", i + 1);
		cout << s << "\n";
	}
	return 0;
}