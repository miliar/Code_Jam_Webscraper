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

#define MAX 55

char m[MAX][MAX];

int main () {
	int T, t = 1;
	
	scanf("%d ", &T);
	while (T--) {
		int r, c;
		
		scanf("%d %d ", &r, &c);
		
		for (int i=0; i < r; i++) {
			gets(m[i]);
		}
		
		bool valid = true;
		
		for (int i=0; i < r; i++) {
			for (int j=0; j < c; j++) {
				
				if (m[i][j] != '#') {
					continue;
				}
				
				if (i == r-1 || j == c-1 || m[i][j+1] != '#' || m[i+1][j] != '#' || m[i+1][j+1] != '#') {
					valid = false;
					goto END;
				}
				
				m[i][j] = m[i+1][j+1] = '/';
				m[i+1][j] = m[i][j+1] = '\\';
			}
		}
		
		END:
		
		printf("Case #%d:\n", t++);
		
		if (!valid) {
			puts("Impossible");
		}
		else {
			for (int i=0; i < r; i++) {
				puts(m[i]);
			}
		}
	}
	
	return 0;
}
