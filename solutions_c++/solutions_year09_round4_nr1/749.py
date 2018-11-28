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

#define MAXN 50

int t, n, a[MAXN][MAXN], lev[MAXN];


int main () {
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	cin >> t;
	forn(rep,t) {
		cin >> n;
		
		char c;	
		bool found[MAXN];
		forn(i,n) found[i] = false;
		
		forn(i,n) {
			forn(j,n) {
				cin >> c;
				if (c == '0') a[i][j] = 0;
				else if (c == '1') {
					a[i][j] = 1;
				}		
			}
		} 
		forn(i,n) for (int j = n-1; j>=0; j--) {
			if (a[i][j] == 1) {
				lev[i] = j;
				found[i] = true;	
				break;
			}	
			
		}
		forn(i,n) if (!found[i]) lev[i] = 0;
		
		int res = 0;
		int fila = 0;
		while (fila<n) {
			int u = fila;
			while (u<n) {
				if (lev[u]<= fila) {
					for(int j = u; j>fila; j--) {
						swap(lev[j],lev[j-1]);	
						res++;
					}	
					break;
				}
				u++;;
			}
			fila++;
		}
		
		cout << "Case #" << rep+1 << ": " << res << endl;
		
		
	}
	
	
	return 0;
}
