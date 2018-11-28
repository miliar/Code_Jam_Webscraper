#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<bitset>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps (1e-9)
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int id_round_for_team(int team, int round, int p) {
	if (round == 0)
		return 0;
	int num = (1 << (p - round));
	int teams = (1 << p);
	return (1 << round) - 1 + team / num;
}

int dp[1 << 11][1 << 11];
int number_of_teams;
int p;

int MakeMask(int mask, int team) {
	if (team == number_of_teams - 1)
		return 0;
	int same = 0;
	for (int i = 0; i < p; ++i) {
		int a = ((team >> (p - i - 1)) & 1);
		int b = (((team + 1) >> (p - i - 1)) & 1);
		if (a == b)
			++same;
		else
			break;
	}
	int new_mask = 0;
	for (int i = 0; i < same + 1; ++i) {
		if ((mask >> i) & 1)
			new_mask = new_mask ^ (1 << i);
	}
	return new_mask;
}

int solve(int team, int mask, const vector<int> & prices, const vector<int> & m) {
	if (team == number_of_teams) 
		return 0;
	if (dp[team][mask] >= 0)
		return dp[team][mask];
	int bit_count = 0;
	for (int i = 0; i < p; ++i) {
		if ((mask >> i) & 1)
			++bit_count;
	}
	int miss = p - bit_count;
	int & res = dp[team][mask];
	res = INF;
	if (miss <= m[team]) 
		res = min(res, solve(team + 1, MakeMask(mask, team), prices, m));
	for (int i = 0; i < p; ++i) {
		if (((mask >> i) & 1) == 0) {
			res = min(res, solve(team, mask ^ (1 << i), prices, m) + prices[id_round_for_team(team, i, p)]);
		}
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int C;
	cin >> C;
	for (int test = 0; test < C; ++test) {
		cerr << test << " " ;
		cout << "Case #"<< test + 1 << ": ";
		cin >> p;
		vector<int> m((1 << p), -1);
		for (int i = 0; i < (1 << p); ++i)
			scanf("%d", &m[i]);
		/*for (int k = p - 1; k >= 0; --k) {
			for (int j = 0; j < (1 << k); ++j) {
				int x;			
				scanf("%d", &x);
			}
		}
		set<int> res;
		for (int i = 0; i < (1 << p); ++i) {
			int need = p - m[i];
			for (int j = 0; j < need; ++j) {
				res.insert(id_round_for_team(i, j, p));
			}
		}
		cout << res.size() << "\n";*/
		vector<int> prices((1 << p), -1);
		number_of_teams = (1 << p);
		for (int round = p - 1; round >= 0; --round) {
			for (int j = 0; j < (1 << round); ++j) {
				int x;			
				scanf("%d", &x);
				prices[(1 << round) - 1 + j] = x;
			}
		}
		memset(dp, -1, sizeof(dp));
		cout << solve(0, 0, prices, m) << "\n";
	}
	return 0;
}