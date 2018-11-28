#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

int main(){
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T;
	int R, K, N;
	int gp[1024];
	int cnt_T;
	int cnt_R, cnt_K, cnt_N;
	bool skip_flag;
	int head;
	unsigned long long euro;
	int riding;

	fscanf(fp, "%d", &T);
	printf("%d\n", T);
	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		fscanf(fp, "%d %d %d", &R, &K, &N);
		printf("%d %d %d\n", R, K, N);
		for (cnt_N=1; cnt_N<=N; cnt_N++){
			fscanf(fp, "%d", &gp[cnt_N]);
			printf("%d ", gp[cnt_N]);
		}
		printf("\n");

		head = 1;
		euro = 0;
		skip_flag = false;

		int buf_head;
		for (cnt_R=1; cnt_R<=R; cnt_R++){
			riding = 0;
			buf_head = head;
			while (riding + gp[head] <= K){
				riding += gp[head];
				head++;
				if (head > N) head = 1;
				if (head == buf_head) break;
			}
			euro += riding;
			
			if (head != 1) continue;
			if (skip_flag == true) continue;
			skip_flag = true;
			euro = euro * unsigned long long(R/cnt_R);
			R = R % cnt_R;
			cnt_R = 0;			
		}

		printf("Case #%d: %llu\n", cnt_T, euro);
		fprintf(ofp,"Case #%d: %llu\n", cnt_T, euro);
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename);
	return 0;
}
