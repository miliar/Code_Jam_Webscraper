#include <iostream>

using namespace std;

char LetterMap[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v',
	'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 
	't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(int argc, char *argv[])
{
	int T;
	char input_str[102];
	FILE *inputfile = fopen("A-small-attempt1.in", "r");
	FILE *outputfile = fopen("A-small-attemp1.out", "w");
	fscanf(inputfile, "%d\n", &T);
	for (int i = 0; i != T; ++i)
	{
		fgets(input_str, 102, inputfile);
		int j = 0;
		while (input_str[j] != '\0')
		{
			if (input_str[j] != ' ')
				input_str[j] = LetterMap[input_str[j] - 'a'];
			++j;
		}
		fprintf(outputfile, "Case #%d: %s\n", i+1, input_str);
	}

	fclose(inputfile);
	fclose(outputfile);

	return 0;
}