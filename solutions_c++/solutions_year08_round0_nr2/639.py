#include <cstdio>

#define MAX_TIME 26*60

FILE* in;
int noofCases, T, NA, NB, amax, bmax, atot, btot;
int a[MAX_TIME], b[MAX_TIME];
int main() {
	in = fopen("b.in","r");
	fscanf(in,"%d\n",&noofCases);
	for (int i = 1; i <= noofCases; i++) {
		for (int j = 0; j < MAX_TIME; j++) {a[j] = 0; b[j] = 0;}
		fscanf(in,"%d\n",&T);
		fscanf(in,"%d %d\n",&NA,&NB);
		for (int j = 0; j < NA; j++) {
			int h1, m1, h2, m2;
			fscanf(in,"%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			a[h1*60+m1]++;
			b[h2*60+m2+T]--;
		}
		for (int j = 0; j < NB; j++) {
			int h1, m1, h2, m2;
			fscanf(in,"%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			b[h1*60+m1]++;
			a[h2*60+m2+T]--;
		}
		amax = bmax = atot = btot = 0;
		for (int j = 0; j < MAX_TIME; j++) {
			atot += a[j];
			btot += b[j];
			amax = amax > atot ? amax : atot;
			bmax = bmax > btot ? bmax : btot;
		}
		printf("Case #%d: %d %d\n",i,amax,bmax);
	}
	return 0;
}