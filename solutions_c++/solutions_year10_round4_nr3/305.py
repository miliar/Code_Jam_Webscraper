#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#define infile "c.in"

FILE *fin=fopen(infile,"r"),
	*fout=fopen("c.out","w");

//for small

int ge,map[2][220][220],now,old;

bool nonempty()
{
	int i,j;
	for (i=1; i<=210; ++i)
		for (j=1; j<=210; ++j)
			if (map[now][i][j]==1)
				return true;
	return false;
}


int main()
{
	int i,j,k,w,t,x1,y1,x2,y2,result;

	fscanf(fin,"%d",&t);
	for (w=1; w<=t; ++w)
	{
		fscanf(fin,"%d", &ge);
		for (i=1; i<=210; ++i)
			for (j=1; j<=210; ++j)
				map[0][i][j]=0;
		for (i=1; i<=ge; ++i)
		{
			fscanf(fin,"%d%d%d%d",&y1,&x1,&y2,&x2);
			for (j=x1; j<=x2; ++j)
				for (k=y1; k<=y2; ++k)
					map[0][j+1][k+1]=1;
		}
		now=0;
		result=0;
		while (nonempty())
		{
			++result;
			old=now;
			now=1-now;
			for (i=1; i<=210; ++i)
				for (j=1; j<=210; ++j)
				{
					if ((i==1)||(j==1))
						map[now][i][j]=0;
					else {
						if (map[old][i][j]==0)
						{
							if ((map[old][i-1][j]==1)&&(map[old][i][j-1]==1))
								map[now][i][j]=1;
							else map[now][i][j]=0;
						}
						else if (map[old][i][j]==1)
						{
							if ((map[old][i-1][j]==0)&&(map[old][i][j-1]==0))
								map[now][i][j]=0;
							else map[now][i][j]=1;
						}
						
					}
				}
		}
		fprintf(fout,"Case #%d: %d\n", w, result);		
		printf("Case #%d: %d\n", w, result);		
	}
	fclose(fin);
	fclose(fout);
	return 0;
}