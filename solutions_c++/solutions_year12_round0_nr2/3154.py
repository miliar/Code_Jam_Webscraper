#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n, s, p, t, mi, mx, a, res;
bool sup[31], no_sup[31];

int main () {
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++) {
		scanf("%d %d %d", &n, &s, &p);

		for (int a=0; a<=10; a++)
			for (int b=max(0, a-2); b<=min(10, a+2); b++)
				for (int c=max(0, max(a-2, b-2)); c<=min(10, min(a+2, b+2)); c++) {
					mi = min(min(a, b), c);
					mx = max(max(a, b), c);
					if (mx < p)
						continue;
					if (mx - mi == 2)
						sup[a+b+c] = true;
					else
						no_sup[a+b+c] = true;
				}
		for (int i=1; i<=n; i++) {
			scanf("%d", &a);
			if (no_sup[a])
				res++;
			else if (sup[a] && s) {
				s--;
				res++;
			}
		}
		printf("Case #%d: %d\n", tt, res);

		res = 0;
		for (int i=0; i<=30; i++)
			sup[i] = no_sup[i] = false;
	}
}

