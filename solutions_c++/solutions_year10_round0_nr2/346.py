#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;

const int maxn = 1000 + 10;
tint t[maxn];

tint gcd(tint a, tint b){ return (b==0) ? (a) : (gcd(b, a%b)); }

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int NC; cin >> NC;
	forn(nc, NC){
		int n; cin >> n;
		forn(i, n) cin >> t[i];

		tint T = 0;
		forn(i, n-1) T = gcd(T, abs(t[i] - t[i+1]));
		tint r = t[0]%T;

//		cout << T << " " << r << endl;
		cout << "Case #" << nc+1 << ": " << (T-r)%T << endl;
	}

	return 0;
}
