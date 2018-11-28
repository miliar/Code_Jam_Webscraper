#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>

void main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc, l, p, c, x, y, z, ans, div, idiv, pow, numpow, num2pow;
	float fdiv;
	float tl, tp;
	int cnt;
	fscanf(fp, "%d", &tc);
	//for(i=1;i<=n;i++) fscanf(fp, "%s", &dat[i][1]);
	for(i=1; i<=tc; i++){
		ans = 0;
		fscanf(fp, "%d %d %d", &l, &p, &c);
		div = p/l;
		if(l * div < p) div++; 
		pow = c;
		numpow = 1;
		while(div > pow){
			pow = pow * c;
			numpow++;
		}
		if(numpow == 1) ans = 0;
		else{
			pow = 2;
			ans = 1;
			while(numpow > pow){
				pow = pow * 2;
				ans++;
			}
		}
		fprintf(ofp, "Case #%d: %d\n", i, ans);
	}
}