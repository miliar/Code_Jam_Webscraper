#include<cstdio>
#include<cstdlib>

using namespace std;

int main() {
	FILE *fin = fopen("a.in","r"), *fout = fopen("a.out","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int t = 1; t<=T; t++) {
		int N, K;
		fscanf(fin,"%d%d",&N,&K);
		K++;
		if(!(K & ((1<<N) - 1))) {
			fprintf(fout,"Case #%d: ON\n",t);
		} else {
			fprintf(fout,"Case #%d: OFF\n",t);
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
