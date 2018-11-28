#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define re return

#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <ii> vii;

template <class T> T abs(T & a) {
	return a > 0 ? a : -a;
}

template <class T> int sgn(T & a) {
	return a > 0 ? 1 : (a < 0 ? -1 : 0);
}

#ifdef ONLINE_JUDGE
const double M_PI = 2.0 * acos(1.0);
#endif

int a[26][26];
int b[26][26];
int w[26];

int main()
{
	int T;
	cin >> T;
	for (int I = 0; I < T; I++) {
		memset(a, 255, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(w, 0, sizeof(w));
		vector <int> ans;
		int x;
		cin >> x;
		for (int i = 0; i < x; i++) {
			string s;
			cin >> s;
			a[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			a[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		cin >> x;
		for (int i = 0; i < x; i++) {
			string s;
			cin >> s;
			b[s[0] - 'A'][s[1] - 'A'] = b[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		string s;
		cin >> x >> s;
		for (int i = 0; i < x; i++) {
			int c = s[i] - 'A';
			
			if (ans.size() && a[ans.back()][c] >= 0) {
				/*if (I == 2) {
					for (int j = 0; j < (int)ans.size(); j++) cerr << ans[j] << ' '; cerr << endl;
				}*/
				w[ans.back()]--;
				ans[ans.size() - 1] = a[ans.back()][c];
				w[ans.back()]++;
			} else {
				bool sdg = true;
				for (int j = 0; j < 26; j++) if (b[c][j] && w[j]) {
					ans.clear();
					memset(w, 0, sizeof(w));
					sdg = false;
				}
				if (sdg) {
					ans.pb(c);
					w[c]++;
				}
			}
		}
		cout << "Case #" << I + 1 << ": [";
		for (int i = 0; i < (int)ans.size(); i++) {
			cout << (char)(ans[i] + 'A');
			if (i < (int)ans.size() - 1) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
