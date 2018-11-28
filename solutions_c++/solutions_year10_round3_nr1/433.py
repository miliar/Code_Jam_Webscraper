#include<stdio.h>
#include<memory.h>
#include<string.h>

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int a[1100];
	int b[1100];

	int i, j, tc, n, p, q, r, ans, temp;
	int cnt;
	fscanf(fp, "%d", &tc);
	//for(i=1;i<=n;i++) fscanf(fp, "%s", &dat[i][1]);
	for(i=1; i<=tc; i++){

		ans = 0;
		fscanf(fp, "%d", &n);
		for(p=1; p<=n ; p++){
			fscanf(fp, "%d %d", &a[p], &b[p]);
		}

		for(p=1; p<=n; p++){
			for(q=p; q<=n; q++){
				if(a[p]>a[q]){
					temp = a[p];
					a[p] = a[q];
					a[q] = temp;

					temp = b[p];
					b[p] = b[q];
					b[q] = temp;
				}
			}
		}
		for(p=1; p<=n; p++){
			for(q=p; q<=n; q++){
				if(b[q]<b[p]) ans++;
			}
		}
		fprintf(ofp, "Case #%d: %d\n", i, ans);
	}

}