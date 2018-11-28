#include<cstdio>
#include<cstdlib>

#define MAXN 45

using namespace std;

int main() {
	FILE *fin = fopen("A.in","r"), *fout = fopen("A.out","w");
	int T, N, a[MAXN];
	fscanf(fin,"%d",&T);
	for(int t = 1; t<=T; t++) {
		fscanf(fin,"%d",&N);
		char s[MAXN];
		for(int i = 0; i<N; i++) {
			fscanf(fin,"%s",s);
			a[i] = -1;
			for(int j = 0; j<N; j++) {
				if(s[j] == '1') a[i] = j;
			}
		}
		int ans = 0;
		for(int i = 0; i<N; i++) {
			for(int j = i; j<N; j++) {
				if(a[j] <= i) {
					for(int k = j; k > i; k--) {
						int t = a[k-1];
						a[k-1] = a[k];
						a[k] = t;
						ans++;
					}
					break;
				}
			}
		}
		fprintf(fout,"Case #%d: %d\n",t,ans);
	}
}
