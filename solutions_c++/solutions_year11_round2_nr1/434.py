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

#define MAXN 200

int t,n, g[MAXN][MAXN], numop[MAXN];

double wp[MAXN], owp[MAXN], oowp[MAXN], rpi[MAXN];

int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	cin >> t;
	forn(caso,t) {
		cin >> n;
		forn(i,n) {
			string s; cin >> s;
			forn(j,n) {
				char c = s[j];	
				if (c == '.') g[i][j] = -1;
				else if (c== '1') g[i][j] = 1;
				else g[i][j] = 0;
			}	
		}
		
		
		
		memset(numop,0,sizeof(numop));
		forn(i,n) {
			wp[i] = 0.0;
			forn(j,n) {
				 if (g[i][j]!=-1) numop[i]++;	
				 if (g[i][j] == 1) wp[i]+=1.0;
			}
			wp[i]/=(double)(numop[i]);
		}
		
		forn(i,n) {
			owp[i] = 0.0;
			forn(j,n) if (g[i][j]!=-1)	{
				int winsj = 0;
				forn(k,n) if (k!=i && g[j][k] == 1)	winsj++;
				owp[i] += (double)(winsj)/(double)(numop[j]-1);
			}
			owp[i]/=(double)(numop[i]);
		}
		
		forn(i,n) {
			oowp[i] = 0.0;
			forn(j,n) if (g[i][j]!=-1)	oowp[i]+=owp[j];
			oowp[i]/=(double)(numop[i]);
		}
		
		
		forn(i,n) rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		
		cout << "Case #" << caso+1 << ":" << endl;
		forn(i,n) cout << rpi[i] << endl;
	}

	return 0;
}
