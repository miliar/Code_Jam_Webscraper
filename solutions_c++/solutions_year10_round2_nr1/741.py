#include<stdio.h>
#include<memory.h>
#include<string.h>


char indirs[110][110];
char outdirs[110][110];

void main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc, n, m, a, b, c, count, ans, found, excount, reqcount;
	ans = 0;
	int cnt;
	
	//fscanf(fp, "%d%d%d", &r, &n, &m);
	fscanf(fp, "%d", &tc);
	for(i=1; i<=tc; i++){
		char exdirs[110][110];
char reqdirs[110][110];
		ans = 0;
		excount = 1;
		reqcount=1;

		fscanf(fp, "%d %d", &n, &m);
		for(a=1; a<=n; a++){
			fscanf(fp, "%s", &indirs[a]);
			for(b=1; b<=strlen(indirs[a]); b++){
				if(indirs[a][b] == '/'){
					strcpy(exdirs[excount], "a");
					for(c=0; c<b; c++){
						exdirs[excount][c] = indirs[a][c];
						
					}
					exdirs[excount][c] = '\0';
					printf("ex[%i]: %s\n", excount, exdirs[excount]);
					excount++;
				}
			}
			strcpy(exdirs[excount], "a");
				
			for(b=0; b<=strlen(indirs[a]); b++){
				exdirs[excount][b] = indirs[a][b];
			}
			printf("ex[%i]: %s\n", excount, exdirs[excount]);			
			excount++;
        }

		
		for(a=1; a<=m; a++){
			fscanf(fp, "%s", &outdirs[a]);
			for(b=1; b<=strlen(outdirs[a]); b++){
				if(outdirs[a][b] == '/'){
					strcpy(reqdirs[reqcount], "a");						
					for(c=0; c<b; c++){
						reqdirs[reqcount][c] = outdirs[a][c];
						
					}
					reqdirs[reqcount][c] = '\0';
					printf("req[%i]: %s\n", reqcount, reqdirs[reqcount]);
					reqcount++;
				}
			}
			strcpy(reqdirs[reqcount], "a");
				
			for(b=0; b<=strlen(outdirs[a]); b++){
				reqdirs[reqcount][b] = outdirs[a][b];
			}
			printf("req[%i]: %s\n", reqcount, reqdirs[reqcount]);
			reqcount++;				
		}
		excount--;
		reqcount--;
		for(a=1; a<=reqcount; a++){
			found = 0;
			for(b=1; b<=excount; b++){
				if(strcmp(reqdirs[a], exdirs[b]) == 0) found = 1;
			}
			if(found == 0){
				ans++;
				excount++;
				strcpy(exdirs[excount], "a");
				strcpy(exdirs[excount], reqdirs[a]);
			}
		}
		excount++;
		reqcount++;
		fprintf(ofp, "Case #%d: %d\n", i, ans);

	}

}