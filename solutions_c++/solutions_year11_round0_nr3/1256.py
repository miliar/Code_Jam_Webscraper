/*
ID: ahaigh1
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

int c[1010], t, n, m;

int main() { 
	/* int x;
	cout << 20 << endl;
	REP(k, 20) {
		cout << 1000 << endl;
		REP(i, 500) x = rand()%(1<<20), cout << x << " " << (~x & ((1<<20)-1) ) << endl;
	}
	return 0; */

	cin >> t;
	REP(i, t) { 
		int total = 0; m = inf; int sum = 0;
		cin >> n;
		REP(j, n) { cin >> c[j]; total ^= c[j]; sum += c[j]; if (c[j] < m) m = c[j]; }
		if (total == 0) { 
			//any subset is good, so let him have only the smallest element
			//cout << m << " " << sum << endl;
			printf("Case #%d: %d\n",i+1,sum-m);
		} else { 
			//no solutions
			printf("Case #%d: NO\n",i+1);
		}
	}
}