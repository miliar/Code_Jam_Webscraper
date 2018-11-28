#include<cstdio>
#include<cstring>

using namespace std;

int T;

char N[10];

int d[10];

int main()
{
	FILE *infile = fopen("b.in", "rt"), *outfile = fopen("b.out", "wt");


	fscanf(infile, "%d", &T);
	

	for(int loop=1; loop<=T; loop++) {
		fscanf(infile, "%s", N);
		
		int len = strlen(N);
		int i, j;

		int t = 0;

		fprintf(outfile, "Case #%d: ", loop);

		for(i=0; i<10; i++) d[i] = 0;
		for(i=len-2; i>=0; i--) {
			//int n = N[i]-'0';
			if(N[i] < N[i+1]) {
				int k;
				for(k=i+1; N[k]>N[i]; k++);
				k--;

				char t = N[i];
				N[i] = N[k];
				N[k] = t;
				break;
			}
		}
		if(i >= 0) {
			for(j=0; j<=i; j++) {
				fprintf(outfile, "%c", N[j]);
			}
			for(j=len-1; j>i; j--) {
				fprintf(outfile, "%c", N[j]);
			}
		}
		else {
			for(i=len-1; i>=0; i--) {
				if(N[i] != '0') {
					char t = N[i];
					N[i] = N[len-1];
					N[len-1] = t;
					break;
				}
			}
			fprintf(outfile, "%c0", N[len-1]);
			for(j=len-2; j>=0; j--) {
				fprintf(outfile, "%c", N[j]);
			}
		}
		
		fprintf(outfile, "\n");
	}
	

	
	fclose(infile); fclose(outfile);
	return 0;
}
