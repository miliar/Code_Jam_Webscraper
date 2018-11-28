#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#pragma comment(linker, "/STACK:64000000")

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

double area(int x1, int y1, int x2, int y2) {
	return (double)x1 * y2 - (double)x2 * y1;
}

string solve() {
	int n, m, a;
	scanf("%d%d%d", &n, &m, &a);
	
	for (int x1 = 0; x1 <= n; x1++)
		for (int y1 = 0; y1 <= m; y1++)
			for (int x2 = 0; x2 <= n; x2++)
				for (int y2 = 0; y2 <= m; y2++) 
				{
					if (x1 == 0 && y1 == 0) continue;
					if (x2 == 0 && y2 == 0) continue;
					if (x1 == x2 && y1 == y2) continue;
					if ( fabs( area(x1, y1, x2, y2) - a ) < 1e-9 )
					{
						ostringstream oss;
						oss << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2;
						return oss.str();
					}
				}
	return "IMPOSSIBLE";
}

int main () {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %s\n", T, solve().c_str());
	fclose(stdin); fclose(stdout);
	return 0;
}
