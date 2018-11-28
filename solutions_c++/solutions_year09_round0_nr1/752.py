#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double eps = 1e-8;
const double pi = acos(-1.0);

int i, j, k, m, n, l, o;
int ok[1000][1000];
string s[10000], p;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int tt, tn;
	cin >> k >> n >> tn;
	F0(i,n) cin >> s[i];

	
	F1(tt,tn) {
		cin >> p;
		j = 0;
		memset(ok, 0, sizeof(ok));
		F0(i,k) {
			if (p[j] == '(') {
				j++;
				while (p[j] != ')') {
					ok[i][p[j]-'a'] = 1;
					j++;
				}
				j++;
			} else {
				ok[i][p[j]-'a'] = 1;
				j++;
			}
		}
		int ans = 0;
		F0(i,n) {
			int f = 1;
			F0(j,k)
				if (!ok[j][s[i][j]-'a']) f = 0;
			ans += f;
		}
		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}
