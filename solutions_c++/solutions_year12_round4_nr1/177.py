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

#define MAXN 10100


int l[MAXN],d[MAXN], T, D,n, minwin[MAXN];

int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	cin >> T;	
	forn(rep,T) {
		cin >> n;
		forn(i,n) cin >> d[i] >> l[i];
		cin >> d[n];
		
		l[0]<?= d[0];
		
		forn(i,n) minwin[i] = -1;
		
		minwin[n] = 0;
		for(int i=n-1; i>=0;i--) {
			for(int j = i+1; d[j]-d[i]<= l[i] && j<=n; j++)	{
				if (minwin[j]>-1 && minwin[j]<=min(d[j]-d[i],l[j])) {
					minwin[i] = d[j]-d[i];
					break;	
				}
			}
		}
		cout << "Case #" << rep+1 << ": ";
		if (minwin[0]>-1) cout << "YES" << endl;
		else cout << "NO" << endl;
		
	}

	return 0;
}
