#include<cstdio>
#include<cstdlib>

#define MAXD 5005
#define MAXN 505
#define MAXL 16

using namespace std;

bool possible[MAXL][26];
char words[MAXD][MAXL];

int main() {
	FILE *fin = fopen("A.in","r");
	FILE *fout = fopen("A.out","w");
	int L, D, N;
	fscanf(fin,"%d%d%d",&L,&D,&N);
	for(int i = 0; i<D; i++) {
		fscanf(fin,"%s ",words[i]);
	}
	for(int i = 0; i<N; i++) {
		for(int j = 0; j<L; j++) {
			for(int k = 0; k<26; k++) {
				possible[j][k]=0;
			}
		}
		char c;
		for(int j = 0; j<L; j++) {
			fscanf(fin,"%c",&c);
			if(c=='(') {
				fscanf(fin,"%c",&c);
				while(c!=')') {
					possible[j][c-'a']=1;
					fscanf(fin,"%c",&c);
				}
			} else {
				possible[j][c-'a'] = 1;
			}
		}
		fscanf(fin,"%c",&c);
		int ans = 0;
		for(int j = 0; j<D; j++) {
			bool okay = 1;
			for(int k = 0; k<L; k++) {	
				if(!possible[k][words[j][k]-'a']) {
					okay = 0;
					break;
				}
			}
			if(okay) ans++;
		}
		fprintf(fout,"Case #%d: %d\n",i+1,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
