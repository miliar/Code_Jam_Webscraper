#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int nn, nc, nd;
char c[40][4], d[30][3], r[210], s[210];


int main(){
// 	freopen("d:\\B-small-attempt0.in","r",stdin);freopen("d:\\B-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("d:\\B-large.in","r",stdin);freopen("d:\\B-large.out","w",stdout);
	int cse, i, j, k, g=1;
	scanf("%d",&cse);
	while(cse--) {
		scanf("%d",&nc);
		for(i=0; i<nc;++i)scanf("%s", c[i]);
		scanf("%d",&nd);
		for(i=0; i<nd;++i)scanf("%s", d[i]);
		scanf("%d",&nn);
		scanf("%s", s);
		//puts(s);
		int nk = 0;
		memset(r, 0x00, sizeof(r));
		for(i=0;i<nn;++i) {
			for(j=0;j<nk;++j){
				for(k=0;k<nd;++k){
					if(r[j]==d[k][0] && s[i]==d[k][1]) {
						nk = 0;
						goto M;
					}
					else if(r[j]==d[k][1] && s[i]==d[k][0]) {
						nk = 0;
						goto M;
					}
				}
			}
			if(i<nn-1) {
				for(j=0;j<nc;++j){
					if(s[i]==c[j][0] && s[i+1]==c[j][1]) {
						r[nk++] = c[j][2];
						++i;
						goto M;
					}
					else if(s[i]==c[j][1] && s[i+1]==c[j][0]) {
						r[nk++] = c[j][2];
						++i;
						goto M;
					}
				}
			}
			r[nk++] = s[i];
M:          ;
		}
		printf("Case #%d: [",g++);
		if(nk) {
			printf("%c",r[0]);
			for(i=1;i<nk;++i)printf(", %c",r[i]);
		}
		printf("]\n");
	}
	return 0;
}
