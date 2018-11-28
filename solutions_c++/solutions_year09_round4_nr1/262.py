#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define re return
#define fi first
#define se second
#define sqr(x) (x)*(x)
#define sz(x) (x).size ()
#define all(x) x.begin(), x.end ()
#define fill(x,y) std::memset(x,y,sizeof(x))

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vii;
typedef set<int> si;
typedef map<int, int> mii;

template <class T>T abs (T x) { if (x < 0) return -x; else return x; }

int c[100];
char w[100];

int main () {
	int tt;
	scanf ("%d\n", &tt);
	for (int it = 0; it < tt; it++) {
		int n;
		scanf ("%d\n", &n);
		for (int i = 0; i < n; i++) {
			scanf ("%s", w);
			c[i] = 0;
			for (int j = 0; j < n; j++)
				if (w[j] == '1')
					c[i] = j;
		}
		int ans = 0;
		for (int i = 0; i + 1 < n; i++)
			if (c[i] > i) {
				int j = i + 1;
				while (c[j] > i) j++;
				ans += (j - i);
				int t = c[j];
				for (int k = j; k > i; k--) c[k] = c[k - 1];
				c[i] = t;
			}
		printf ("Case #%d: %d\n", it + 1, ans);	
	}
}                
