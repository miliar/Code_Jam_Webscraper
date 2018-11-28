#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define debug(x) cout << '>' << #x << ':' << x << endl;
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define INF 2123123123
#define EPS 0.0000001
#define vint vector<int>
#define LL long long
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();++X)

using namespace std;

int main() {
	
	int y,n,m;
	cin >> y;
	forn(z,y) {
		cout << "Case #" << z+1 << ": ";
		cin >> n >> m;
		int twopang = 1 << (n);
		m++;
		if (m % twopang == 0) cout << "ON" << endl; else cout << "OFF" << endl;
		}
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









