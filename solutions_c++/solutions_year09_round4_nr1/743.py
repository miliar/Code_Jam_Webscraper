/*#include<stdio.h>

char a[100][100];
int b[100];

int T, n;
int result;

int main()
{
	FILE *infile = fopen("a.in", "rt"), *outfile = fopen("a.out", "wt");
	
	fscanf(infile, "%d", &T);
	for(int loop=1; loop<=T; loop++) {
		fscanf(infile, "%d", &n);
		int i, j;
		for(i=0; i<n; i++) {
			fscanf(infile, "%s", a[i]);
			b[i] = 0;
			for(j=0; j<n; j++) {
				if(a[i][j] == '1') b[i] = j;
			}
		}
		result = 0;
		for(i=0; i<n-1; i++) {
			int cnt = 0;
			for(j=0; j<n; j++) {
				if(b[j] == -1) {
				}
				else if(b[j] <= i) {
					result += cnt;
					b[j] = -1;
					break;
				}
				else {
					cnt++;
				}
			}
		}

		printf("Case #%d: %d\n", loop, result);
	}

	
	fclose(infile);
	fclose(outfile);
	return 0;
}


*/
#include<stdio.h>

int T, n;
char a[50][50];
int b[50];


int main()
{
	FILE *infile = fopen("a.in", "rt");
	FILE *outfile = fopen("a.out", "wt");

	fscanf(infile, "%d", &T);

	for(int loop=1; loop<=T; loop++) {
		fscanf(infile, "%d", &n);
		int i, j, k;

		for(i=0; i<n; i++) {
			fscanf(infile, "%s", a[i]);
			b[i] = 0;
			for(j=0; j<n; j++) {
				if(a[i][j] == '1') b[i] = j;
			}
		}
		
		int result = 0;
			
		for(i=0; i<n-1; i++)  {
			if(b[i] <= i) continue;
			for(j=i+1; j<n; j++) {
				if(b[j] <= i) break;
			}
			result += j-i;
			int t = b[j];
			for(; j>i; j--) {
				b[j] = b[j-1];
			}
			b[i] = t;
		}

		fprintf(outfile, "Case #%d: %d\n", loop, result);
	}

	fclose(infile);
	fclose(outfile);


	return 0;
}
