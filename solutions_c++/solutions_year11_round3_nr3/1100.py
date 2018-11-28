#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
 
#define PB        push_back
#define ALL(v)      (v).begin() , (v).end()
#define SZ(v)      ( (int) v.size() )
#define FOR(i, a, b)  for (int i = (a); i < b ; i++)

using namespace std;

int v[1000], T, n, l, h;

int main() {
	scanf("%d", &T);
	FOR(i,0,T) {
		scanf("%d %d %d", &n, &l, &h);
		FOR(j,0,n)
			scanf("%d", &v[j]);
		bool ff = false;
		FOR(j,l,h+1) {
			bool f = true;
			FOR(k,0,n) {
//				printf("%d mod %d =%d\n", v[k], j, v[k]%j);
				if (v[k]%j && j%v[k]) {
					f = false;
					break;
				}
			}
			if (f) {
				printf("Case #%d: %d\n", i+1, j);
				ff = true;
				break;
			}
		}
		if (!ff)
			printf("Case #%d: NO\n", i+1);
	}

	return 0;
}