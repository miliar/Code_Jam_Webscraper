#include <stdio.h>


int main(){
	
	int N,K,n;
	FILE* f1 = fopen("A.out","w");
	FILE* f2 = fopen("A.in","r");
	fscanf(f2,"%d",&n);
	for(int i=0;i<n;i++)
	{
		fscanf(f2,"%d%d",&N,&K);
		if (K%(1<<N) == ((1<<N)-1)) fprintf(f1,"Case #%d: ON\n",i+1);
		else fprintf(f1,"Case #%d: OFF\n",i+1);
	}
	fclose(f1);

	return 0;
}