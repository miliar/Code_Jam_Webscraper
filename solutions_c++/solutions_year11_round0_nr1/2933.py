
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)

const int maxn = 100 + 11;

int typ[maxn];
int num[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i, j, n, k, to;
	char tmp;
	cin >> t;
	forn(i, t) {
		cin >> n;
		forn(j, n) {
			cin >> tmp >> num[j];
			typ[j] = (tmp == 'O') ? 0 : 1;
		}
		int i0, i1, ans = 0, v;
		i0 = i1 = 1;
		forn(j, n) {
			if (typ[j] == 0) {
				v = abs(i0 - num[j]) + 1;
				i0 = num[j];
				ans += v;
				for (k = j + 1; k < n && typ[k] == 0; ++k) ;
				if (k != n) {
					if (abs(i1 - num[k]) <= v)
						i1 = num[k];
					else {
						(num[k] > i1) ? i1 += v : i1 -=v;	
					}
				}
			} else {
				v = abs(i1 - num[j]) + 1;
				i1 = num[j];
				ans += v;
				for (k = j + 1; k < n && typ[k] == 1; ++k) ;
				if (k != n) {
					if (abs(i0 - num[k]) <= v)
						i0 = num[k];
					else {
						(num[k] > i0) ? i0 += v : i0 -=v;	
					}
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}