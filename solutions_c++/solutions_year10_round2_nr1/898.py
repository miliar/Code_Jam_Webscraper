#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <queue>
#include <iostream>
#include <cmath>
#include <memory.h>
#include <string>
#include <cstring>
#include <map>
#include <stack>
#include <utility>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;

int main() {
	int jtc;
	scanf("%d", &jtc);
	for (int tc = 0; tc < jtc; tc++) {
		int N, M;
		map <string, bool> catat;
		int i, j;
		scanf("%d %d%*c", &N, &M);
		for (i = 0; i < N; i++) {
			char tmp[120];
			scanf("%s", tmp);
			string tmps;
			tmps = tmp;
			catat[tmps] = true;
			for (j = tmps.size() - 1; j > 0; j--) {
				if (tmps[j] == '/')
					catat[tmps.substr(0, j)] = true;
			}
		}
		int hasil = 0;
		for (i = 0; i < M; i++) {
			char tmp[120];
			scanf("%s", tmp);
			string tmps;
			tmps = tmp;
			if (catat.find(tmps) == catat.end()) {
				//printf("%s\n", tmps.c_str());
				catat[tmps] = true;
				hasil++;
			}
			for (j = tmps.size() - 1; j > 0; j--) {
				if (tmps[j] == '/') {
					string lho = tmps.substr(0, j);
					if (catat.find(lho) == catat.end()) {
						//printf("%s\n", lho.c_str());
						catat[lho] = true;
						hasil++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", tc + 1, hasil);
	}
	return 0;
}
