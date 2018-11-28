#include <stdio.h>
#include <memory.h>

char data[1000][1000];
int r,c;

int main()
{
	FILE* fp=fopen("c:\\a-large.in","r");
	FILE* fp2=fopen("c:\\a-large.txt","w");

#if 0
#define fp stdin
#define fp2 stdout
#endif

	int T;
	fscanf(fp,"%d",&T);
	for (int t=1; t<=T; t++)
	{
		fscanf(fp,"%d%d",&r,&c);
		for (int i=1; i<=r; i++)
		{
			fscanf(fp,"%s",data[i]+1);
		}

		for (int i=1; i<=r; i++)
		{
			for (int j=1; j<=c; j++)
			{
				if (data[i][j] == '#')
				{
					if (data[i][j+1] == '#' && data[i+1][j] == '#' && data[i+1][j+1])
					{
						data[i][j] = '/';
						data[i][j+1] = '\\';
						data[i+1][j] = '\\';
						data[i+1][j+1] = '/';
					}
					else
					{
						fprintf(fp2,"Case #%d:\nImpossible\n", t);
						goto reset;
					}
				}
			}
		}

		fprintf(fp2,"Case #%d:\n", t);

		for (int i=1; i<=r; i++)
		{
			for (int j=1; j<=c; j++)
			{
				fputc(data[i][j],fp2);
			}
			fputc('\n',fp2);
		}


		reset:
		memset(data,0,sizeof(data));
	}
	return 0;
}