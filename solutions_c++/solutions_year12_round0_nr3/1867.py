#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define debug 1
#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define Rep(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define cp(a) cerr << "(" << #a << "," << a << ") "
#define cen cerr << endl

typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int inf = 0x7fffffff;

const int Size = 1000 * 1000 + 1;
char buffer[Size];

const int size = 10 * 1000 * 1000 + 100;
int dp[size];

int solution(int nTest) {
	printf("Case #%d: ", nTest + 1);
	int a, b;
	scanf("%d%d", &a, &b);
	For(i, 0, size) {
		dp[i] = 0;
	}
	vector<int> d;
	vector<int> db;
	while(a) {
		d.pb(a % 10);
		a /= 10;
	}
	while(b) {
		db.pb(b % 10);
		b /= 10;
	}
	while(true) {
		vector<int> less = d;
		For(i, 0, sz(d)) {
			int flag = 0;
			For(j, 0, sz(d)) {
				int t = i + j;
				if(t >= sz(d)) {
					t -= sz(d);
				}
				if(d[t] > less[j]) {
					flag = 1;
					break;
				}
				else if(d[t] < less[j]) {
					break;
				}
			}
			if(flag) {
				For(j, 0, sz(d)) {
					int t = i + j;
					if(t >= sz(d)) {
						t -= sz(d);
					}
					less[j] = d[t];
				}
			}
		}
		int res = 0;
		int p = 1;
		For(i, 0, sz(less)) {
			res = res + p * less[i];
			p *= 10;
		}

		dp[res]++;


		int flag = 0;
		For(i, 0, sz(d)) {
			if(d[i] != db[i]) {
				flag = 1;
				break;
			}
		}
		if(flag == 0) {
			break;
		}
		int i = 0;
		do {
			d[i]++;
			if(d[i] >= 10) {
				d[i] = 0;
				i++;
			}
			else {
				break;
			}
		}
		while(true);
	}
	lint res = 0;
	For(i, 0, size) {
		res += dp[i] * (dp[i] - 1) / 2;
	}
	cout << res << endl;





	return 1;
}

int main() {
	if(debug) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}


	int i = 0, n = 99999;
	scanf("%d", &n);
	while(i < n && solution(i)) {
		i++;
	}

	return 0;
}
