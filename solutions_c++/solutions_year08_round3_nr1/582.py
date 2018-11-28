#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX 1000
#define MAXK 1200
#define MAXP 1000

int n=0,P,K,L;
long double noskey,keys[MAXK][MAXP];

void bsort(long double frequency[MAX])
{
	int i,j;
	double t;

	for(i=0;i<L-1;i++)
	{
		for(j=0;j<L-1-i;j++)
		{
			if(frequency[j+1]>frequency[j])
			{
				t=frequency[j];
				frequency[j]=frequency[j+1];
				frequency[j+1]=t;
			}
		}
	}
}

void main()
{
	FILE *fp,*fp2;
	int i=0,j=0,w=0,x=0,y=0,count;
	long double frequency[MAX];
	void bsort(long double [MAX]);

	//fp=fopen("E:\\Amol\\CodeJam\\Text\\A-small.txt","r");
	fp=fopen("E:\\Amol\\CodeJam\\Text\\A-large.txt","r");
	if(fp==NULL)
		printf("Error in input file!");

	fscanf(fp,"%d",&n);
	
	//fp2=fopen("E:\\Amol\\CodeJam\\Text\\A-small-out.txt","w");
	fp2=fopen("E:\\Amol\\CodeJam\\Text\\A-large-out.txt","w");
	if(fp2==NULL)
		printf("Error in output file!");

	for(i=0;i<n;i++)
	{
		fscanf(fp,"%d",&P);
		fgetc(fp);
		fscanf(fp,"%d",&K);
		fgetc(fp);
		fscanf(fp,"%d",&L);

		//printf("%d %d %d",P,K,L);

		for(j=0;j<L;j++)
		{
			fscanf(fp,"%Lf",&frequency[j]);
		}

		bsort(frequency);
		noskey=0;
		j=0;

		for(x=0;x<MAXK;x++)
		{
			for(y=0;y<MAXP;y++)
				keys[x][y]=0;
		}

		count=0;
		for(x=0;x<P;x++)
		{
			for(w=0;w<K;w++)
			{
					keys[w][x]=frequency[j++];
					noskey+=(keys[w][x])*(x+1);
					count++;
					if(j==L)
						break;
					//printf("%d\n",count);
					//printf("\n%Lf (%d,%d)", noskey, w,x);
					//getch();
			}
			if(j==L)
				break;
		}

		//printf("%d",noskey);

		fprintf(fp2,"Case #%d: %.0Lf\n",i+1,noskey);
	}

	fclose(fp);
	fclose(fp2);
}