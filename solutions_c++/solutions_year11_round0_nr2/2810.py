
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)

const int maxc = 26 + 5;

char f[maxc][maxc];
bool anti[maxc][maxc];

bool was[maxc];

vector <char> ans;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	string buf;

	int t, i, k;
	cin >> t;
	forn(i, t) {
		memset(f, '#', sizeof(f));
		memset(anti, false, sizeof(anti));
		ans.clear();
		int c, j;
		cin >> c;
		forn(j, c) {
			cin >> buf;
			f[buf[0] - 'A'][buf[1] - 'A'] = buf[2];
			f[buf[1] - 'A'][buf[0] - 'A'] = buf[2];
		}
		int d;
		cin >> d;
		forn(j, d) {
			cin >> buf;
			anti[buf[0] - 'A'][buf[1] - 'A'] = anti[buf[1] - 'A'][buf[0] - 'A'] = true;
		}
		int n;
		cin >> n;
		cin >> buf;
		forn(j, n) {
			if (!ans.empty() && f[ans.back() - 'A'][buf[j] - 'A'] != '#') {
				char ch = ans.back();
				ans.pop_back();
				ans.push_back(f[ch - 'A'][buf[j] - 'A']);
			} else
				ans.push_back(buf[j]);
			forn(k, (int)ans.size() - 1)
				if (anti[ans[k] - 'A'][ans.back() - 'A']) {
					ans.clear();
					break;
				}
		}


		cout << "Case #" << i + 1 << ": [";
		forn(j, ans.size()) {
			cout << ans[j];
			if (j < ans.size() - 1)
				cout << ", ";
		}
		cout << "]" << endl;
	}

	return 0;
}