#include<cmath>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main() {
	FILE *fin = fopen("D.in","r"), *fout = fopen("D.out","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int t = 1; t<=T; t++) {
		int N;
		fscanf(fin,"%d",&N);
		if(N == 1) {
			int x, y, r;
			fscanf(fin,"%d%d%d",&x,&y,&r);
			fprintf(fout,"Case #%d: %.6f\n",t,(double)r);
		} else if(N == 2) {
			int x1, y1, r1, x2, y2, r2;
			fscanf(fin,"%d%d%d%d%d%d",&x1,&y1,&r1,&x2,&y2,&r2);
			fprintf(fout,"Case #%d: %.6f\n",t,(double)(r1 > r2 ? r1 : r2));
		} else if(N == 3) {
			int x[3], y[3], r[3];
			for(int i = 0; i<3; i++) {
				fscanf(fin,"%d%d%d",&x[i],&y[i],&r[i]);
			}
			double ans = 10000000.;
			for(int i = 0; i<3; i++) {
				if((sqrt((x[i]-x[(i+1)%3])*(x[i]-x[(i+1)%3]) + (y[i]-y[(i+1)%3])*(y[i]-y[(i+1)%3])) + r[i] + r[(i+1)%3])/2. < ans) {
					ans = (sqrt((x[i]-x[(i+1)%3])*(x[i]-x[(i+1)%3]) + (y[i]-y[(i+1)%3])*(y[i]-y[(i+1)%3])) + r[i] + r[(i+1)%3])/2.;
				}
			}
			fprintf(fout,"Case #%d: %.6f\n",t,ans);
		}
	}
}
