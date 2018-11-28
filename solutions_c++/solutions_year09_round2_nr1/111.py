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

char s[1000000];
int len;

vs v;

double go(int pos, double x) {
	//cout << pos << ' ' << x << endl;
	while (s[pos] == ' ')
		pos++;
	pos++;
	int p1 = pos;
	int g = 0;
	while (s[p1] != ')') {
		if (isalpha(s[p1]))
			g = 1;
		p1++;
	}

	double pr;

	if (g == 0) {
		sscanf(s + pos, "%lf", &pr);
		re x * pr;
	}
	else {
		char u[100];
		sscanf(s + pos, "%lf%s", &pr, u);
		string ss = u;
		while (s[pos] != '(')
			pos++;
		if (binary_search(all(v), ss))
			re go(pos, x * pr);
		else {
			int z = 1;
			pos++;
			while (z != 0) {
				if (s[pos] == '(') {
					z++;
				}
				if (s[pos] == ')') {
					z--;
				}
				pos++;
			}
			re go(pos, x * pr);
		}
	}
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tCount;
	cin >> tCount;
	rep(test, tCount) {
		cout << "Case #" << test + 1 << ":" << endl;

		len = 0;
		cin >> m;
		gets(s);
		rep(i, m) {
			char str[1000];
			gets(str);
			int l = strlen(str);
			rep(j, l) {
				s[j + len] = str[j];
			}
			len += l + 1;
			s[len - 1] = ' ';
		}
		s[len] = 0;
		//cout << s << endl;
		cin >> n;
		rep(i, n) {
			v.clear();
			string tmp;
			cin >> tmp;
			int a;
			cin >> a;
			rep(j, a) {
				string u;
				cin >> u;
				v.pb(u);
			}
			sort(all(v));
			printf("%.7lf\n", go(0, 1));
		}
	}

	return 0;
}
