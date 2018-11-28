#include <cstdio>
#include <algorithm>

using namespace std;

int cases;
int R,C,A;

int main() {
	FILE * fin=fopen("B.in","r");
	FILE * fout=fopen("B.out","w");
	
	fscanf(fin,"%d ",&cases);
	for(int h=0;h<cases;h++) {
		fscanf(fin,"%d %d %d ",&R,&C,&A);
		fprintf(fout,"Case #%d: ",h+1);
		if (A>R*C) {fprintf(fout,"IMPOSSIBLE\n");continue;}
		bool found=false;
		
		for(int i=0;i<=R && !found;i++) {
			for(int j=0;j<=C;j++) {
				if (i*j==A) {
					fprintf(fout,"0 0 %d 0 0 %d\n",i,j);found=true;break;
				}
			}
		}
		if (found) {continue;}
		
		for(int i=1;i<=R && !found;i++) {
			for(int j=1;j<=C && !found;j++) {
				for(int a=1;a<i && !found;a++) {
					for(int b=1;b<j;b++) {
						if (i*j==A+a*b) {
							fprintf(fout,"0 0 %d %d %d %d\n",i,b,a,j);found=true;break;
						}
					}
				}
			}
		}
		
		if (!found) {fprintf(fout,"IMPOSSIBLE\n");}		
	}

	return 0;
}
