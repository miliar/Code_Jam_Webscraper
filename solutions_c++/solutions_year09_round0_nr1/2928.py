#include<stdio.h>
#include<string.h>

FILE *in = fopen("large.in","r");
FILE *out = fopen("large.out","w");

int main()
{

	int L,D,N;
	fscanf(in,"%d %d %d",&L,&D,&N);
	char words[6000][30];
	for(int i = 0;i < D;i++)
		fscanf(in,"%s",&words[i]);
	for(int i = 0; i < N;i++)
	{
		int counter = 0;
		char dic[1000];
		fscanf(in,"%s",dic);
		for(int j = 0;j < D;j++)
		{
			int allfound = 1;
			int patternnumber = 0;
			for(int k = 0; k < strlen(dic);k++)
			{
				if (dic[k] == '(')
				{
					int found = 0;
					for(int z = k + 1; z < strlen(dic);z++)
					{
						if (dic[z] == words[j][patternnumber])
							found = 1;
						else if (dic[z] == ')')
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
					if (!(dic[k] == words[j][patternnumber]))
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
		fprintf(out,"Case #%d: %d\n",i + 1,counter);
	}
}
