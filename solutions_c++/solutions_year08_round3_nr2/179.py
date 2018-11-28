#include <stdio.h>
#include <string.h>

int t, T;
char s[50], *p;
int cnt;
__int64 v;
int sig[50];
int len;

int eval()
{
	char *p;
	__int64 v, res = 0;
	int i, j;
	int sg = 1;

	p = s;
//	if (*p == '-') {
//		sg = -1;
//		p++;
//	}

	v = (__int64)(*p - '0');
	p++;

	i = 0;
	while (i < len-1) {
		if (sig[i] == 0) {
			v = v*10 + (__int64)(*p - '0');
			p++;
			i++;
		} else {
			res += sg * v;
			sg = sig[i];
			v = (__int64)(*p - '0');
			p++;
			i++;
		}
	}
	res += sg * v;

	if (res % 2 == 0 || res % 3 == 0 || res % 5 == 0 || res % 7 == 0) return 1;

	return 0;
}

void srch(int pos)
{
	if (pos == len-1) {
       if (eval() == 1) cnt++;
	   return;
	}

	sig[pos] = -1;
	srch(pos+1);
	sig[pos] = 0;
	srch(pos+1);
	sig[pos] = 1;
	srch(pos+1);

	return;
}

int main() {

	FILE *in = fopen("B-small.in", "rt");
	FILE *out = fopen("B-small.out", "wt");

	//FILE *in = fopen("B-large.in", "rt");
	//FILE *out = fopen("B-large.out", "wt");

	fscanf(in, "%d", &T);

	for (t = 1; t <= T; t++) {
		fscanf(in, "%s", s);

		len = strlen(s);		

		if (len == 1) {
			v = (__int64)(s[0] - '0');
	        if (v % 2 == 0 || v % 3 == 0 || v % 5 == 0 || v % 7 == 0)
				fprintf(out, "Case #%d: %d\n", t, 1);
			else
				fprintf(out, "Case #%d: %d\n", t, 0);
			continue;
		}

		cnt = 0;
		srch(0);

		fprintf(out, "Case #%d: %d\n", t, cnt);
	}

	fclose(in);
	fclose(out);

	return 0;
}