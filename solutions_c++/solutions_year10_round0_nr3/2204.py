#include<stdio.h>
#define INPUT "C-small-attempt0.in"
#define OUTPUT "C-small.out"

int main(void)
{
	int T;
	FILE *fp = fopen(INPUT,"r");
	FILE *out = fopen(OUTPUT,"w");
	fscanf(fp,"%d",&T);
	for (int TT=1; TT<=T;++TT)
	{
		int R,k,N;
		int g[1000];
		fscanf(fp,"%d%d%d",&R,&k,&N);
		//R time runs in a day
		//k people at once:
		//
		// g[i] size of group
		for (int i = 0 ; i < N ; ++i)
			fscanf(fp,"%d",&g[i]);
	
		int V=0;
		int pt=0;
		while (R){
			int _v =0;
			int st=pt;
			while (_v+g[pt]<=k)
			{
				_v += g[pt++];
//				printf("%d ",pt-1);
				if (pt==N) pt=0;
				if (pt == st) break;
			}
			R--;
//			printf("%d\n",_v);
			V+=_v;
		}

		fprintf(out,"Case #%d: ",TT);
			
		fprintf(out,"%d\n",V);
	}
	fclose(out);
	fclose(fp);
	return 0;
}
