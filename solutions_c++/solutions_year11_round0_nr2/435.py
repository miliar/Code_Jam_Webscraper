#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

#include <climits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <string>
#include <bitset>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned char byte;
typedef unsigned short ushort;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int main() {
	int c, t;
	
	scanf("%d", &t);
	for (c = 1; c <= t; c++) {
		int i, j, m;
		map<pii, int> me;
		set<pii> so;
		vector<int> stk;
		scanf("%d", &m);
		for (i = 0; i < m; i++) {
			char e1, e2, er;
			scanf(" %c%c%c", &e1, &e2, &er);
			me[pii(e1, e2)] = er;
			me[pii(e2, e1)] = er;
		}
		scanf("%d", &m);
		for (i = 0; i < m; i++) {
			char e1, e2;
			scanf(" %c%c", &e1, &e2);
			so.insert(pii(e1, e2));
			so.insert(pii(e2, e1));
		}
		scanf("%d", &m);
		for (i = 0; i < m; i++) {
			char e;
			scanf(" %c", &e);
			stk.push_back(e);
			pii t;
			if (stk.size() >= 2)
				t = pii(stk[stk.size() - 1], stk[stk.size() - 2]);
			if (stk.size() >= 2 && me.find(t) != me.end()) {
				stk.pop_back(), stk.pop_back(), stk.push_back(me[t]);
			}
			else {
				for (j = 0; j < (int) stk.size() - 1; j++)
					if (so.find(pii(stk[j], stk[stk.size() - 1])) != so.end())
						stk.clear();
			}
		}
		printf("Case #%d: [", c);
		for (i = 0; i < (int) stk.size(); i++)
			printf("%s%c", (i ? ", " : ""), stk[i]);
		printf("]\n");
	}
	
	return (0);
}
