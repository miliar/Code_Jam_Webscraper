#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int N;
		scanf("%d", &N);
		int c[1010];
		int ps = 0;
		for (int j = 0; j < N; j++) {
			scanf("%d", &c[j]);
			ps ^= c[j];
		}
		if (ps != 0) {
			printf("Case #%d: NO\n", i+1);
			continue;
		}
		sort(c, c+N);
		int s = 0;
		for (int j = 1; j < N; j++)
			s += c[j];
		printf("Case #%d: %d\n", i+1, s);
	}
}
