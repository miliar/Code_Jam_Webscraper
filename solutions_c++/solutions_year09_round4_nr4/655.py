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
int c,n;

int x[MAXN], y[MAXN], r[MAXN];

double dist(int a, int b) {
	return sqrt((x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b])*(y[a]-y[b]));
}

int main () {
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	cin >> c;
	forn(rep,c) {
		cin >> n;
		double res = 0.0;
		forn(i,n) {
			cin >> x[i] >> y[i] >> r[i];	
		}
		
		if (n<=2) {
			if (n==1) res = (double) r[0];
			if (n==2) res = (double)max(r[0],r[1]);
			cout << "Case #" << rep+1 << ": " << res << endl;
		}	
		else {
			double tmp =  1<<30;
			tmp<?= max((double)r[0], (dist(1,2) + (double)(r[1]+r[2]) )* 0.5);	
			tmp<?= max((double)r[1], (dist(0,2) + (double)(r[0]+r[2]) )* 0.5);
			tmp<?= max((double)r[2], (dist(1,0) + (double)(r[0]+r[1]) )* 0.5);
			cout << "Case #" << rep+1 << ": " << tmp << endl;
		}
		
	}
	
	
	return 0;
}
