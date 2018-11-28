#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "A-large.in";
const char outFileName[] = "A-large.out";

const string text[4] = {"X won", "O won", "Draw", "Game has not completed"};

int T, n, sol;
char s[10][10];
int a[10][10];

void print(int caseNum, FILE* outFile, int ind)
{
	fprintf(outFile, "Case #%d: %s\n", caseNum, text[ind].c_str());
}

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) 
	{
		fscanf(inFile, "%d", &n);
		for (int i = 0; i < 4; i++)
			fscanf(inFile, "%s", s[i]);
		fscanf(inFile, "\n");
		
		bool x, o;
		int dots = 0;

		//rows
		for (int i = 0; i < 4; i++)
		{
			x = true; o = true;
			for (int j = 0; j < 4; j++)
			{
				x = x && (s[i][j] == 'X' || s[i][j] == 'T');
				o = o && (s[i][j] == 'O' || s[i][j] == 'T');
				if (s[i][j] == '.') dots++;
			}
			if (x) { print(t + 1, outFile, 0); break; }
			if (o) { print(t + 1, outFile, 1); break; }
		}
		if (x || o) continue;

		//cols
		for (int j = 0; j < 4; j++)
		{
			x = true; o = true;
			for (int i = 0; i < 4; i++)
			{
				x = x && (s[i][j] == 'X' || s[i][j] == 'T');
				o = o && (s[i][j] == 'O' || s[i][j] == 'T');
				if (s[i][j] == '.') dots++;
			}
			if (x) { print(t + 1, outFile, 0); break; }
			if (o) { print(t + 1, outFile, 1); break; }
		}
		if (x || o) continue;

		//diags
		x = true; o = true;
		for (int i = 0; i < 4; i++)
		{
			x = x && (s[i][i] == 'X' || s[i][i] == 'T');
			o = o && (s[i][i] == 'O' || s[i][i] == 'T');
			
		}
		if (x) { print(t + 1, outFile, 0); continue; }
		if (o) { print(t + 1, outFile, 1); continue; }

		x = true; o = true;
		for (int i = 0; i < 4; i++)
		{
			x = x && (s[i][3 - i] == 'X' || s[i][3 - i] == 'T');
			o = o && (s[i][3 - i] == 'O' || s[i][3 - i] == 'T');
			
		}
		if (x) { print(t + 1, outFile, 0); continue; }
		if (o) { print(t + 1, outFile, 1); continue; }

		if (dots == 0) 
			print(t + 1, outFile, 2);
		else
			print(t + 1, outFile, 3);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
