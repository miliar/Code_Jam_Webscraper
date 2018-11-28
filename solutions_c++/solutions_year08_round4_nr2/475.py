#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

int N, M, A;


void solve(int id) {
	
	

	printf("Case #%d: ", id);

	for (int x1=0; x1<=N; ++x1) {
		for (int y1=0; y1<=M; ++y1) {
			for (int x2=0; x2<N; ++x2)
				for (int y2=0; y2<=M; ++y2) {
					if (abs(x1 * y2 - x2 * y1) == A) {
						printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
						return;
					}
				}
		}
	}

	
	
		printf("IMPOSSIBLE\n");
	
	
	
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	
	int C;
	scanf("%d", &C);
	for (int id=1; id<=C; ++id) {
		scanf("%d %d %d", &N, &M, &A);
		solve(id);
	}
	return 0;
}