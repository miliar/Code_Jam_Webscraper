#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>

#include <memory>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

#include <cassert>

#define TASK "A"
#define PB(a) push_back(a)

using namespace std;

typedef long long int64;

int T;
vector <int> got;
char s[64];
bool mem[1000024];

inline int sqr(int a) {
	return a*a;
}

inline bool checkLucky(int k, int base) {
    while (!(k == 1 || mem[k])) {
    	mem[k] = true;

    	int kk = k, sq = 0;

		while (kk > 0) {
			sq += sqr(kk % base);
			kk /= base;
		}

		k = sq;
    }

    return (k == 1);
}
             
int main() {
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif

	scanf("%d\n", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);

		got.clear();

		gets(s);
		int l = strlen(s);
		for (int i = 0; i < l; i++) {
			if (s[i] == '2') got.PB(2);
			if (s[i] == '3') got.PB(3);
			if (s[i] == '4') got.PB(4);
			if (s[i] == '5') got.PB(5);
			if (s[i] == '6') got.PB(6);
			if (s[i] == '7') got.PB(7);
			if (s[i] == '8') got.PB(8);
			if (s[i] == '9') got.PB(9);
			if (s[i] == '1') got.PB(10);
		}

		/*for (int b = 0; b < got.size(); b++) {
			a[got[b]][1][1] = true;
		}*/

		//lucky.clear();
		for (int b = 0; b < got.size(); b++) { cerr << got[b] << " ";}
		cerr << endl;

		for (int k = 2; k <= 1000000; k++) {
		   	bool isLucky = true;

		   	for (int b = 0; b < got.size(); b++) {
		   		memset(mem, 0, sizeof(mem));
		   		if (!checkLucky(k, got[b])) {
		   			isLucky = false;
		   			break;
		   		}
		   	}

		   	if (isLucky) {
		   		printf("%d", k);
		   		break;
		   	}
		}

		printf("\n");
	}

	return 0;
}

