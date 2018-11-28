#include <iostream>
#include <vector>
using namespace std;

#define abs(a) (((a) > 0) ? (a) : (-(a)))
#define min(a, b) (((a) < (b)) ? (a) : (b))

int n;
vector <pair <int, int> > o, b;

int doTest ()
{
	cin >> n;
	o.clear ();
	b.clear ();

	char r;
	for (int i = 0, p; i < n; ++i) {
		cin >> r >> p;
		if (r == 'O') {
			o.push_back (make_pair (p, i + 1));
		} else {
			b.push_back (make_pair (p, i + 1));
		}
	}

	int po = 1, pb = 1, lst = 0, t = 0;
	vector <pair <int, int> >::iterator lo = o.begin (), lb = b.begin ();

	while (lo != o.end () || lb != b.end ()) {
		if (lo != o.end () && lo->second == lst + 1) {
			int tc = abs (lo->first - po) + 1;
			// we move the orange robot
			po = lo->first;
			lst = lo->second;
			lo++;
			//we move the black one too...
			if (lb != b.end ()) {
				if (pb <= lb->first) {
					pb = min (pb + tc, lb->first);
				} else {
					pb = max (pb - tc, lb->first);
				}
			}
			t += tc;
		}
		if (lb != b.end () && lb->second == lst + 1) {
			int tc = abs (lb->first - pb) + 1;
			// we move the black robot
			pb = lb->first;
			lst = lb->second;
			lb++;
			//we move the orange one too...
			if (lo != o.end ()) {
				if (po < lo->first) {
					po = min (po + tc, lo->first);
				} else {
					po = max (po - tc, lo->first);
				}
			}
			t += tc;
		}
	}	

	return t;
}

int main ()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": " << doTest () << endl;
	}

	system ("pause");

	return 0;
}
