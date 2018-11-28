#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int a[1000100];

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int L, N, C;
		ll t;
		scanf("%d %lld %d %d", &L, &t, &N, &C);
		int aa[1010];
		for (int j = 0; j < C; j++) {
			scanf("%d", &aa[j]);
		}
		for (int j = 0; j < N; j++) {
			a[j] = aa[j % C];
		}
		double s, b1, b2;
		double ans = (ll)1 << 59;
		for (int j = 0; j < N; j++) {
			for (int k = (L==0 || L==1 ? 0 : j+1); k < N; k++) {
				if (L == 0)
					j = N, k = N;
				if (L == 1)
					k = N;
				s = 0.0;
				b1 = -1;
				b2 = -1;
				//printf("j=%d k=%d\n", j, k);
				for (int l = 0; l < N; l++) {
					b1 = -1;
					if (l == j || l == k)
						b1 = t;
					double z = s + aa[l % C] * 2.0;
					if (b1 != -1) {
						if (z > b1) {
							if (b1 > s)
								z = b1 + (aa[l%C] - (b1-s)*.5);
							else
								z = s + aa[l%C];
							b1 = -1;
						}
					}
					s = z;
					//printf("%g ", s);
				}
				//printf("\n");
				ans = min(ans, s);
			}
		}

		printf("Case #%d: %lld\n", i+1, (ll)(ans+0.0000001));
	}
}
