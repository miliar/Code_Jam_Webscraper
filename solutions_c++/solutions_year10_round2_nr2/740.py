#include<stdio.h>
#include<memory.h>
#include<string.h>

int ans;
void main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc, n, k, b, t, p, q, r, numchic, slowchic;
	int dist[100];
	int vel[100];
	int finpos[100];
	int cnt;
	fscanf(fp, "%d", &tc);
	//for(i=1;i<=n;i++) fscanf(fp, "%s", &dat[i][1]);
	for(i=1; i<=tc; i++){
		ans = 0;
		numchic = 0;
		slowchic = 0;
		fscanf(fp, "%d %d %d %d", &n, &k, &b, &t);
		for(p=1; p<=n; p++){
			fscanf(fp, "%d", &dist[p]);
		}
		for(p=1; p<=n; p++){
			fscanf(fp, "%d", &vel[p]);
		}
		for(p=1; p<=n; p++){
			finpos[p] = dist[p] + vel[p] * t;
		}
		for(p=1; p<=n; p++){
			if(finpos[p]>=b) numchic++;
		}
		if(numchic >= k){
			for(p=n; k>0; p--){
				if(finpos[p]<b) slowchic++;
				else{
					k--;
					ans += slowchic;
				}
			}
		}
		if(numchic < k) fprintf(ofp, "Case #%d: IMPOSSIBLE\n", i);
		else fprintf(ofp, "Case #%d: %d\n", i, ans);
	}
}