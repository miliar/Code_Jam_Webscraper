#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "deque"
using namespace std;
typedef long long i64;

char table[] = {
//	 a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
	'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'
};

int main() {
	int T; scanf("%d", &T);
	char G[128];
	fgets(G,128,stdin);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		fgets(G,128,stdin);
		char *p=G;
		while(*p!=0) {
			if ('a' <= *p && *p <= 'z') {
				*p = table[*p - 'a'];
			}
			++p;
		}

		printf("Case #%d: %s", Ti, G);
	}
	return 0;
}
