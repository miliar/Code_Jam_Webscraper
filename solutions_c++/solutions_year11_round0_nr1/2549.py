#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(){
	//ファイル入出力部
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T, N, R, P, Pold[2], Rold, y;
	char Rchar;
	int notPwait;
	
	int cnt_T, cnt_N;

	fscanf(fp, "%d", &T); //Tの読み込み
	printf("%d\n", T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		y=0;
		Rold=2;
		notPwait = 0; // 次にボタンを押す方ではないロボットの待ち時間を記録
		Pold[0] = 1;	Pold[1] = 1;

		//Nの読み込み
		fscanf(fp, "%d", &N);
		printf("%d\n", N);
		for (cnt_N=1; cnt_N<=N; cnt_N++){
			//R,Pの読み込み
			fscanf(fp, " %c %d", &Rchar, &P);
			printf("%c %d ", Rchar, P);
			if (Rchar == 'O') R=0;
			if (Rchar == 'B') R=1;

			if (R == Rold || cnt_N == 1){ // 前回と同じロボのときと初回
				y += abs(P - Pold[R]) + 1;
				notPwait += abs(P - Pold[R]) + 1;
			}
			else if (R != Rold){	// 前回と違うロボのとき
				if (abs(P - Pold[R]) > notPwait){ //他のロボの移動時間内では移動が終わらなかった
					y += abs(P - Pold[R]) - notPwait + 1;
					notPwait = abs(P - Pold[R]) - notPwait + 1;
				}else{ //他のロボの移動時間内に移動が終わっていた
					y = y+1; //ボタンを押す時間だけ必要
					notPwait = 1;
				}
			}
			printf("y=%d\n", y);

			Rold = R;
			Pold[R] = P;
		}
		fprintf(ofp,"Case #%d: %d\n", cnt_T, y);
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //終了前の入力待ち
	return 0;
}
