#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cassert>
#include <ctime>
#include <map>
#include <set>
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(s) (int)(s).size()
#define mp make_pair

using namespace std;

typedef long long li;
typedef pair<double, double> pt;
int t, n;
int a[2000], b[2000];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> t;
	forn(q, t){
		cin >> n;
		int ans = 0;
		forn(i, n)
			cin >> a[i] >> b[i];
		forn(i, n)
			forn(j, n){
				if(i == j)
					continue;
				if(a[i] < a[j] && b[i] > b[j])
					ans++;
			}
		cout << "Case #" << q + 1 << ": " << ans << endl;
	}
	return 0;
}