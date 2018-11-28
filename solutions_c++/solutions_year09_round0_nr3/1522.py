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
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define mod 10000
int n;
char c;

int main () {
	cin >> n;
	vector<char> wcj;
	string s = "welcome to code jam";
	forn(i, s.size()) wcj.pb(s[i]);
	c = getchar();
	forn (rep,n) {
		int exact[32][1024], sump[32][1024];	
		vector<char> word;
		c = getchar();
		while (c!= '\n' && c!= EOF) {
			word.pb(c);
			c = getchar();
		}
		int m = word.size();
		
		forn(j,m) {
			if (word[j] == wcj[0]) exact[0][j] = 1;
			else exact[0][j] = 0;	
		}
		sump[0][0] = exact[0][0];
		forsn(j,1,m) sump[0][j] = sump[0][j-1] + exact[0][j];
		
		forsn(i,1,19) {
			forn(j,m) {
				if (j<i) exact[i][j] = 0;
				else if (word[j] != wcj[i]) exact[i][j] = 0;
				else if (word[j] == wcj[i]) exact[i][j] = sump[i-1][j-1];	
			}		
			sump[i][0] = 0;
			forsn(j,1,m) sump[i][j] = (sump[i][j-1] + exact[i][j])%mod;		
		}
		
		cout << "Case #"<< rep+1 << ": ";
		if (sump[18][m-1]<10) cout << 0;
		if (sump[18][m-1]<100) cout << 0;
		if (sump[18][m-1]<1000) cout << 0;
		cout << sump[18][m-1] << endl;
	}

	return 0;
}
