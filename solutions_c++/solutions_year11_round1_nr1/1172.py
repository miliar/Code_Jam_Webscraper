#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define DBG(x) cerr << #x << " = " << (x) << endl

typedef long long tint;



tint tt;
tint n;
tint phoy;
tint ptot;

int mcd(int a,int b) {
	return (a==0)?b:mcd(b%a,a);
}

bool broken(tint a, tint b, tint c, tint d, tint n) {
	if (n < b)
		return true;
	if (c == 0 and a != 0)
		return true;
	if ((d-c) == 0 and (b-a) != 0)
		return true;
	return false;
}

int main() {
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	cin >> tt;
	forn(t,tt) {
		cin >> n >> phoy >> ptot;
		tint m = mcd(phoy,100);
		tint a = phoy/m;
		tint b = 100/m;
		m=mcd(ptot,100);
		tint c = ptot/m;
		tint d = 100/m;
		cout << "Case #" << t+1 << ": ";
		if (broken(a,b,c,d,n))
			cout << "Broken";
		else
			cout << "Possible";
		cout << endl;
	}
}
