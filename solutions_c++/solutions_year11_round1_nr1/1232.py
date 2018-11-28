#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <gmpxx.h>

using namespace std;
using namespace tr1;

typedef mpz_class number;

int main () {
	int T, t = 1;
	
	cin >> T;
	while (T--) {
		int n, Pd, Pg;
		bool possible = false;
		
		cin >> n >> Pd >> Pg;
		
		if (Pg == 0 || Pg == 100) {
			possible = (Pg == Pd);
			goto END;
		}
		
		for (int d=1; d <= n; d++) {
			if ((d * Pd) % 100 == 0) {
				possible = true;
				break;
			}
		}
		
		END:
		
		printf("Case #%d: %s\n", t++, possible ? "Possible" : "Broken");
	}
	
	return 0;
}
