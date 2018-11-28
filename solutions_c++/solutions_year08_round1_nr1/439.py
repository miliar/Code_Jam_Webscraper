#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <queue>

#define num(a) ((int)(a)-48)
#define chr(a) ((char)(a+48))

using namespace std;

int main() {
	int nTC;
	int panjang;
	long long v1[1000], v2[1000];
	scanf("%d", &nTC);
	for (int kasus=1; kasus<=nTC; kasus++) {
		scanf("%d", &panjang);
		for (int i=0; i<panjang; i++) {
			scanf("%lld", &v1[i]);
		}
		for (int i=0; i<panjang; i++)
			scanf("%lld", &v2[i]);
		sort(v1, v1+panjang);
		sort(v2, v2+panjang);
		long long hasil=0;
		for (int i=0; i<panjang; i++) {
			hasil=hasil+v1[i]*v2[panjang-1-i];
		}
		printf("Case #%d: %lld\n", kasus, hasil);
	}
	return 0;
}
