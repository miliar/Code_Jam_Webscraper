#include "stdio.h"
#include "string.h"
int main(int argc, char* argv[])
{
	if(argc > 0)
	{
		FILE* fp = fopen(argv[1],"r");
		FILE* fOut = fopen("c:\\Output1.txt", "w+");
		
		if(fp != NULL)
		{
			int L, D, N;
			char Dict[500][500];

			fscanf(fp, "%d %d %d", &L, &D, &N);
			for(int i=0; i<D; i++)
			{
				fscanf(fp, "%s", Dict[i]);
			}

			char text[500];
			for(int j=0; j<N; j++)
			{
				char Grid[500][500];
				if(fscanf(fp, "%s", text) != NULL)
				{
					//printf("%s\n", text);
					bool bBracket = false;
					bool bChar = false;

					int nRow = 0, k =0;
					int nCount = strlen(text);
					
					for(int l=0;l<nCount;l++)
					{
						if(text[l] == '(')
						{
							bBracket = true;
							if(bChar == true)
							{
								Grid[nRow][k] = '\0';
								nRow++;
								k=0;
							}
						}
						else if(text[l] == ')')
						{
							bChar = false;
							bBracket = false;
							Grid[nRow][k] = '\0';
							nRow++;
							k=0;
						}
						else
						{
							bChar = true;
							Grid[nRow][k++] = text[l];
							if(bBracket == false)
							{
								bChar = false;
								Grid[nRow][k] = '\0';
								nRow++;
								k=0;
							}
						}
					
					}

					/*
					printf("__________Grid Generated_________\n");
					for(int c=0; c<nRow;c++)
						printf("%s\n", Grid[c]);

					printf("___________________________________\n");
					*/


					int nMatch = 0;
					for(int i=0; i<D; i++)
					{
						int nLen = 0;
						int nCount = strlen(Dict[i]);
						char ch;
						for(int l=0;l<nCount ;l++)
						{
							ch = Dict[i][l];
							int nCount2 = strlen(Grid[l]);
							for(int k=0; k<nCount2; k++)
							{
								if(Grid[l][k] == ch)
								{
									nLen++;
									break;
								}
							}
						}
						if(nCount == nLen)
							nMatch++;
					}

					fprintf(fOut, "Case #%d: %d\n", j+1, nMatch);
				}
			}
			
		}

		if(fOut != NULL)
			fclose(fOut);

		if(fp != NULL)
			fclose(fp);

	}

	return 0;

}