#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

struct Animal
{
	int h;
	int w;
	bool is_bird;
};

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int n;
		cin >> n;

		vector<Animal> a(n);

		for(int i = 0; i < n; i++) {
			string s;
			cin >> a[i].h >> a[i].w >> s;
			a[i].is_bird = (s == "BIRD");
			if(s == "NOT") { cin >> s; /* "BIRD" */ }
		}

		int m;
		cin >> m;

		cout << "Case #" << iCase << ":" << endl;

		for(int i = 0; i < m; i++) {
			int h, w;
			cin >> h >> w;

			int hmin = INT_MAX;
			int hmax = INT_MIN;
			int wmin = INT_MAX;
			int wmax = INT_MIN;

			for(int j = 0; j < n; j++) {
				if(!a[j].is_bird) { continue; }
				hmin = min(hmin, a[j].h);
				hmax = max(hmax, a[j].h);
				wmin = min(wmin, a[j].w);
				wmax = max(wmax, a[j].w);
			}

			if(hmin <= h && h <= hmax && wmin <= w && w <= wmax) {
				cout << "BIRD" << endl;
				continue;
			}

			bool nonbird = false;

			for(int j = 0; j < n; j++) {
				if(a[j].is_bird) { continue; }

				bool hbad = false;
				hbad |= (h <= hmin && h <= a[j].h && a[j].h <= hmax);
				hbad |= (h >= hmax && h >= a[j].h && a[j].h >= hmin);
				hbad |= (hmin <= a[j].h && a[j].h <= hmax);

				bool wbad = false;
				wbad |= (w <= wmin && w <= a[j].w && a[j].w <= wmax);
				wbad |= (w >= wmax && w >= a[j].w && a[j].w >= wmin);
				wbad |= (wmin <= a[j].w && a[j].w <= wmax);

				nonbird = hbad & wbad;
				if(nonbird) { break; }
			}

			if(nonbird) {
				cout << "NOT BIRD" << endl;
			}
			else {
				cout << "UNKNOWN" << endl;
			}
		}
	}

	return 0;
}
