#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {
	FILE *in = fopen("A.in","r");
	FILE *out = fopen("A.out","w");
	int L,D,N,i,j,k,c;
	fscanf(in,"%d%d%d",&L,&D,&N);
	char dict[5000][16];
	for(i=0;i<D;i++) {
		fscanf(in,"%s",dict[i]);
	}
	char curr[1000];
	char poss['z'+1][16];
	
	for(i=0;i<N;i++) {
		c=0;
		fscanf(in,"%s",curr);
		for(j='a';j<='z';j++){
			for(k=0;k<L;k++){
				poss[j][k]=0;
			}
		}
		k=0;
		for(j=0;j<L;j++) {
			if(curr[k]=='(') {
				while(curr[++k]!=')') {
					poss[curr[k]][j]=1;
				}
			}
			else {
				poss[curr[k]][j]=1;
			}
			k++;
		}
		
		for(j=0;j<D;j++) {
			for(k=0;k<L&&poss[dict[j][k]][k];k++);
			if(k==L) c++;
		}
		
		fprintf(out,"Case #%d: %d\n",i+1,c);
	}
	fclose(in);
	fclose(out);
}