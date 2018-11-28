#include <stdio.h>
#include <stdlib.h>


void ReadData(int *R,int *k,int *N,int **p,FILE *fp);
void Compute(int R,int k,int N,int *p,int T,FILE *fp);

int main()
{
	int R,k,N,T,i=1;
	int *p;
	FILE *fp1,*fp2;

	fp1=fopen("C-small-attempt0.in.txt","r");
	if(NULL==fp1)
	{
		printf("can't open file");
		return -1;
	}
	fp2=fopen("22.txt","w");
	if(NULL==fp2)
	{
		printf("can't open file");
		return -1;
	}

	fscanf(fp1,"%d",&T);

	while(i<=T)
	{
		ReadData(&R,&k,&N,&p,fp1);
		Compute(R,k,N,p,i,fp2);
		i++;
	}
	fclose(fp1);
	fclose(fp2);

	return 0;
}

void ReadData(int *R,int *k,int *N,int **p,FILE *fp)
{
	int i;

	fscanf(fp,"%d %d %d",R,k,N);

	*p=(int*)malloc(sizeof(int)*(*N));
	if(NULL==p)
	{
		printf("out of space");
		return ;
	}

	for(i=0;i<(*N);i++)
		fscanf(fp,"%d",*p+i);
}

void Compute(int R,int k,int N,int *p,int T,FILE *fp)
{
	int j,total_money,total_person,len,first;

	total_money=0;
	while(R>0)
	{
		R--;
		total_person=0;
		len=N;
		first=p[0];
		
		while(total_person+first<=k && len>0)
		{
			total_person+=first;
			for(j=0;j<N-1;j++)
				p[j]=p[j+1];
			p[N-1]=first;
			first=p[0];
			len--;
		}
		total_money+=total_person;
	}
	free(p);
	fprintf(fp,"Case #%d: %d\n",T,total_money);
}