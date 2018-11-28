#include <stdio.h>


int main(){
	
	FILE *fi,*fo; fi=fopen("B-large.in","r"); fo=fopen("output.out","w");
	int n,m,k,i,j,s,aux,p;
	
	fscanf(fi,"%d",&n);
	for (i=1; i<=n; i++){
		k=0;
		fscanf(fi,"%d%d%d",&m,&s,&p);
		for (j=1; j<=m; j++){	
			fscanf(fi,"%d",&aux);
			if (aux>=p*3-2) k++;
			else
			if (aux>=p*3-4 && s>0 && p>1) {
				k++; s--;
			}
		}
		fprintf(fo,"Case #%d: %d\n",i,k);
	}
	
	return 0;
}
