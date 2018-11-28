#include<stdio.h>
#include<string.h>

int main()
{
	FILE *fout = fopen("small.out","w");
	FILE *fin = fopen("small.in","r");
	int L,D,N;
	fscanf(fin,"%d %d %d",&L,&D,&N);
	char xz[6000][20];
	for(int i = 0;i < D;i++)
	{
		fscanf(fin,"%s",&xz[i]);
	}
	for(int i = 0; i < N;i++)
	{
		int counter = 0;
		char temp[600];
		fscanf(fin,"%s",temp);
		for(int j = 0;j < D;j++)
		{
			int allfound = 1;
			int patternnumber = 0;
			for(int k = 0; k < strlen(temp);k++)
			{
				if (temp[k] == '(')
				{
					int found = 0;
					for(int z = k + 1; z < strlen(temp);z++)
					{
						if (temp[z] == xz[j][patternnumber])
						{
							found = 1;
						}
						else if (temp[z] == ')')
						{
							patternnumber ++;
							k = z;
							if (found == 0)
								allfound = 0;
							break;
						}
					}
				}
				else
				{
					if (!(temp[k] == xz[j][patternnumber]))
					{
						allfound = 0;
						patternnumber ++;
						break;
					}
					patternnumber ++;
				}
			}
			if (allfound == 1)
				counter ++;
		}
		fprintf(fout,"Case #%d: %d\n",i + 1,counter);
	}
}