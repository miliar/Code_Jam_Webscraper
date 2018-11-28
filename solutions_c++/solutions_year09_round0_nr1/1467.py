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


vector<string> dic;
int l,d,n,ind;
string tmp;

int main () {
//	freopen("in.txt","r",stdin);
	
	cin >> l >> d >> n;
	
	forn(i,d) {
		cin >> tmp;
		dic.pb(tmp);
	}
	
//	cout << "klalalala" << endl;
	
	ind = 1;
	forn(rep,n) {
		int total = 0;
		string actual; 
		int check[20][30];
		forn(i,l) forn(j,30) check[i][j] = 0; 
		cin >> actual; 
		int u = 0, v=0;
		while (u<actual.size()) {
			if (actual[u]=='(') {
				u++;
				while (actual[u]!= ')') {
					check[v][actual[u]-'a'] = 1;
					u++;	
				}		
			}	
			else {
				check[v][actual[u]-'a'] = 1;
			}
			v++;
			u++;
		}
		forn(i,d) {
			bool vale = true;
			forn(j,l) {
				if (check[j][dic[i][j] - 'a'] == 0) vale = false;	
			}
			if (vale) total++;
		}
		cout << "Case #" << ind++ << ": " << total << endl;
	}	

	return 0;
}
