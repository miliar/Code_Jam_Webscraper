#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char map[100][100];
int R,C;
FILE *fin,*fout;


int main(void)
{
	int i,j,k;
	int T;
	int flag;
	fin=fopen("input.in","r");
	fout=fopen("output.out","w+");
	fscanf(fin,"%d",&T);
	for(k=1;k<=T;k++)
	{
		flag=1;
		fscanf(fin,"%d%d\n",&R,&C);
		for(i=1;i<=R;i++)
		{
			for(j=1;j<=C;j++)
				map[i][j]=fgetc(fin);
			fgetc(fin);
		}
		for(i=1;i<=R&&flag;i++)
			for(j=1;j<=C&&flag;j++)
				if(map[i][j]=='#')
				{
					if(i+1>R||j+1>C||map[i+1][j]!='#'||map[i+1][j+1]!='#'||map[i][j+1]!='#')
					{
						flag=0;break;
					}
					map[i][j]='/';
					map[i+1][j]='\\';
					map[i][j+1]='\\';
					map[i+1][j+1]='/';
				}
		fprintf(fout,"Case #%d:\n",k);
		if(flag)
		{
			for(i=1;i<=R;i++)
			{
				for(j=1;j<=C;j++)
					fputc(map[i][j],fout);
				fputc('\n',fout);
			}
		}
		else
			fprintf(fout,"Impossible\n");
	}
	return 0;
}

		
