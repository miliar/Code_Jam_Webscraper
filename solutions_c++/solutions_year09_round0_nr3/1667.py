#include <stdio.h>
#include <string.h>

const char *wtcj = "welcome to code jam";

static unsigned anno[19][500];

unsigned int welcome(int d, const char *w, const char *obuf, const char *buf) {
	unsigned q = 0;
	if (!*w)
		return 1;
	if (!*buf)
		return 0;
	const char *s = buf;
	while (*s) {
		if (*w ==*s) {
			unsigned &k = (anno[d+1][s+1-obuf]);
			if (k)
				q += k-1;
			else {
			    k = welcome(d+1, w+1, obuf, s+1);
				q += k;
				++k;
			}
		}
		++s;
	}
	return q;
}

int main() {
	char buf[512];
	int n, l, q;
	scanf("%d\n", &n);
	for (int i = 0; i < n; ++i) {
		fgets(buf, sizeof(buf), stdin);
		l = strlen(buf);
		buf[l-1] = '\0';
		memset(anno, 0, sizeof(anno));
		q = welcome(0, wtcj, buf, buf);
		printf ("Case #%d: %04u\n", i+1, q % 10000);
	}

}
