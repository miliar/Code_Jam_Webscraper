#include<cstdio>
#include<cstdlib>

using namespace std;

int main() {
	FILE *fin = fopen("B.in","r"), *fout = fopen("B.out","w");
	int C, A, N, M, x1, x2, y1, y2;
	bool done;
	fscanf(fin,"%d",&C);
	for(int k = 1; k<=C; k++) {
		fscanf(fin,"%d%d%d",&N,&M,&A);
		done = 0;
		for(x1 = 0; x1<=N; x1++) {
			for(y2 = 0; y2<=M; y2++) {
				for(x2 = 1; x2<=N; x2++) {
					y1 = (A+x1*y2)/x2;
					if(y1 >= 0 && y1 <= M && y1*x2 == A+x1*y2) {
						done = 1;
						break;
					}
				}
				if(done) break;
			}
			if(done) break;
		}
		if(!done) {
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",k);
		} else {
			fprintf(fout,"Case #%d: 0 0 %d %d %d %d\n",k,x1,y1,x2,y2);
		}
	}
	fclose(fin); fclose(fout);
	return 0;
}
