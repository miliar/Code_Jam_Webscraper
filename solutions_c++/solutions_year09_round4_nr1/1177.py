/*
 * main.cpp
 *
 *  Created on: 2009-9-27
 *      Author: delguoqing
 */

#include <cstdio>
#include <algorithm>
using namespace std;
int a[40], b[40], c[40];
char buf[200];
int N;
bool check() {
	for(int i = 0; i < N; ++ i)
		if(b[i] < a[i])
			return false;
	return true;
}
int calc() {
	for(int i = 0; i < N; ++ i)
		c[i] = i;

	int ret = 0;
	for(int i = N - 1; i >= 0; -- i) {
		for(int j = 0; j < N; ++ j)
			if(b[c[j]] == i) {
				ret += i - j;

				int tmp = c[j];
				for(int k = j; k < i; ++ k)
					c[k] = c[k + 1];
				c[i] = tmp;
			}
	}

	return ret;
}
int main() {
	int cases;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf("%d", &cases);
	for(int caseId = 1; caseId <= cases; ++ caseId) {
		scanf("%d", &N);
		memset(a, 0, sizeof(a));
		for(int i = 0; i < N; ++ i) {
			scanf("%s", buf);
			for(int j = N - 1; j >= 0; -- j)
				if(buf[j] == '1') {
					a[i] = j;
					break;
				}
		}
		for(int i = 0; i < N; ++ i)
			b[i] = i;
		int cnt = 0x7fffffff;
		do {
			if(check() == false)
				continue;
			int ret = calc();
			cnt = min(cnt, ret);
		} while(next_permutation(b, b + N));
		printf("Case #%d: %d\n", caseId, cnt);
	}
}
