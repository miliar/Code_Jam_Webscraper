#include <cstdio>
#include <algorithm>
using namespace std;

int cases;
int N, K;

char name[] = "E:\\Tdownload\\a1";

int main() 
{
	char input[100];
	strcpy(input, name);
	strcat(input, ".in");
	
	char output[100];
	strcpy(output, name);
	strcat(output, ".out");

	FILE *fin = fopen(input, "r");
	FILE *fou = fopen(output, "w");

	fscanf(fin, "%d", &cases);
	for (int testcases = 0; testcases < cases; testcases++)
	{
		fscanf(fin, "%d %d", &N, &K);
		int a = K + 1;
		int b = 1 << N;
		if (a % b == 0) fprintf(fou, "Case #%d: ON\n", testcases + 1); else fprintf(fou, "Case #%d: OFF\n", testcases + 1);
	}

	fclose(fin);
	fclose(fou);
	return 0;
}
