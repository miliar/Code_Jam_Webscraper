#include<cstdio>

bool process(int n,int k){
	int p = (1 << n) - 1;
	int f = k - p;
	if(n == 1 && k%2 == 1) return true;
	else if(n==1 && k%2 == 0) return false;

	if(f % (p+1) == 0) return true;
	return false;
}

int main(void){
	int i,T;
	int n,k;
	bool chk;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fin,"%d %d",&n,&k);
		chk = process(n,k);
		if(chk) fprintf(fout,"Case #%d: ON\n",i);
		else fprintf(fout,"Case #%d: OFF\n", i);
	}	
	return 0;
}