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

ll f[10010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int N;
		ll L, H;
		scanf("%d %lld %lld", &N, &L, &H);
		for (int j = 0; j < N; j++)
			scanf("%lld", &f[j]);
		int ans = -1;
		for (int j = L; j <= H; j++) {
			for (int k = 0; k < N; k++) {
				if (f[k]%j != 0 && j%f[k] != 0)
					goto NEXT;
			}
			ans = j;
			break;
		NEXT:;
		}

		if (ans == -1)
			printf("Case #%d: NO\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, ans);
	}
}
