#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>

#define rep(i, n) repb(i, 0, n)
#define repb(i, b, n) repbc(i, b, n, <)
#define repe(i, n) repbe(i, 0, n)
#define repbe(i, b, n) repbc(i, b, n, <=)
#define repbc(i, b, n, c) for(int i = b; i c n; i++)

#define MAX_SIZE 1030

int main()
{
	int T, P, M[MAX_SIZE], C[MAX_SIZE], res;
	scanf("%i", &T);
	rep(t, T) {
		scanf("%i", &P);
		rep(i, 1 << P) {
			scanf("%i", &M[i]);
		}
		rep(i, P) {
			rep(j, 1 << (P - i - 1)) {
				scanf("%i", &C[i]);
			}
		}
		res = 0;
		rep(i, P) {
			rep(j, 1 << (P - i - 1)) {
				bool found = false;
				rep(k, 1 << (i + 1)) {
					int fk = j * (1 << (i + 1)) + k;
					//printf("(i, j, fk): %i %i %i\n", i, j, fk);
					if(M[fk] == 0) {
						found = true;
					} else {
						M[fk]--;
					}
				}
				if(found) res++;
			}
		}
		printf("Case #%i: %i\n", t + 1, res);
	}
	
  return 0;
}
