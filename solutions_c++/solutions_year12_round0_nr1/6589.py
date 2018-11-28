#include<stdio.h>
#include<memory.h>
#include<string.h>

int main()
{
	
	int l, n = 0, length = 0;
	char r;
	char in_text[102], out_text[102];
	char googlerese[] = "ynficwlbkuomxsevzpdrjgthaq";
	
	char filename[100];
	char inputfile[100], outputfile[100];
	scanf("%s", filename);
	
	sprintf_s(inputfile, 100, "%s.in", filename);
	sprintf_s(outputfile, 100, "%s.out", filename);

	FILE *inf=fopen(inputfile, "r");
	FILE *ofp=fopen(outputfile, "w");

	fscanf(inf, "%d%c", &n, &r);

	for(l = 1; l <= n; ++l)
	{
		in_text[0] = '\0';
		fgets(&in_text[0], 102, inf);

		out_text[0] = '\0';

		length = strlen(in_text);

		for(unsigned int letter = 0; letter < length; ++letter)
		{
			if((in_text[letter] > 0x60) && (in_text[letter] <= 0x7A))
				out_text[letter] = strchr(googlerese, in_text[letter]) - googlerese + 1 + 0x60;
			else
				out_text[letter] = in_text[letter];
		}

		out_text[length] = '\0';

		fprintf(ofp, "Case #%d: %s", l, out_text);
	}

	fclose(inf);
	fclose(ofp);

	return 0;
}

