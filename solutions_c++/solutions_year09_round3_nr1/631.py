#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INFILE "A-large.in"
#define OUTFILE "A-large.out"

char line[64];
int hashTab[36];

int main()
{
	FILE *fpIn = freopen(INFILE, "r", stdin);
	FILE *fpOut = fopen(OUTFILE, "w");

	int T;
	scanf("%d", &T);
	gets(line);

	// dbg 
	// printf("T = %d\n", T);
	// dbg end
	for (int cnt1 = 0; cnt1 < T; cnt1++) {
		for (int i = 0; i < 36; i++)
			hashTab[i] = -1;
		gets(line);
		// dbg 
		// printf("%s\n", line);
		// dbg end
		int len = strlen(line);
		unsigned long long base = 0;
		for (int i = 0; i < len; i++) {
			if (i == 0) {
				int idx;
				if (line[i] >= '0' && line[i] <= '9') 
					idx = line[i] - '0';					
				else 
					idx = 10 + line[i] - 'a'; 
				hashTab[idx] = 1;
				base++;
			}
			else {
				int idx;
				if (line[i] >= '0' && line[i] <= '9') 
					idx = line[i] - '0';					
				else 
					idx = 10 + line[i] - 'a';
				if (hashTab[idx] == -1) {
					if (base == 1) 
						hashTab[idx] = 0;
					else
						hashTab[idx] = base;
					base++;
				}
			}			
		} // for (int i = 0; i < len; i++) 
		
		if (base == 1)
			base = 2;
		
		for (int i = 0; i < len; i++)  {
			int idx;
			if (line[i] >= '0' && line[i] <= '9') 
				idx = line[i] - '0';					
			else 
				idx = 10 + line[i] - 'a'; 
			// dbg
			// printf("i = %d, hashTab[idx] = %d\n", i, hashTab[idx]);
			// dbg end
			line[i] = hashTab[idx];
		}

		unsigned long long res = 0;
		for (int i = len-1, j=0; i >= 0; i--, j++)
		{
			unsigned long long mid = 1;
			for (int k = 1; k <= j; k++) 
				mid = mid * base;
			unsigned long long tmp = line[i];
			res = res + mid*tmp;
		}

		fprintf(fpOut, "Case #%d: %lld\n", cnt1+1, res);
	} // for (int cnt1 = 0; cnt1 < T; cnt1++) 

	fclose(fpIn);
	fclose(fpOut);
}