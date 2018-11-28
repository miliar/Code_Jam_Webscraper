#include <stdio.h>
#include <math.h>
#include <malloc.h>

typedef struct 
{
	unsigned long G;
	float everysum;
	unsigned short nextp;
}Roller,*pRoller;

void main()
{
	unsigned short int times=0;
	FILE *fp_in=fopen("C-small.in","r");
	FILE *fp_out=fopen("C-small.out","w");
	unsigned short int T=0;

	fscanf(fp_in,"%u",&T);
	while(times<T)
	{
		times++;

		unsigned long R=0;
		unsigned long K=0;
		unsigned short N=0;
		fscanf(fp_in,"%lu %lu %u",&R,&K,&N);
		pRoller pr=(pRoller)malloc(N*sizeof(Roller));
		float sum=0.0;
		int i=0;
		pRoller q=pr;
		for(i=0;i<N;i++,q++)
		{
			fscanf(fp_in,"%lu",&(q->G));
			q->everysum=0.0;
			sum += q->G;
		}
		if((sum-K)<0.0001)
		{
			sum=sum*R;
			fprintf(fp_out,"Case #%u: %.0f\n",times,sum);
		}
		else
		{
			sum=0.0;
			q=pr;
			for(i=0;i<N;i++,q++)
			{
				int j=i;
				for(;;)
				{
					q->everysum+=pr[j].G;
					j = (j+1)%N;
					if(K-q->everysum<pr[j].G)
						break;
				}
				q->nextp=j;
			}
			unsigned short firstp=0;  //循环开始位置
			for(i=0;;i=pr[i].nextp)
			{
				firstp=i;
				int m=0,j=i;
				for(;m<N;m++)
				{
					if(pr[j].nextp==firstp) break;
					j=pr[j].nextp;
				}
				if(m!=N) break;
			}
			if(firstp!=0)
			{
				for(i=0;pr[i].nextp!=firstp&&R>1;R--)
				{
					sum+=pr[i].everysum;
					i=pr[i].nextp;
				}
				sum+=pr[i].everysum,R--;
			}

			unsigned short cycle=0;  //循环周期
			float cyclesum=0.0; //循环周期内的和
			for(i=firstp;pr[i].nextp!=firstp;cycle++)
			{
				cyclesum+=pr[i].everysum;
				i=pr[i].nextp;
			}
			cyclesum+=pr[i].everysum,cycle++;


			sum+=cyclesum*((unsigned long)(R/cycle));
			R=R%cycle;
			for(i=firstp;R>0;R--)
			{
				sum+=pr[i].everysum;
				i=pr[i].nextp;
			}

			fprintf(fp_out,"Case #%u: %.0f\n",times,sum);
		}

		free(pr);
	}
	fclose(fp_in);
	fclose(fp_out);
}