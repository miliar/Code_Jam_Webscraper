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
int m;

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tCount;
	cin >> tCount;
	rep(test, tCount) {
		cout << "Case #" << test + 1 << ":" << ' ';

		string s;
		cin >> s;
		if (next_permutation(all(s))) {
			cout << s << endl;
			continue;
		}
		else {
			s += '0';
			sort(all(s));
			int p = 0;
			while (s[p] == '0')
				p++;
			swap(s[0], s[p]);
			cout << s;
		}

		cout << endl;
	}

	return 0;
}
