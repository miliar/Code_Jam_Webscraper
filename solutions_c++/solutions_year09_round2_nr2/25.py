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

int main () {
	int n;
	scanf ("%d\n", &n);
	for (int i = 0; i < n; i++) {
		char w[30];
		int x[30];
		scanf ("%s", w);
		int m = 0;
		while (w[m]) {
			x[m] = w[m] - '0';
			m++;
		}
		if (!next_permutation (x, x + m)) {
		        x[m++] = 0;
			sort (x, x + m);
			for (int i = 0; i < m; i++)
				if (x[i] != 0) {
					swap (x[i], x[0]);
					break;
				}
		}
		printf ("Case #%d: ", i + 1);
		for (int i = 0; i < m; i++) printf ("%d", x[i]);
		printf ("\n");
	}
		
}                
