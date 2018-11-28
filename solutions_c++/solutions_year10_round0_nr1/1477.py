#include <stdio.h>

int N, K, T;

int main(){
	int two[31];

	FILE *fin = fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	two[0]=1;
	for(int i=1;i<=30;i++)
		two[i]=two[i-1]*2;
	
	fscanf(fin,"%d",&T);
	for(int i=1;i<=T;i++){
		fscanf(fin,"%d%d",&N,&K);
		int temp = K%two[N];
		int flag=0;
		for(int j=N;j>=1;j--){
			K%=two[j];
			if(K<two[j-1]){
				flag=1;
				break;
			}
		}

		if(flag==1)
			fprintf(fout,"Case #%d: OFF\n", i);
		else
			fprintf(fout,"Case #%d: ON\n",i);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
