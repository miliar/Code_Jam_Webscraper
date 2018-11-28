#include<cstdio>
#include<cstdlib>
#include<algorithm>

#define MAXS 50005
#define MAXK 20
#define INFTY 99999

using namespace std;

int main() {
	FILE *fin = fopen("D.in","r"), *fout = fopen("D.out","w");
	int N, K, c[MAXS], P[MAXK], S;
	fscanf(fin,"%d",&N);
	for(int k = 1; k<=N; k++) {
		fscanf(fin,"%d\n",&K);
		for(int i = 0; i<K; i++) P[i]=i;
		S = 0;
		for(int i = 0; 1; i++) {
			char ch;
			fscanf(fin,"%c",&ch);
			c[i]=(int)ch;
			if(c[i]==10) {
				c[i]=-1;
				break;
			} else {
				c[i]-=26;
			}
			S++;
		}
		int ans = INFTY;
		do {
			int lc = -1, nc = -1, size = 0;
			for(int i = 0; i<S; i+=K) {
				for(int j = 0; j<K; j++) {
					nc = c[i+P[j]];
					if(lc != nc) size++;
					lc = nc;
				}
			}
			if(size < ans) ans = size;
		} while(next_permutation(P,P+K));
		fprintf(fout,"Case #%d: %d\n",k,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
