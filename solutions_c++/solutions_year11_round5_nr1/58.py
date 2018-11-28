#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;


vector <pair<int, int> > L, U;
int w, g;
int ln, un;


const long double eps = 1e-9;

void Load()
{
	L.clear();
	U.clear();
	cin >> w >> ln >> un >> g;
	int i;
	for (i = 0; i < ln; i++) {
		int q, w;
		cin >> q >> w;
		L.push_back(make_pair(q,w));
	}
	for (i = 0; i < un; i++) {
		int q, w;
		cin >> q >> w;
		U.push_back(make_pair(q,w));
	}
	sort(L.begin(), L.end());
	sort(U.begin(), U.end());
}






void Solve()
{
	long double area, curarea;
	long double curx = 0;
	long double yu, yl;
	yu = U[0].second;
	yl = L[0].second;
	area = 0;
	int i;
	for (i = 1; i < un; i++) {
		area +=  (U[i].second + U[i-1].second) / (long double)2.0 * (U[i].first - U[i-1].first);
	}
	for (i = 1; i < ln; i++) {
		area -=  (L[i].second + L[i-1].second) / (long double)2.0 * (L[i].first - L[i-1].first);
	}
	area /= g;
	curarea = 0;

	int ll, uu;
	ll = uu = 1;
	while (true) {
		if (g == 1) break;
		long double nxtx;
		long double yu1, yl1;
		
		while (U[uu].first < curx+eps) uu++;
		while (L[ll].first < curx+eps) ll++;

		if (U[uu].first > L[ll].first) {
			nxtx = L[ll].first;
			yl1 = L[ll].second;
			yu1 = yu + (U[uu].second - yu)*(nxtx - curx)/(U[uu].first - curx);
		} else if (U[uu].first < L[ll].first) {
			nxtx = U[uu].first;
			yu1 = U[uu].second;
			yl1 = yl + (L[ll].second - yl)*(nxtx - curx)/(L[ll].first - curx);
		} else {
			nxtx = U[uu].first;
			yu1 = U[uu].second;
			yl1 = L[ll].second;
		}
		long double curp;

		curp = (nxtx-curx)*(yu+yu1-yl-yl1)/2.0;

		if (curp + curarea < area + eps) {
			curarea += curp;
		} else {
			long double ll, rr;
			ll = 0;
			rr = 1;
			long double k = (area - curarea) / curp;
			long double h = nxtx - curx;
			long double a = yu - yl;
			long double b = yu1 - yl1;
			for (int zz = 0; zz < 100; zz++) {
				long double mm = (ll + rr)/ 2.0;
				long double ck = (a + a+(b-a)*mm)*h*mm/2.0 + curarea;
				if (ck > area) rr = mm;
				else ll = mm;
			}
			k = (ll + rr) / 2.0;		
			nxtx = curx + (nxtx - curx)*k;
			yu1 = yu + (yu1-yu)*k;
			yl1 = yl + (yl1-yl)*k;
			curp = (nxtx-curx)*(yu+yu1-yl-yl1)/2.0;
			cout << nxtx << "\n";
			curarea = 0;
			g--;
		}
		yu = yu1;
		yl = yl1;
		curx = nxtx;
	}

}

int main()
{
	int nt, tt;
	cin >> nt;
	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(10);
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ":\n";
		Solve();
	}
	return 0;
}
