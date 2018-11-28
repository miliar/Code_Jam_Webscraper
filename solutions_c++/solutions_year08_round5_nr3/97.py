#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

vs L;
int dp[11][1025];

void solveCase(int Case) {
	L.clear();
	int M, N;
	cin >> M >> N;
	fr(i, M) {
		string s;
		cin >> s;
		L.pb(s);
	}
	memset(dp, 0, sizeof(dp));
	for(int R = M - 1; R >= 0; R--) {
		for(int mask = 0; mask < (1 << N); mask++) {
			for(int sit = 0; sit < (1 << N); sit++) {
				bool blogai = false;
				fr(i, N) if(mask & (1 << i)) {
					if(i > 0 && (sit & (1 << (i - 1)))) {
						blogai = true;
						break;
					}
					if(sit & (1 << (i + 1))) {
						blogai = true;
						break;
					}
				}
				fr(i, N) {
					if(sit & (1 << i)) if(L[R][i] == 'x') {
						blogai = true;
						break;
					}
				}
				fr(i, N - 1) {
					if(sit & (1 << i)) if(sit & (1 << (i + 1))) {
						blogai = true;
						break;
					}
				}
				if(blogai) continue;
				int kiek = 0;
				fr(i, N) kiek += (bool)(sit & (1 << i));
				dp[R][mask] >?= kiek + dp[R + 1][sit];
			}
		}
	}
	cout << "Case #" << Case << ": " << dp[0][0] << endl;	
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; test++) solveCase(test);	
	return 0;
}
