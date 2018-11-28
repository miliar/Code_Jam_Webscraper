#include <stdio.h>
#include <string.h>
int buf[512][32];
char line[512];
int wn;
const char *welcome = "welcome to code jam";

int main() {
	wn = strlen(welcome);
	int n;
	FILE *fi = fopen("c.in", "r");
	FILE *fo = fopen("c.out", "w");
	fscanf(fi, "%d", &n);
	fgets(line, 512, fi);
	for (int li=0; li<512; li++)
		buf[li][0] = 1;
	for (int wi=1; wi<32; wi++)
		buf[0][wi] = 0;
	for (int t=0; t<n; t++) {
		fgets(line, 512, fi);
		int ln = strlen(line) - 1;
		for (int wi=1; wi<=wn; wi++) {
			for (int li=1; li<=ln; li++) {
				buf[li][wi] = buf[li-1][wi];
				if (line[li-1]==welcome[wi-1]) {
					buf[li][wi] += buf[li-1][wi-1];
					if (buf[li][wi]>=10000)
						buf[li][wi] -= 10000;
				}
			}
		}
		fprintf(fo, "Case #%d: %04d\n", t+1, buf[ln][wn]);
	}
	fclose(fo);
	fclose(fi);
	return 0;
}
