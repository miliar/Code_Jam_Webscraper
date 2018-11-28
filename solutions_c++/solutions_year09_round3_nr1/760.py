#include <stdio.h>
#include <string.h>

int main(void){
	char st[100];
	int n,i,j,l;
	long long val[128],v,b,k;
	FILE *fin=fopen("A-large.in","r"), *fout=fopen("out-l.txt","w");

	fscanf(fin,"%d",&n);
	for(i=1;i<=n;++i){
		fscanf(fin,"%s",st);
		for(l='0';l<='9';++l) val[l]=-1;
		for(l='a';l<='z';++l) val[l]=-1;
		k=0;
		l=strlen(st);
		for(j=0;j<l;++j){
			if(val[st[j]]==-1){
				if(k==0) { val[st[j]]=1; k++; }
				else if(k==1) { val[st[j]]=0; k++; }
				else val[st[j]]=k++;
			}
		}
		if(k<2) k=2;
		b=1;
		v=0;
		for(j=1;j<l;++j) b*=k;
		for(j=0;j<l;++j){
			v+=b*val[st[j]];
			b/=k;
		}
		fprintf(fout,"Case #%d: %lld\n", i, v);
	}

	fclose(fin); fclose(fout);

	return 0;
}