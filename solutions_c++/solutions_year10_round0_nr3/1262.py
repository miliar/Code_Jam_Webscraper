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
#include <cstring>
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


tint step[1024];
int used[1024];
int r,k,n,g[1024],t;


int main () {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	cin >> t;
	forn(i,t) {
		cin >> r >> k >> n;
		forn(j,n) cin >> g[j];

		queue<int> q;
		forn(j,n) {
			q.push(g[j]);
			used[j] = -1;
		}

//		bool stop = -1;
//		forn(j,n) if(g[j]>k) stop = j;

		step[0] = 0, used[0] = 0;
		int v = 0, j = 0, first, last;
		while (v<r) {
			v++;
			int left = k;
			step[v] = step[v-1];
			int count = 0;
			while(count<n) {
				int act = q.front();
				if (left>=act) {
					left-=act;
					step[v] += act;
					q.pop(), q.push(act);
					j++; if (j==n) j=0;
					count++;
				} else break;
			}
			if (used[j]!=-1) {
				first = used[j];
				last = v;
				break;
			} else used[j] = v;
		}
//		cout << first << " " << last << endl;
		cout << "Case #" << i+1 << ": ";
		if (v==r) {
			cout << step[v] << endl;
		} else {
			tint res = step[first];
			res += ((tint)(r-first)/(last-first))*(step[last]-step[first]) + step[first+(r-first)%(last-first)]-step[first];
			cout << res << endl;
		}
//		cout << first << " " << last << endl;

//		forn(i,n+1) cout << step[i] << " "; cout << endl;
	}

	return 0;
}
