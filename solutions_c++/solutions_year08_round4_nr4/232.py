#include <cstdio>
#include <algorithm>

using namespace std;


int cases;
char str[50005];
char perm[50005];
int p[9];
int n,k;

int solve() {
	int ret=1;
	for(int i=0;i<n-1;i++) {
		if (perm[i]!=perm[i+1]) {ret++;}
	}
	return ret;
}

int main() {
	FILE * fin=fopen("D.in","r");
	FILE * fout=fopen("D.out","w");
	
	fscanf(fin,"%d ",&cases);
	for(int h=0;h<cases;h++) {
		fscanf(fin,"%d ",&k);
		fscanf(fin,"%s ",str);
		n=strlen(str);
		int ans=n;
		for(int i=0;i<k;i++) {p[i]=i;}
		
		do {
			for(int i=0;i<n;i+=k) {
				for(int j=0;j<k;j++) {
					perm[i+j]=str[i+p[j]];
				}
			}
			ans<?=solve();
		}	while (next_permutation(p,p+k));
		
	
		fprintf(fout,"Case #%d: %d\n",h+1,ans);
	}

	return 0;
}
