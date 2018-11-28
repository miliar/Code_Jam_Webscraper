#include <cstdio>
#include <cstring>

using namespace std;

char cb[33][33], s[1111], ans[1111];
int op[33], ansl;

int main() {
	int t, c, ds=1;
	char a, b, d;
	scanf("%d", &t);
	while(t--) {
		memset(cb, 0, sizeof cb);
		memset(op, 0, sizeof op);
		printf("Case #%d: [", ds++);
		scanf("%d", &c);
		for(int i = 0; i < c; ++i) {
			scanf(" %c%c%c", &a, &b, &d);
			cb[a-'A'][b-'A'] = cb[b-'A'][a-'A'] = d;
		}
		scanf("%d", &c);
		for(int i = 0; i < c; ++i) {
			scanf(" %c%c", &a, &b);
			op[a-'A'] |= 1<<(b-'A');
			op[b-'A'] |= 1<<(a-'A');
		}

		scanf("%*d");
		int opmask = ansl = 0;
		scanf("%s", s);
		for(int j = 0; s[j]; ++j) {
			ans[ansl++] = s[j];
			if (ansl >= 2 and cb[ans[ansl-1]-'A'][ans[ansl-2]-'A'] != 0) {
				ans[ansl-2] = cb[ans[ansl-1]-'A'][ans[ansl-2]-'A'];
				ansl--;
				opmask = 0;
				for(int k = 0; k < ansl; ++k) 
					opmask |= op[ans[k]-'A'];
			} else if ((opmask & (1<<(s[j]-'A'))) != 0) {
				ansl = opmask = 0;
				continue;
			} else
				opmask |= op[s[j]-'A'];
		}
		for(int i = 0; i < ansl-1; ++i)
			printf("%c, ", ans[i]);
		if (ansl)
			printf("%c", ans[ansl-1]);
		puts("]");
	}
	return 0;
}
