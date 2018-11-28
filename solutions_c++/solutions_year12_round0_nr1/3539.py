#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	int t = 0;
	char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
	char input_string[111];
	int string_length = 0;
	FILE *fin;
	FILE *fout;

	fin = fopen("A-small-attempt2.in", "r");
	fout = fopen("A-output.out", "w");

	fscanf(fin, "%d ", &t);



	for(int cycle = 0; cycle<t; cycle++)
	{		
		fgets(input_string, 110, fin);
		//	cin.getline(input_string, sizeof(input_string));

		string_length = strlen(input_string);
		input_string[strlen(input_string)-1] = '\0';

		fprintf(fout, "Case #%d: ", cycle+1);

		//	for(int i=0; i<string_length; i++)
		int i = 0;
		while(input_string[i] != '\0')
		{
			if (input_string[i] == ' ') fprintf(fout, " ");
			else fprintf(fout, "%c", map[input_string[i]-'a']);
			//	else fprintf(fout, "%c", input_string[i]);
			//	printf("%c", map[i]);
			i++;
		}
		fprintf(fout, "\n");
	}

	fclose(fin);
	fclose(fout);
}