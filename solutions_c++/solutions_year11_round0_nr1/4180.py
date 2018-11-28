#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <iostream>
using namespace std;

int comp(const void* a, const void* b) { return ( *(int*)a - *(int*)b ); }

int main()
{
//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	freopen("A-small.in","r",stdin); freopen("A-small.out","w",stdout);
//	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
//	freopen("A-small-practice.in","r",stdin); freopen("A-small-practice.out","w",stdout);
//	freopen("A-large-practice.in","r",stdin); freopen("A-large-practice.out","w",stdout);

	int t;
	cin >> t;

	for (int i=0; i<t; i++) {
		int n;
		cin >> n;

		int o[100] = {0}, b[100] = {0};
		int omax = 0, bmax = 0;

		char r; int p;
		char list[100];
		for (int j=0; j<n; j++) {
			cin >> r >> p;
			if (r == 'O') {
				o[omax++] = p;
			}
			else {
				b[bmax++] = p;
			}
			list[j] = r;
		}

		int y=0;
		int oi=0, bi=0, opos=1, bpos=1;
		int d;
		for (int j=0; j<n; j++) {
			if (list[j] == 'O') {
				d = abs(o[oi]-opos)+1;
				opos = o[oi++];
				if (bi<bmax)
					if (bpos < b[bi])
						bpos = (b[bi] < bpos+d) ? b[bi] : bpos+d;
					else if (bpos > b[bi])
						bpos = (b[bi] > bpos-d) ? b[bi] : bpos-d;
			} else {
				d = abs(b[bi]-bpos)+1;
				bpos = b[bi++];
				if (oi<omax)
					if (opos < o[oi])
						opos = (o[oi] < opos+d) ? o[oi] : opos+d;
					else if (opos > o[oi])
						opos = (o[oi] > opos-d) ? o[oi] : opos-d;
			}
			y += d;
		}

		cout << "Case #" << i+1 << ": " << y << endl;
	}

	return 0;
}
