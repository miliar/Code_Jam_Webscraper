#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		int r,c;
		cin >> r >> c;
		vector<string> v(r);
		for (int i=0;i<r;++i) cin >> v[i];

		bool ok = 1;
		for (int i=0;i<r;++i) {
			for (int j=0;j<c;++j) {
				if (v[i][j] == '#') {
					if (i + 1 < r && j + 1 < c && v[i+1][j] == '#' && v[i][j+1] == '#' && v[i+1][j+1] == '#') {
						v[i][j] = v[i+1][j+1] = '/';
						v[i+1][j] = v[i][j+1] = '\\';
					} else {
						ok = 0;
					}
				}
			}
		}

		printf("Case #%d:\n", z);
		if (!ok) {
			printf("Impossible\n");
		} else {
			for (int i=0;i<r;++i) {
				for (int j=0;j<c;++j) {
					printf("%c", v[i][j]);
				}
				printf("\n");
			}
		}
	}
}
