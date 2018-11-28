#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

int main() {
	int n, a, b, rt;
	cin >> n;
	forn(t, n) {
		map<int, int> sa, sb;
		cin >> rt >> a >> b;
		int h1,m1,h2,m2;
		forn (i, a) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			sa[h1*60+m1] --;
			sb[h2*60+m2+rt] ++;
		}
		forn (i, b) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			sb[h1*60+m1] --;
			sa[h2*60+m2+rt] ++;
		}
		int ma = 0, mb = 0;
		int h = 0;
		forall(it, sa) { h+=it->second; ma = min(h, ma); }
		h = 0;
		forall(it, sb) { h+=it->second; mb = min(h, mb); }
		cout << "Case #" << t+1 << ": " << -ma << " " << -mb << endl;
	}
	return 0;
}
