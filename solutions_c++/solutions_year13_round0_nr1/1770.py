#include<stdio.h>
#include<memory.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int T;
char Map[10][10];
int X1[10],X2[10],O1[10],O2[10],XP[10],OP[10],XM[10],OM[10];
int main()
{
	fscanf(in,"%d",&T);
	int i,j,t;
	int N=4;
	int x,o,b;
	for(t=1;t<=T;t++)
	{
		x=o=b=0;
		for(i=1;i<=N;i++) fscanf(in,"%s",&Map[i][1]);
		for(i=0;i<10;i++) X1[i]=X2[i]=O1[i]=O2[i]=XP[i]=OP[i]=XM[i]=OM[i]=0;
		for(i=1;i<=N;i++)
		{
			for(j=1;j<=N;j++)
			{
				if(Map[i][j]=='X')
				{
					X1[i]++; X2[j]++; XP[i+j]++; XM[i-j+4]++;
				}
				else if(Map[i][j]=='O')
				{
					O1[i]++; O2[j]++; OP[i+j]++; OM[i-j+4]++;
				}
				else if(Map[i][j]=='T')
				{
					X1[i]++; X2[j]++; XP[i+j]++; XM[i-j+4]++;
					O1[i]++; O2[j]++; OP[i+j]++; OM[i-j+4]++;
				}
				else
				{
					b=1;
				}
			}
		}
		for(i=0;i<10;i++)
		{
			if(X1[i]==4) x=1;
			if(X2[i]==4) x=1;
			if(O1[i]==4) o=1;
			if(O2[i]==4) o=1;
			if(XP[i]==4) x=1;
			if(OP[i]==4) o=1;
			if(XM[i]==4) x=1;
			if(OM[i]==4) o=1;
		}
		fprintf(out,"Case #%d: ",t);
		if(x) fprintf(out,"X won");
		else if(o) fprintf(out,"O won");
		else if(b) fprintf(out,"Game has not completed");
		else fprintf(out,"Draw");
		fprintf(out,"\n");
	}
}