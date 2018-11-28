// googlerese.cpp
#include <stdio.h>
#include <string.h>

int main(void)
{

	//								'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
	char charmap[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'}; 

	int T = 0;	
	char line[200];

	FILE* fin  = fopen("in.txt", "r");
	FILE* fout = fopen("out.txt", "w");

	if ((fin != NULL) && (fout != NULL)) 
	{
		fscanf(fin, "%d", &T);
		fgets(line, 200, fin);

		for(int i=0; i<T; ++i)
		{
			fgets(line, 200, fin);

			for(int j=0; j<strlen(line); ++j)
			{
				if('a' <= line[j] && line[j] <= 'z')
					line[j] = charmap[line[j]-'a'];
			}

			fprintf(fout,"Case #%d: ", i+1);
			fputs(line, fout);
		}
	}
	else
	{
		printf("error: open file out.txt or in.txt\n");
	}
	
	fclose(fin);
	fclose(fout);
	return 0; 
}
