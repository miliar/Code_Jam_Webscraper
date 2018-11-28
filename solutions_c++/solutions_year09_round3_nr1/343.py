#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <utility>

#define REP(i, a, b) for (typeof(a) i = a; i < b; i++)
#define FOR(i, k) REP(i, 0, k)

#define all(x) x.begin(), x.end()

#define mp make_pair
#define pb push_back

#define watch(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long LL;
typedef pair < int, int > PII;
typedef vector < int > VI;
typedef vector < string > VS;

int dic[260];
string s;

LL mpow(int a, int b){
	if (b == 0) return 1;
	if (b == 1) return a;
	if (b % 2 == 0) return mpow(a, b / 2) * mpow(a, b / 2);
	return a * mpow(a, b - 1);
}

LL g(LL x, int b){
	LL ans = 0;
	int ca = 0;

	//watch(b);

	while (x > 0){
		ans += mpow(b, ca++) * (x % 10);
		//watch(ans); watch(ca);
		x /= 10;
	}

	return ans;
}

int main(){
	int t;
	scanf("%d", &t);

	FOR(tt, t){
		int ndiff = 0;
		int cnt = 1;
		s = "";
		cin >> s;
		//memset(dic, -1, sizeof(dic));
		FOR(i, 260) dic[i] = -1;
		
		FOR(i, (int) s.size()){
			char c = s[i];
			if (dic[c] == -1){
				dic[c] = cnt;
				if (cnt == 1) cnt = 0;
				else if (cnt == 0) cnt = 2;
				else cnt++;
				ndiff++;
			}
		}

		LL ans = 0;
		int ca = 0;

		for (int i = s.size() - 1; i >= 0; i--){
			ans += mpow(10, ca++) * dic[s[i]];
		}

		if (ndiff == 1) ndiff = 2;

		//watch(ndiff);

		printf("Case #%d: %lld\n", tt + 1, g(ans, ndiff));
	}

	return 0;
}
