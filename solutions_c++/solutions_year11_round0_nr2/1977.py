#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <memory.h>
#include <cstdio>
#include <cstdlib>
        
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = n - 1 ; i >= 0 ; i--)
#define forv(i, a) for (int i = 0; i < (int)(a.size()); i++)
#define forab(i, a, b) for (int i = a; i < (int)(b); i++)
#define fordab(i, a, b) for (int i = b - 1; i >= (int)(a); i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932
#define all(a) a.begin(), a.end()

typedef long long int64;       
typedef long double ld;

bool op[26][26];
int cr[26][26];
string s;
vector<int> a;

int main() { 
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn (q, t) {
		forn (i, 26) {
			forn (j, 26) {
				op[i][j] = false;
			}
		}
		forn (i, 26) {
			forn (j, 26) {
				cr[i][j] = -1;
			}
		}
		int c;
		cin >> c;
		forn (i, c) {
			cin >> s;
			cr[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			cr[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		int d;
		cin >> d;
		forn (i, d) {
			cin >> s;
			op[s[0] - 'A'][s[1] - 'A'] = true;
			op[s[1] - 'A'][s[0] - 'A'] = true;
		}
		a.clear();
		int n;
		cin >> n >> s;
		forn (i, n) {
			a.pb(s[i] - 'A');
			while (a.size() > 1 && cr[a[a.size() - 1]][a[a.size() - 2]] != -1) {
				int x = cr[a[a.size() - 1]][a[a.size() - 2]];
				a.pop_back();
				a.pop_back();
				a.pb(x);
			}
			forv (i, a) {
				if (op[a[a.size() - 1]][a[i]]) {
					a.clear();
					break;
				}
			}
		}
		cout << "Case #" << q + 1 << ": [";
		forn (i, a.size() - 1) {
			cout << char(a[i] + 'A') << ", ";
		}
		if (a.size()) {
			cout << char(a[a.size() - 1] + 'A');
		}
		cout << ']' << endl;
	}
}

