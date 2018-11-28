#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	FILE *f, *f2;
	FILE *f3, *f4;
	int many;
	char str[30][200];
	char str2[30][200];
	char googlerese[30];
	char pregoog[30];
	
	f = fopen("gooinput.txt", "r");
	f2 = fopen("input_output.txt", "r");

	fscanf(f, "%d\n", &many);
	
	for(int i=0; i<many; i++)
		fgets(str[i], 200 ,f);

	for(int i=0; i<many; i++)
		fgets(str2[i], 200 ,f2);


	//printf("%d\n", many);

	for(int i=0; i<many-1; i++)
	{
		str[i][strlen(str[i])-1] = NULL;
		str2[i][strlen(str2[i])-1] = NULL;
	}

	for(int i=0; i<30; i++)
	{
		googlerese[i]=i+'a';
	}

	for(int i=0; i<26; i++)
	{
		pregoog[i] = googlerese[i];
	}

	for(int i=0; i<many; i++)
		printf("%s\n", str[i]);
	printf("\n");
	for(int i=0; i<many; i++)
		printf("%s\n", str2[i]);

	for(int i=0; i<many; i++)
	{
		for(int j=0; j<strlen(str[i]); j++)
		{
			if(str[i][j] != ' ')
				googlerese[str[i][j]-'a'] = str2[i][j];
		}
	}

	googlerese['q'-'a']='z';
	googlerese['z'-'a']='q';

	for(int i=0; i<26; i++)
	{
		printf("%c -> %c\n", pregoog[i], googlerese[i]);
	}


	f3 = fopen("input.txt", "r");
	f4 = fopen("output.txt", "w");

	int num;
	char pretranslate[30][200];
	char translate[30][200];

	fscanf(f3, "%d\n", &num);

	for(int i=0; i<num; i++)
		fgets(pretranslate[i], 200, f3);

	for(int i=0; i<num-1; i++)
	{
		pretranslate[i][strlen(pretranslate[i])-1] = NULL;
	}

	for(int i=0; i<num; i++)
	{
		for(int j=0; j<strlen(pretranslate[i]); j++)
		{
			if(pretranslate[i][j] != ' ')
				translate[i][j] = googlerese[pretranslate[i][j]-'a'];
			else
				translate[i][j] = ' ';
		}

		translate[i][strlen(pretranslate[i])] = NULL;
	}

	for(int i=0; i<num; i++)
	{
		fprintf(f4, "Case #%d: ", i+1);
		if(i==(num-1))
			fprintf(f4, "%s", translate[i]);
		else
			fprintf(f4, "%s\n", translate[i]);
	}
	
	return 0;
}