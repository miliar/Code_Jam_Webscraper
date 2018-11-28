#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int a[40][40];
int edge[40][40];
int ind[40];
char str[1000];
int main() {
	int T, N, res, tmp, i, j, k;
	scanf("%d", &T);
	int t = 1;
	while (T--) {
		scanf("%d", &N);
		for (i = 0; i < N; i++) {
			scanf("%s", str);
			for (j = 0; j < N; j++) {
				a[i][j] = str[j] - '0';
			}
			for (j = 0; j < N; j++) {
				for (k = j + 1; k < N; k++) {
					if (a[i][k] == 1) break;
				}
				if (k == N) edge[i][j] = 1;
				else edge[i][j] = 0;
				//printf("%d\n",edge[i][j]);
			}
			ind[i] = i;
		}
		res=  10000;
		do {
			for (i = 0; i < N; i++) {
				if (edge[i][ind[i]] == 0) break;
			}
			if (i == N) {
				tmp = 0;
				for (i = 0; i < N; i++) {
					for (j = 0; j < N; j++) {
						if (ind[j] > ind[i] && j < i) tmp++;
					}
				}
				if (tmp < res) {
					res = tmp;
					for (i = 0; i < N; i++) {
				//		printf("%d", ind[i]);
					}	
				//	putchar(10);
				} 
			}
		}while(next_permutation(ind, ind + N));
		printf("Case #%d: %d\n", t++, res);
	}
}
