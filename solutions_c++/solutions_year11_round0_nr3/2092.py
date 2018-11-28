#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <memory.h>
#include <cstdio>
#include <cstdlib>
        
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = n - 1 ; i >= 0 ; i--)
#define forv(i, a) for (int i = 0; i < (int)(a.size()); i++)
#define forab(i, a, b) for (int i = a; i < (int)(b); i++)
#define fordab(i, a, b) for (int i = b - 1; i >= (int)(a); i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932
#define all(a) a.begin(), a.end()

typedef long long int64;       
typedef long double ld;

vector<int> a;

int main() { 
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn (q, t) {
		int n;
		cin >> n;
		a.clear();
		a.resize(n);
		int x = 0, sum = 0, mn = 10000000;
		forn (i, n) {
			cin >> a[i];
			x ^= a[i];
			sum += a[i];
			mn = min(a[i], mn);
		}
		cout << "Case #" << q + 1 << ": ";
		if (x) {
			cout << "NO";
		} else {
			cout << sum - mn;
		}
		cout << endl;
	}
}
