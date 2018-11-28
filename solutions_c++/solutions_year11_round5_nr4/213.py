#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;


int t, p;
string s, ans;
bool found;

void analize(string t, int d) {
	if (found) return;
	if (d == si(t))	{
		tint n = 0, pot = 1;
		for(int i = si(t)-1; i>=0; i--) {
			if (t[i] == '1') n+= pot;
			pot*=2;	
		}
		tint m = sqrt(n);
		if (m*m == n || (m+1)*(m+1) == n || (m-1)*(m-1) == n) {
			ans = t;
			found = true;	
		}
	} else {
		if (t[d]!='?') analize(t,d+1);
		else {
			t[d] = '1';
			analize(t,d+1);
			t[d] = '0';
			analize(t,d+1);			
		}
	}
}

int main () {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	cin >> t;
	forn(rep,t) {
		cin >> s;
		found = false;
		analize(s,1);
		cout << "Case #" << rep+1 << ": " << ans << endl;
	}

	return 0;
}
