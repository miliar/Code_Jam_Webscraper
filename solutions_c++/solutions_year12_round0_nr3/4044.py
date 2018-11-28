#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

const char inFileName[] = "C-large.in";
const char outFileName[] = "C-large.out";

const int MaxN = 1010;

int T, n;
int A, B, pow10[10], len;
int mark[20];

int shift(int X, int len, int pos)
{
	int tmp = X % pow10[pos];
	if (tmp < pow10[pos - 1]) return -1;

	return (tmp * pow10[len - pos] + X / pow10[pos]);
}

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	pow10[0] = 1;
	for (int i = 1; i < 10; i++) pow10[i] = pow10[i - 1] * 10;

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) {

		fscanf(inFile, "%d%d", &A, &B);
		int a1 = A;
		len = 0;
		while (a1 > 0)
		{
			len++;
			a1 /= 10;
		}

		int sol = 0;
		for (int num = A; num < B; num++)
		{
			int count = 0;
			for (int pos = 1; pos < len; pos++)
			{
				int x = shift(num, len, pos);
				bool marked = false;
				for (int i = 0; i < count; i++)
					if (x == mark[i]) marked = true;

				if (num < x && x <= B && !marked) 
				{
					sol++;
					mark[count++] = x;
				}
			}
		}

		fprintf(outFile, "Case #%d: %d\n", t + 1, sol);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
