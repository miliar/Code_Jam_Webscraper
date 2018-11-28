#include <cstdio>
#include <climits>
#include <cstring>

#include <memory.h>

#define INPUT_FILE "A-small-attempt2.in"

using namespace std;

int ipow(int base,int exp)
{
	int ret=1;
	while(exp-->0) ret*=base;
	return ret;
}

int main()
{
	FILE* fin=fopen(INPUT_FILE,"r");
	char output_file[1024];
	strcpy(output_file,INPUT_FILE);
	strcpy(strrchr(output_file,'.'),".out");
	FILE* fout=fopen(output_file,"w");

	int num_cases;
	fscanf(fin,"%d",&num_cases);
	for(int k=0;k<num_cases;++k)
	{
		int N,PD,PG;
		fscanf(fin,"%d %d %d",&N,&PD,&PG);
		printf("\n");

		if(PG==100)
		{
			if(PD==100) goto possible; else goto broken;
		}
		if(PG==0)
		{
			if(PD==0) goto possible; else goto broken;
		}
		
		int d2=0,d5=0,g2=0,g5=0;
		for(int n=PD;n%2==0;n/=2) ++d2;
		for(int n=PD;n%5==0;n/=5) ++d5;
		for(int n=PG;n%2==0;n/=2) ++g2;
		for(int n=PG;n%5==0;n/=5) ++g5;

		int d=ipow(2,2-d2)*ipow(5,2-d5),wd=d*PD/100;
		int g=ipow(2,2-g2)*ipow(5,2-g5),wg=g*PG/100;

		printf("N=%d, d=%d/%d, d=%d/%d\n",N,wd,d,wg,g);
		bool solved=false;
		for(int D=d;D<=N;D+=d)
		{
			int WD=D*PD/100;
			int k=0;

			int G=(D+g-1)/g*g;
			int WG=G*PG/100;

			printf("D=%d/%d, G(init)=%d/%d, wg=%d, g=%d\n",WD,D,WG,G,wg,g);
			do
			{
				if(WG>=WD && WG-WD<=G-D)
				{
					printf("D=%d/%d, G=%d/%d, G-D=%d/%d\n",WD,D,WG,G,WG-WD,G-D);
					solved=true;
					break;
				}
				if(g==wg) break;
				G+=g;
				WG+=wg;
			} while(1);
			if(solved) break;
		}
		if(solved)
		{
			possible:
			printf("Case #%d: Possible\n",k+1);
			fprintf(fout,"Case #%d: Possible\n",k+1);
		} else {
			broken:
			printf("Case #%d: Broken\n",k+1);
			fprintf(fout,"Case #%d: Broken\n",k+1);
		}
	}
	fclose(fout);
	fclose(fin);
}