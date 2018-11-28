#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

bool snp[32];


int main(){
	//ファイル入出力部
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int initial;

	int T, N, K;
	int cnt_T, cnt_K;
	int cnt_N;
	fscanf(fp, "%d", &T); //Tの読み込み
	printf("%d\n", T);
	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		fscanf(fp, "%d %d", &N, &K); //N個,K回の読み込み
		printf("%d %d\n", N, K);

		//初期化
		for (cnt_N=0; cnt_N<32; cnt_N++)	snp[cnt_N]=false;

		//k回処理
		for (cnt_K=1; cnt_K<=K; cnt_K++){
			for (cnt_N=1; cnt_N<=N; cnt_N++){
				if (snp[cnt_N] == true){
					snp[cnt_N] = false;
					continue;
				}
				else if (snp[cnt_N] == false){
					snp[cnt_N] = true;
					break;
				}
			}
		}

		//結果判定
		int flag;
		flag = true;
		for (cnt_N=1; cnt_N<=N; cnt_N++){
			if (snp[cnt_N] == false) flag=false;
		}

		if (flag==false){ //OFFのsnapperがあった
			printf("Case #%d: OFF\n", cnt_T);
			fprintf(ofp,"Case #%d: OFF\n", cnt_T);
		}
		else if (flag==true){ //全てONだった
			printf("Case #%d: ON\n", cnt_T);
			fprintf(ofp,"Case #%d: ON\n", cnt_T);
		}
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //終了前の入力待ち
	return 0;
}
