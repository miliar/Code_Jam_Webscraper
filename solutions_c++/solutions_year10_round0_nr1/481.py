#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l, ans;
char ss[1000002];

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("output.txt", "w", stdout);

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
/*
	for (n = 1; n <= 10; n++) {
		int start = 0, other;
		map<int, int> M;
		for (i = 0; 1; i++) {
			cout << i << ": ";
			if (M.count(start)) {
				cout << "It was At step " << M[start] << endl;
				break;
			}
			M[start] = i;
			other = start;
			other ^= 1;
			for (j = 0; j+1 < n; j++) 
				if (start&(1<<j)) other ^= (1<<(j+1));
				else break;
			for (j = 0; j < n; j++)
				cout << ((start&(1<<j)) ? 1 : 0);
			start = other;
			cout << endl;
		}
		gets(ss);
	}
	return 0;
*/
	int tt, tn; cin >> tn;
	F1(tt,tn) {
		cin >> n >> k;
		printf("Case #%d: %s\n", tt, (((k+1) % (1<<n)) ? "OFF" : "ON"));
	}
	
	return 0;
}
