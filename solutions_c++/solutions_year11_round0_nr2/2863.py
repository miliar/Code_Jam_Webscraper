#include <iostream>
#include <vector>
using namespace std;

#define SIGMA 128

char red[SIGMA][SIGMA], op[SIGMA][SIGMA];
int inStk[SIGMA];

typedef vector <char>::iterator iter;
vector <char> stk;

void clear ()
{
	if (stk.empty ())
		return;

	char c = *(stk.end () - 1), ok = false;
	for (int j = 'A'; j <= 'Z' && !ok; ++j) {
		if (inStk[j] && op[c][j]) {
			// we've found an opposing pair
			for (iter it = stk.begin (); it != stk.end (); ++it) {
				inStk[*it]--;
			}
			ok = true;
			stk.clear ();
		}
	}
}

void doTest ()
{
	stk.clear ();
	for (int i = 0; i < SIGMA; ++i) {
		inStk[i] = 0;
		for (int j = 0; j < SIGMA; ++j) {
			red[i][j] = 0;
			op[i][j] = 0;
		}
	}
	char buf[200];
	int c, d;
	cin >> c;
	for (int i = 0; i < c; ++i) {
		cin >> buf;
		red[buf[0]][buf[1]] = buf[2];
		red[buf[1]][buf[0]] = buf[2];
	}

	cin >> d;
	for (int i = 0; i < d; ++i) {
		cin >> buf;
		op[buf[0]][buf[1]] = op[buf[1]][buf[0]] = true;
	}

	int n;
	cin >> n >> buf;
	for (int i = 0; i < n; ++i) {
		stk.push_back (buf[i]);
		inStk [buf[i] ] ++;
		while (stk.size () >= 2 && red[*(stk.end () - 1)][*(stk.end () - 2)]) {
			char a = *(stk.end () - 1);
			char b = *(stk.end () - 2);
			inStk[a] --, inStk[b]--;
			stk.erase (stk.end () - 2, stk.end ());
			stk.push_back (red[a][b]);
			inStk[red[a][b]] ++;
		}
		clear ();
	}

	cout << "[";

	if (!stk.empty ()) {
		for (iter it = stk.begin (); it != stk.end () - 1; ++it) {
			cout << *it << ", ";
		}
	
		cout << *(stk.end () - 1);
	}
	cout << "]";
}


int main ()
{
	//freopen ("b.in", "r", stdin);
	//freopen ("b.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		doTest ();
		cout << endl;
	}

	return 0;
}