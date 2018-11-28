#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

struct Tcase{
	int T;
	int N;
	int K;
	bool result;
};

Tcase caselist[10001];
bool snp[32];

int compare_Tcase(const Tcase *A, const Tcase *B){
	if (A->K != B->K) return (A->K - B->K);
	return (A->N - B->N);
}

int compare_Tcase_T(const Tcase *A, const Tcase *B){
	return (A->T - B->T);
}

int main(){
	//ファイル入出力部
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T;
	int cnt_T, cnt_K;
	int cnt_N;
	int buf_id=1;

	fscanf(fp, "%d", &T); //Tの読み込み
	printf("%d\n", T);
	//N個,K回の読み込み
	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		caselist[cnt_T].T = cnt_T;
		fscanf(fp, "%d %d", &caselist[cnt_T].N, &caselist[cnt_T].K);
		printf("%d %d\n", caselist[cnt_T].N, caselist[cnt_T].K);
	}
	//Kでソートする
	qsort(&caselist[1], T, sizeof(Tcase), (int (*)(const void*, const void*))compare_Tcase);
	printf("\n-----------------\n");
	for (cnt_T=1; cnt_T<=T; cnt_T ++){ printf("%d %d\n", caselist[cnt_T].N, caselist[cnt_T].K); }

	//初期化
	for (cnt_N=0; cnt_N<32; cnt_N++)	snp[cnt_N]=false;

	//K=0のものはここで判定処理する
	while (caselist[buf_id].K == 0){
		//結果判定
		caselist[buf_id].result = true;
		for (cnt_N=1; cnt_N<=caselist[buf_id].N; cnt_N++){
			if (snp[cnt_N] == false){
				caselist[buf_id].result = false;
				break;
			}
		}

		buf_id++;
	}

	//k回処理
	for (cnt_K=1; cnt_K<=caselist[T].K; cnt_K++){
		//1回指パッチンすると。。。
		for (cnt_N=1; cnt_N<32; cnt_N++){
			if (snp[cnt_N] == true){
				snp[cnt_N] = false;
				continue;
			}
			else if (snp[cnt_N] == false){
				snp[cnt_N] = true;
				break;
			}
		}

		while (caselist[buf_id].K == cnt_K){
			//結果判定
			caselist[buf_id].result = true;
			for (cnt_N=1; cnt_N<=caselist[buf_id].N; cnt_N++){
				if (snp[cnt_N] == false){
					caselist[buf_id].result = false;
					break;
				}
			}

			buf_id++;
		}
	}

	//Tでソートする
	qsort(&caselist[1], T, sizeof(Tcase), (int (*)(const void*, const void*))compare_Tcase_T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		if (caselist[cnt_T].result==false){
			printf("Case #%d: OFF\n", cnt_T);
			fprintf(ofp,"Case #%d: OFF\n", cnt_T);
		}
		else if (caselist[cnt_T].result==true){ //全てONだった
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
