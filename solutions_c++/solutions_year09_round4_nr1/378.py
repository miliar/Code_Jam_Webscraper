#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>
#include <cstring>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define sqr(x) ((x)*(x))
#define For(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,n) For(i,0,n)
#define re return
#define fi first
#define se second
#define y0 y47847892
#define y1 y47824262
#define fill(x, val) memset(x, val, sizeof(x))

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n;
string m[50];

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tCount;
	cin >> tCount;
	rep(test, tCount) {
		cout << "Case #" << test + 1 << ":" << ' ';
		cin >> n;
		rep(i, n)
			cin >> m[i];

		if (0) {
		cout << endl;
		rep(i, n)
			cout << m[i] << endl;
		cout << endl;
		}

		int ans = 0;
		rep(i, n) {
			int f = 1;
			for (int j = i; j < n; j++)
				if (m[j][i] != '0') {
					f = 0;
					break;
				}
			//if (f == 1)
			//	continue;
			for (int j = i; j < n; j++){
				int g = 1;
				for (int k = i + 1; k < n; k++)
					if (m[j][k] == '1') {
						g = 0;
						break;
					}
				if (g == 1) {
					//cout << "g " << j << endl;
					for (int k = j; k > i; k--) {
						swap(m[k], m[k - 1]);
						ans++;
					}
					if (0)
					rep(i, n)
						cout << m[i] << endl;
					break;
				}
			}
		}

		if (0)
		rep(i, n)
			cout << m[i] << endl;

		cout << ans;
		cout << endl;
	}

	return 0;
}
