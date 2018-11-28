#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(int argc, char* argv[])
{
	int T, R, C;
	bool flag;
	char** ch;
	FILE *f_in;
	FILE *f_out;
	f_in=fopen("A-large.in","rt");
	f_out=fopen("out.txt","wt");
	fscanf(f_in,"%d",&T);
	for(int r=0; r<T; r++)
	{
		flag=false;
		fscanf(f_in,"%d",&R);
		fscanf(f_in,"%d",&C);
		ch=new char*[R];
		char tmp;
		for(int i=0; i<R; i++)
			ch[i]=new char[C];
		for(int i=0; i<R; i++)
		{
			fscanf(f_in,"%c",&tmp);
			for(int j=0; j<C; j++)
				fscanf(f_in,"%c",&ch[i][j]);
		}
		for(int i=0; i<R-1; i++)
			for(int j=0; j<C-1; j++)
			{
				if(ch[i][j]=='#'&&ch[i+1][j]=='#'&&ch[i+1][j+1]=='#'&&ch[i][j+1]=='#')
				{
					ch[i][j]='/';
					ch[i+1][j]='\\';
					ch[i+1][j+1]='/';
					ch[i][j+1]='\\';
				}

			}
			for(int i=0; i<R; i++)
			{
				for(int j=0; j<C; j++)
					if(ch[i][j]=='#')
					{
						fprintf(f_out,"Case #%d:\nImpossible\n", r+1);
						flag=true;
						break;
					}
				if(flag)
					break;
			}
			if(!flag)
			{
				fprintf(f_out,"Case #%d:\n", r+1);
				for(int i=0; i<R; i++)
				{
					for(int j=0; j<C; j++)
							fprintf(f_out,"%c", ch[i][j]);
					fprintf(f_out,"\n");
				}
			}
	}
	return 0;
}