#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 10 * 1000;

int ansx[size], ansy[size];

int main() {
	freopen("problem_b2.in", "r", stdin);
	freopen("problem_b2.out", "w", stdout);
	
	int tc;
	cin >> tc;
	vector <pair <int, int> > h, aput;
	vector <int> xtotry;

	for (int t = 0; t < tc; t++)
	{
		h.clear();
		aput.clear();
		xtotry.clear();
		xtotry.pb(0);
		int n, w, l, r;
		cin >> n >> w >> l;
		for (int i = 0; i < n; i++)
		{
			cin >> r;
			h.pb(mp(r, i));
		}
		sort(h.begin(), h.end());
		int stx = 0;
		int x = stx;
		for (int i = 0; i < n; i++)
		{
			sort(xtotry.begin(), xtotry.end());
			for (int j = 0; j < int(xtotry.size()); j++)
			{
				x = xtotry[j];
				if (x != 0)
					x += h[i].fs;
				int y = 0;
				for (int j = 0; j < int(aput.size()); j++)
					if (aput[j].fs + h[j].fs > x - h[i].fs && aput[j].fs - h[j].fs < x + h[i].fs)
						y = max(y, aput[j].sc + h[j].fs + h[i].fs);
				if (y <= l)
				{
					aput.pb(mp(x, y));
					xtotry.pb(x + h[i].fs);
					break;
				}
			}
			assert(int(xtotry.size()) == i + 2);
		}
		for (int i = 0; i < n; i++)
		{
			ansx[h[i].sc] = aput[i].fs;
			ansy[h[i].sc] = aput[i].sc;
		}
		cout << "Case #" << t + 1 << ":";
		for (int i = 0; i < n; i++)
			cout << " " << ansx[i] << " " << ansy[i];
		cout << endl;
	}

	return 0;
}