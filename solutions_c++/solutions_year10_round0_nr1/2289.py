#include<stdio.h>
#define INPUT "A-large.in"
#define OUTPUT "A-large.out"

int main(void)
{
	int T;
	FILE *fp = fopen(INPUT,"r");
	FILE *out = fopen(OUTPUT,"w");
	fscanf(fp,"%d",&T);
	for (int TT=1; TT<=T;++TT)
	{
		int n;
		int k,e=1;
		fscanf(fp,"%d%d",&n,&k);
		for (int i = 1; i<=n;++i){
			e*=2;
		}

		while ( k > e){
			k-=e;
		}

		fprintf(out,"Case #%d: ",TT);
			
		if (k== e-1)	fprintf(out,"ON\n");
		else fprintf(out,"OFF\n");
	}
	fclose(out);
	fclose(fp);
	return 0;
}
