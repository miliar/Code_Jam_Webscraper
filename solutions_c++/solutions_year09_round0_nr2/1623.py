// Water.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

int alturas[100][100];
char resultado[100][100];
int colar[10000],colac[10000];
int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};
int H,W,T;

int main(int argc, char* argv[])
{
	FILE *entrada = fopen("input.txt","rt");
	FILE *salida = fopen("salida.txt","wt");
	fscanf(entrada,"%d",&T);
	for (int t=0;t<T;t++)
	{
		if (t>0)
		{
			fprintf(salida,"\n");
		}
		fprintf(salida,"Case #%d:\n",t+1);
		char actual='a';
		fscanf(entrada,"%d %d",&H,&W);
		for (int r=0;r<H;r++)
		{
			for (int c=0;c<W;c++)
			{
				fscanf(entrada,"%d",&alturas[r][c]);
				resultado[r][c]=' ';
			}
		}
		for (int r=0;r<H;r++)
		{
			for (int c=0;c<W;c++)
			{
				if (resultado[r][c]!=' ')
				{
					continue;
				}
				colar[0]=r;
				colac[0]=c;
				int contador=1;
				int cc=c;
				int rr=r;
				while (true)
				{
					//move to next
					int nr=rr;
					int nc=cc;
					for (int i=0;i<4;i++)
					{
						int pr=rr+dr[i];
						int pc=cc+dc[i];
						if ((pr<0)||(pc<0)||(pr>=H)||(pc>=W))
						{
							continue;
						}
						if (alturas[nr][nc]>alturas[pr][pc])
						{
							nr=pr;
							nc=pc;
						}
					}
					//if it has a path, assign it
					char assign;
					if (resultado[nr][nc]!=' ')
					{
						assign=resultado[nr][nc];
					}
					else if ((nr==rr)&&(nc==cc))
					{
						//if it is a sink, assign new letter and increment actual
						assign=actual;
						actual++;
						resultado[nr][nc]=assign;
					}
					else
					{
						//nothing
						colar[contador]=nr;
						colac[contador]=nc;
						contador++;
						rr=nr;
						cc=nc;
						continue;
					}
					for (int i=0;i<contador;i++)
					{
						resultado[colar[i]][colac[i]]=assign;
					}
					break;
				}
			}
		}
		for (int r=0;r<H;r++)
		{
			if (r>0)
			{
				fprintf(salida,"\n");
			}
			for (int c=0;c<W;c++)
			{
				if (c>0)
				{
					fprintf(salida," ");
				}
				fprintf(salida,"%c",resultado[r][c]);
			}
		}
	}
	fclose(entrada);
	fclose(salida);
	return 0;
}

