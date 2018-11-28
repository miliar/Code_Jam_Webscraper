#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char opp[30][2];
char cob[40][3];
char elem[110];
int tail;

FILE *fin,*fout;

int combine(int n)
{
	int i;
	if(tail==1||tail==0)
		return 0;
	for(i=1;i<=n;i++)
		if((cob[i][0]==elem[tail]&&cob[i][1]==elem[tail-1])||(cob[i][1]==elem[tail]&&cob[i][0]==elem[tail-1]))
		{
			elem[--tail]=cob[i][2];
			return 1;
		}
	return 0;
}

void oppose(int n)
{
	int i,j;
	if(tail<=1)
		return;
	for(i=tail-1;i>0;i--)
		for(j=1;j<=n;j++)
			if((opp[j][0]==elem[i]&&opp[j][1]==elem[tail])||(opp[j][1]==elem[i]&&opp[j][0]==elem[tail]))
			{
				tail=0;
				return;
			}
}

int main(void)
{
	int i,j,k;
	int T;
	int C,D,N;
	fin=fopen("b.in","r");
	fout=fopen("b.out","w+");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fscanf(fin,"%d",&C);
		tail=0;
		for(j=1;j<=C;j++)
		{
			fgetc(fin);
			cob[j][0]=fgetc(fin);
			cob[j][1]=fgetc(fin);
			cob[j][2]=fgetc(fin);
		}
		fscanf(fin,"%d",&D);
		for(j=1;j<=D;j++)
		{
			fgetc(fin);
			opp[j][0]=fgetc(fin);
			opp[j][1]=fgetc(fin);
		}
		fscanf(fin,"%d",&N);
		fgetc(fin);
		for(j=1;j<=N;j++)
		{
			elem[++tail]=fgetc(fin);
			while(combine(C))	oppose(D);
			oppose(D);
		}
		fprintf(fout,"Case #%d: [",i);
		for(j=1;j<tail;j++)
			fprintf(fout,"%c, ",elem[j]);
		if(tail!=0)
			fprintf(fout,"%c]\n",elem[j]);
		else
			fprintf(fout,"]\n",elem[j]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
