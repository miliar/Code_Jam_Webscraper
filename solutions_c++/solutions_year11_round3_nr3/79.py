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
		int N, L, H;
		
		cin >> N >> L >> H;
		
		vector <int> v(N);
		
		for (int i=0; i < N; i++) {
			cin >> v[i];
			assert(v[i] != 0);
		}
		
		int ans = -1;
		
		for (int i=L; i <= H; i++) {
			bool good = true;
			for (int j=0; j < N; j++) {
				if (v[j] % i != 0 && i % v[j] != 0) {
					good = false;
					break;
				}
			}
			if (good) {
				ans = i;
				break;
			}
		}
		
		printf("Case #%d: ", t++);
		if (ans == -1) {
			puts("NO");
		}
		else {
			printf("%d\n",ans);
		}
	}
	
	return 0;
}
