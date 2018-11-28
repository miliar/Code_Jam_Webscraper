#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

const char inFileName[] = "A-small.in";
const char outFileName[] = "A-small.out";

const string in[3] =  {"ejpmysljylckdkxveddknmcrejsicpdrysi", "rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd", "dekrkdeoyakwaejtysrreujdrlkgcjv"};
const string out[3] = {"ourlanguageisimpossibletounderstand", "therearetwentysixfactorialpossibilities", "soitisokayifyouwanttojustgiveup"};

char s[200];

int T, n;
int a[100];

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	for (int i = 0; i < 26; i++) a[i] = (int)('A');
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < in[i].length(); j++)
			a[in[i][j] - 'a'] = out[i][j] - 'a';

	//for (int i = 0; i < 26; i++) fprintf(outFile, "%c -> %c\n", 'a' + i, 'a' + a[i]);

	a['z' - 'a'] = 'q' - 'a';
	a['q' - 'a'] = 'z' - 'a';

	fscanf(inFile, "%d\n", &T);
	for (int t = 0; t < T; t++) 
	{
		fgets(s, 200, inFile);
		int len = strlen(s);

		fprintf(outFile, "Case #%d: ", t + 1);
		for (int i = 0; i < len; i++)
			if (s[i] != ' ') fprintf(outFile, "%c", a[s[i] - 'a'] + 'a');
			else fprintf(outFile, " ");
		fprintf(outFile, "\n");
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
