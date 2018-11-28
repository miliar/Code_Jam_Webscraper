#include<stdio.h>
#include<conio.h>
#include<string.h>


#define SIZE_S 102
#define SIZE_Q 1002

void clearmark(void);
int chklast(void);

char srch[SIZE_S][102];
char que [102];
int mark [SIZE_S];

int S,Q;

FILE *fout;

int main(int argc, char **argv)
{
	FILE *fin;
	
	int cases;
	int N, j, lasteng;
	int sw;
		
	fin = fopen(argv[1],"r");
	if(fin==NULL)
	{
		printf("cannot open read file");
		return 0;
	}

	fout = fopen(argv[2],"w");
	if(fout==NULL)
	{
		printf("cannot open write file");
		return 0;
	}

	fscanf(fin,"%d",&cases);

	for(N=1 ; N<=cases; N++)
	{
		sw=0;

		fscanf(fin,"%d",&S);
		fgets(srch[0],100,fin);
		for(int i=0 ; i<S; i++)
			fgets(srch[i],100,fin);

		clearmark();

		fscanf(fin,"%d",&Q);
		fgets(que,100,fin);
		for(int i=0 ; i<Q; i++)
		{
			fgets(que,100,fin);
			for(j=0;j<S;j++)
			{
				if(strcmp(que,srch[j])==0)
				{
					mark[j]=1;
					break;
				}
			}
			
			lasteng = chklast();

			if(lasteng != -1)
			{
				sw++;
				clearmark();
			}
			mark[j]=1;
		}
		//printf("Case #%d: %d \n",N,sw);
		fprintf(fout,"Case #%d: %d \n",N,sw);
	}

	fclose(fin);
	fclose(fout);

	//getch();
	return 0;
}


int chklast(void)
{
	int cnt=0;
	for(int i=0;i<S;i++)
	{
		if(mark[i]==1)cnt++;
	}
	if(cnt==S)	return 1;
	else        return -1;
}

void clearmark(void)
{
	for(int i=0;i<S;i++)
		mark[i]=0;
}
