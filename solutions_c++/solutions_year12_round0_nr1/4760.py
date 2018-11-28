#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#define eps 1e-8
#define oo 1<<29
#define LL long long

using namespace std;

int T, m, n, q, w, mi, ma, cnt, s, t, fi, cc, e, r, z, x, an;
char c[30] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

char temp[10], a[200];

int main(){
	scanf("%d", &T);
	gets(temp);
	for (int rr = 1; rr <= T; rr++){
		printf("Case #%d: ", rr);
		gets(a);
		for (int j=0; a[j]; j++){
			if (a[j] != ' ')
				printf("%c", c[a[j]-'a']);
			else printf(" ");
		}
		puts("");
	}
	return 0;
}
