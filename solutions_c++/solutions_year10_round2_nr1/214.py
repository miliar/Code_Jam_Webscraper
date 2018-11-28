#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>

#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#include <map>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned char byte;
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

typedef pair<int, int> pii;

char buff[256];

int main() {
	int t, tc;
	int i, j, n, m;

	set<string> sp;
	set<string>::iterator it;
	string p;
	
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		int r = 0;
		sp.clear();
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s", buff), sp.insert(buff);
		}
		for (i = 0; i < m; i++) {
			scanf("%s", buff), p = buff;
			while (!p.empty()) {
				it = sp.find(p);
				if (it != sp.end()) break;
				sp.insert(p);
				j = (int) p.find_last_of('/');
				p.erase(j);
				r++;
			}
		}
		printf("Case #%d: %d\n", t, r);
	}
	
	return (0);
} 
