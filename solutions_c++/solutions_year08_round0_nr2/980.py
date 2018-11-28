#include <stdio.h>
#define SCHEMAX	200

typedef struct timestructure
{
	int h;
	int m;
} time;

typedef struct schestructure
{
	time departure;
	time arrive;
} schedule;

void minadd(time * a, int min)
{
	a->m += min;

	if(a->m >= 60)
	{
		a->h++;
		a->m -= 60;
	}
}

int compare(time a, time b)
{
	if(a.h > b.h)
		return 1;

	else if(a.h < b.h)
		return -1;

	else
	{
		if(a.m > b.m)
			return 1;

		else if(a.m < b.m)
			return -1;

		else
			return 0;
	}
}

int main()
{
	int N;
	int NA, NB;
	int T;

	schedule sA[SCHEMAX], sB[SCHEMAX];
	time AR[SCHEMAX], BR[SCHEMAX];

	bool AU[SCHEMAX], BU[SCHEMAX];

	int ARCnt = 0, BRCnt = 0;

	int AResult, BResult;

	FILE *fp = fopen("input.txt","r");
	FILE *fp2 = fopen("output.txt","w");

	fscanf(fp, "%d\n",&N);

	for(int i=0;i<N;i++)
	{
		fscanf(fp, "%d\n", &T);

		fscanf(fp, "%d %d\n", &NA, &NB);

		ARCnt = 0;
		BRCnt = 0;

		AResult = 0;
		BResult = 0;

		for(int j=0;j<SCHEMAX;j++)
		{
			AU[j] = false;
			BU[j] = false;
		}

		for(j=0;j<NA;j++)
		{
			fscanf(fp, "%d:%d %d:%d\n", &sA[j].departure.h, &sA[j].departure.m, &sA[j].arrive.h, &sA[j].arrive.m);
			BR[BRCnt] = sA[j].arrive;
			minadd(&BR[BRCnt], T);
			BRCnt++;

			//printf("%d:%d %d:%d\n",sA[j].departure.h, sA[j].departure.m, sA[j].arrive.h, sA[j].arrive.m);
		}

		for(j=0;j<NB;j++)
		{
			fscanf(fp, "%d:%d %d:%d\n", &sB[j].departure.h, &sB[j].departure.m, &sB[j].arrive.h, &sB[j].arrive.m);
			AR[ARCnt] = sB[j].arrive;
			minadd(&AR[ARCnt], T);
			ARCnt++;

			//printf("%d:%d %d:%d\n",sB[j].departure.h, sB[j].departure.m, sB[j].arrive.h, sB[j].arrive.m);
		}

		time tmp;

		for(j=0;j<ARCnt-1;j++)
		{
			for(int k=j;k<ARCnt;k++)
			{
				if(compare(AR[j], AR[k]) > 0)
				{
					tmp = AR[j];
					AR[j] = AR[k];
					AR[k] = tmp;
				}
			}
		}

		for(j=0;j<BRCnt-1;j++)
		{
			for(int k=j;k<BRCnt;k++)
			{
				if(compare(BR[j], BR[k]) > 0)
				{
					tmp = BR[j];
					BR[j] = BR[k];
					BR[k] = tmp;
				}
			}
		}

		for(j=0;j<NA-1;j++)
		{
			for(int k=j;k<NA;k++)
			{
				if(compare(sA[j].departure, sA[k].departure) > 0)
				{
					tmp = sA[j].departure;
					sA[j].departure = sA[k].departure;
					sA[k].departure = tmp;
				}
			}
		}

		for(j=0;j<NB-1;j++)
		{
			for(int k=j;k<NB;k++)
			{
				if(compare(sB[j].departure, sB[k].departure) > 0)
				{
					tmp = sB[j].departure;
					sB[j].departure = sB[k].departure;
					sB[k].departure = tmp;
				}
			}
		}

		int point = 0;

		for(j=0;j<NA;j++)
		{
			if(point < ARCnt && compare(sA[j].departure, AR[point]) >= 0)
				point ++;

			else
				AResult ++;
		}

		point = 0;

		for(j=0;j<NB;j++)
		{
			if(point < BRCnt && compare(sB[j].departure, BR[point]) >= 0)
				point ++;

			else
				BResult ++;
		}

		fprintf(fp2, "Case #%d: %d %d\n",i+1, AResult, BResult);

	}

	fclose(fp2);
	fclose(fp);
	
	return 0;
}