#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;


typedef pair < int , int > pii;
typedef vector < int > vi;
typedef long long LL;


#define REP(i, a) for (int i = 0; i < a; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define CLEAR(x, val) memset(x, val, sizeof(x))


int tc, n, s, p, req[110];
int memo[110][110][110];


int dp(int id, int sum, int surprising) {
	if (memo[id][sum][surprising] != -1)
		return memo[id][sum][surprising];
	
	if (id == n) {
		if (surprising == s)
			return memo[id][sum][surprising] = sum;
		else
			return memo[id][sum][surprising] = 0;
	}
	
	int tmp = req[id];
	int ans = 0;
	
	FOR(i, 0, 10) {
		FOR(j, i - 2, i + 2) {
			if (j < 0 || j > 10)
				continue;
				
			int k = tmp - (i + j);
			
			
			if (k < 0 || k > 10) continue;
			
			int selisih = max(abs(i - j), max(abs(i - k), abs(j - k)));
			
			if (selisih > 2)
				continue;
				
			int maks = max(i, max(j, k));
			
			if (maks >= p) {
				if (selisih == 2) {
					ans = max(ans, dp(id + 1, sum + 1, surprising + 1));
				}
				else {
					ans = max(ans, dp(id + 1, sum + 1, surprising));
				}
			}
			else {
				if (selisih == 2)
					ans = max(ans, dp(id + 1, sum, surprising + 1));
				else
					ans = max(ans, dp(id + 1, sum, surprising));
			}
		}
	}
	
	return memo[id][sum][surprising] = ans;
}


int main () {
	scanf("%d\n", &tc);
	
	
	FOR(i, 1, tc) {
		scanf("%d %d %d", &n, &s, &p); 
	
		CLEAR(memo, -1);
	
		REP(j, n) {
			scanf("%d", &req[j]);
		}
		
		printf("Case #%d: %d\n", i, dp(0, 0, 0));
	}
}
