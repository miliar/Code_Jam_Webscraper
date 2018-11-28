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

const int inf = (1<<29);
int T, s, p, a[200],n;

int dp[200][200]; //n s

bool puede(int b, bool usa,int p) {
	if (!usa) return (b>= 3*p-2);
	else {
		if (b<2 || b>28) return false;
		return (b>= 3*p-4);		
	}
}

int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	cin >> T;
	
//	cout << puede(22,true,8) << endl;
	forn(rep,T) {
		cin >> n >> s >> p;
		forn(i,n) cin >> a[i];	
		
		dp[0][0] = 0;
		forsn(i,1,s+1) dp[0][i] = -1; 
		
		forsn(i,1,n+1) forn(j,s+1) {
			dp[i][j] = dp[i-1][j];
			if (j>0 && puede(a[i-1],true,p)) dp[i][j]>?= dp[i-1][j-1] + 1;
			if (puede(a[i-1],false,p)) dp[i][j] >?= dp[i-1][j] + 1;
		}
		int ans= 0;
		forn(i,s+1) ans>?= dp[n][i];
		cout << "Case #" << rep+1 << ": "<< ans << endl;
		
	}		
	return 0;
}
