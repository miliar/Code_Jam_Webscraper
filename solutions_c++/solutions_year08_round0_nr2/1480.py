#include<cstdio>
#include<cstdlib>

#define MAXT 1500

using namespace std;

int rtime(FILE *fin) {
	int h, m;
	fscanf(fin,"%d:%d",&h,&m);
	return 60*h+m;
}

int main() {
	FILE *fin = fopen("B.in","r"), *fout = fopen("B.out","w");
	int N, NA, NB, T, ca, cb, sa, sb, aneed[MAXT], bneed[MAXT], aget[MAXT], bget[MAXT];
	fscanf(fin,"%d",&N);
	for(int k = 1; k<=N; k++) {
		fscanf(fin,"%d%d%d",&T,&NA,&NB);
		for(int i = 0; i<MAXT; i++) {
			aneed[i]=bneed[i]=aget[i]=bget[i]=0;
		}
		ca = cb = sa = sb = 0;
		for(int i = 0; i<NA; i++) {
			int d = rtime(fin);
			int a = rtime(fin);
			aneed[d]++;
			bget[a+T]++;
		}
		for(int i = 0; i<NB; i++) {
			int d = rtime(fin);
			int a = rtime(fin);
			bneed[d]++;
			aget[a+T]++;
		}
		for(int i = 0; i<MAXT; i++) {
			ca += aget[i];
			cb += bget[i];
			while(aneed[i]) {
				if(ca) {
					ca--;
					aneed[i]--;
				} else {
					aneed[i]--;
					sa++;
				}
			}
			while(bneed[i]) {
				if(cb) {
					cb--;
					bneed[i]--;
				} else {
					bneed[i]--;
					sb++;
				}
			}
		}
		fprintf(fout,"Case #%d: %d %d\n",k,sa,sb);
	}
}
