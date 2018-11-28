/*
 * ROUND1B_a.cpp
 *
 *  Created on: 2009-9-12
 *      Author: zhangkai
 */
#include <cstdio>
#include <algorithm>
using namespace std;
int bigInt[30], a[30], l;
int cmp()
{
	for (int i = 0; i < l; ++ i) {
		if (a[i] == bigInt[i])
			continue;
		return a[i] - bigInt[i];
	}
	return 0;
}
int main ()
{
	int t, ca, i;
	char tmp[30];
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	gets(tmp);
	for (ca = 1; ca <= t; ++ ca) {
		gets(tmp);
		for (i = 0; tmp[i]; ++ i) {
			bigInt[i] = tmp[i] - '0';
		}
		l = i;
		for (i = 0; i < l ;++ i)
			a[i] = bigInt[i];
		next_permutation(a, a + l);
		printf("Case #%d: ", ca);
		if (cmp() > 0) {
			for (i = 0; i < l; ++ i)
				printf("%d", a[i]);
			puts("");
		} else {
			for (i = 0; i < l; ++ i)
				if (a[i] > 0)
					break;
			int k = a[0];
			a[0] = a[i];
			a[i] = k;
			printf("%d0", a[0]);
			for (i = 1; i < l; ++ i)
				printf("%d", a[i]);
			puts("");
		}
	}
}
