#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef long double LD;

#define pb push_back
#define mp make_pair
#define sz(A) int((A).size())
#define y1 Y1
#define y2 Y2

const int N = 105;
int sc, n, s, p;

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int cnt = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 0; j < n; j++) {
			scanf("%d", &sc);

    		if (sc >= p + max(p - 1, 0) * 2)
    			cnt++;
    		else {
    			if (s) {
    				if (sc >= p + max(p - 2, 0) * 2) {
    					cnt++;
    					s--;
    				}
    			}
    		}
		}
		printf("Case #%d: %d\n", i + 1, cnt);
	}																																					
	return 0;
}
