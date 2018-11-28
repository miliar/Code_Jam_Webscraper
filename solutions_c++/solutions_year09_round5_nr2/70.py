#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

#define MOD 10009

string word[110];
map<char, int> c[110];
int use[10];
int fact[6] = {1, 1, 2, 6, 24, 120};

int mul(int k) {
	map<int, int> cou;
	for(int i = 0; i < k; ++i) ++cou[use[i]];
	int res = fact[k];
	for(map<int, int>::iterator it = cou.begin(); it != cou.end(); ++it) res /= fact[it->second];
	return res;
}

int calc_sum(int pos, int n, int k, map<char, int>& sum, const string& expr, int prev = 0) {
	if(pos == k) {
		int res = 1;
		for(int i = 0; i < (int)expr.size(); ++i) res = res * sum[expr[i]] % MOD;
		return res * mul(k) % MOD;
	}
	int res = 0;
	for(int i = prev; i < n; ++i) {
		set<char> used;
		for(int j = 0; j < (int)expr.size(); ++j) if(used.insert(expr[j]).second) sum[expr[j]] += c[i][expr[j]];
		use[pos] = i;
		res = (res + calc_sum(pos + 1, n, k, sum, expr, i)) % MOD;
		used.clear();
		for(int j = 0; j < (int)expr.size(); ++j) if(used.insert(expr[j]).second) sum[expr[j]] -= c[i][expr[j]];
	}
	return res;
}

int calc(string expr, int n, int k) {
	map<char, int> m;
	return calc_sum(0, n, k, m, expr);
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		string expr;
		int n, k;
		cin >> expr >> k >> n;
		for(int i = 0; i < n; ++i) cin >> word[i];
		for(int i = 0; i < n; ++i) {
			c[i].clear();
			for(int j = 0; j < (int)word[i].size(); ++j) ++c[i][word[i][j]];
		}
		printf("Case #%d:", t + 1);
		for(int i = 1; i <= k; ++i) {
			string ex = expr;
			int res = 0;
			while(expr.size()) {
				int pos = 0;
				for(; pos < (int)expr.size() && expr[pos] != '+'; ++pos);
				res = (res + calc(expr.substr(0, pos), n, i)) % MOD;
				if(pos != (int)expr.size()) expr = expr.substr(pos + 1);
				else expr = "";
			}
			expr = ex;
			printf(" %d", res);
		}
		puts("");
	}
	return 0;
}
