#include <iostream>
using namespace std;

typedef struct  
{
	long time;
	long is_start;
	long a_or_b;
}Info;

Info even[440];

int cmp(const void *p1, const void *p2)
{
	Info *a=(Info *) p1;
	Info *b=(Info *) p2;

	if (a->time>b->time)
	{
		return 1;
	}

	if (a->time<b->time)
	{
		return -1;
	}

	if (a->is_start>b->is_start)
	{
		return 1;
	}

	if (a->is_start<b->is_start)
	{
		return -1;
	}

	return 0;

}
FILE *fp1,*fp2;
int main()
{

	fp1=fopen("B-large.in","r");
	fp2=fopen("B-large.out","w");
	long N;
	fscanf(fp1,"%ld",&N);
	//scanf("%ld",&N);
	long T,NA,NB;
	long i;
	for (i=1;i<=N;++i)
	{
		fscanf(fp1,"%ld",&T);
		fscanf(fp1,"%ld %ld",&NA,&NB);
// 		scanf("%ld",&T);
// 		scanf("%ld %ld",&NA,&NB);
		long j;
		
		long hh1,mm1,hh2,mm2;
		
		long mindex=0;

		for (j=0;j<NA;++j)
		{
			fscanf(fp1,"%ld:%ld %ld:%ld",&hh1,&mm1,&hh2,&mm2);
		//	scanf("%ld:%ld %ld:%ld",&hh1,&mm1,&hh2,&mm2);

			even[mindex].a_or_b=0;
			even[mindex].is_start=1;
			even[mindex].time=hh1*60+mm1;

			++mindex;

			even[mindex].a_or_b=1;
			even[mindex].is_start=0;
			even[mindex].time=hh2*60+mm2+T;

			++mindex;
		}

		for (j=0;j<NB;++j)
		{
			fscanf(fp1,"%ld:%ld %ld:%ld",&hh1,&mm1,&hh2,&mm2);
		//scanf("%ld:%ld %ld:%ld",&hh1,&mm1,&hh2,&mm2);
			
			even[mindex].a_or_b=1;
			even[mindex].is_start=1;
			even[mindex].time=hh1*60+mm1;

			++mindex;
			
			even[mindex].a_or_b=0;
			even[mindex].is_start=0;
			even[mindex].time=hh2*60+mm2+T;
			
			++mindex;
		}

		qsort(even,mindex,sizeof(Info),cmp);

		long a_had=0,b_had=0;
		long a_need=0,b_need=0;

		for (j=0;j<mindex;++j)
		{
			if (even[j].is_start==0)//到达
			{
				if (even[j].a_or_b==0)//a站
				{
					++a_had;
				}
				else//b站
				{
					++b_had;
				}
			}
			else // 出发
			{

				if (even[j].a_or_b==0)//a站
				{
					if(a_had>0)
					{
						--a_had;
					}
					else
					{
						++a_need;
					}
				}
				else//b站
				{
					if(b_had>0)
					{
						--b_had;
					}
					else
					{
						++b_need;
					}
				}
			}
		}
	//	printf("Case #%ld:%ld %ld\n",i,a_need,b_need);
		fprintf(fp2,"Case #%ld: %ld %ld\n",i,a_need,b_need);

	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}