#include<cstdio>
#include<cstring>

using namespace std;

int N;
char s[600];
char w[20] = "welcome to code jam";

int d[500][19];

int main()
{
	FILE *infile = fopen("c.in", "rt");
	fscanf(infile, "%d\n", &N);
	
	FILE *outfile = fopen("c.out", "wt");

	int wl = strlen(w);
	for(int loop=1; loop<=N; loop++) {
		fgets(s, 510, infile);
		int sl = strlen(s);
		
		int i, j;
		int t = 0;
		for(int i=0; i<sl; i++) {
			if(s[i] == 'w') d[i][0] = t + 1;
			else d[i][0] = t;
			t = d[i][0];
		}

		for(j=1; j<wl; j++) {
			t = 0;
			for(i=0; i<sl; i++) {
				if(s[i] == w[j]) {
					d[i][j] = d[i-1][j-1] + d[i-1][j];
				}
				else {
					d[i][j] = d[i-1][j];
				}
				d[i][j] %= 10000;
				t = d[i][j];
			}
		}

		fprintf(outfile, "Case #%d: %04d\n", loop, d[sl-1][wl-1]);
	}

	fclose(outfile);
	fclose(infile);
	return 0;
}
