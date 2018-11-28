#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


long my_add(long input1, long input2){
	long output = 0;
	output = input1 ^ input2; //XOR演算子
	return output;
}

int main(){
	//ファイル入出力部
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T, R, C;
	int cnt_T, cnt_R, cnt_C;
	char data[51][51];
	bool impossible;

	fscanf(fp, "%d", &T); //Tの読み込み
	printf("T:%d", T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		impossible = false;

		//R,Cの読み込み
		fscanf(fp, "\n%d %d\n", &R, &C);
		printf("\n R:%d, C:%d", R, C);

		//データの読み込み
		for (cnt_R=1; cnt_R<=R; cnt_R++){
			for (cnt_C=1; cnt_C<=C; cnt_C++){
				fscanf(fp, "%c", &data[cnt_R][cnt_C]);
			}
			fscanf(fp, "\n");
		}

		//Main
		for (cnt_R=1; cnt_R<=R; cnt_R++){
			for (cnt_C=1; cnt_C<=C; cnt_C++){
				
				//青(#)じゃなかったら。。。
				if (data[cnt_R][cnt_C] != '#') continue;

				//青だったが入れ替えできなかったら。。。
				if (cnt_R == R || cnt_C == C || 
					(data[cnt_R+1][cnt_C] != '#' || 
					 data[cnt_R][cnt_C+1] != '#' || 
					 data[cnt_R+1][cnt_C+1] != '#')){

						 impossible = true;
						 goto Label1;
				}

				//青で入れ替えできるなら。。。
				data[cnt_R][cnt_C] = '/';
				data[cnt_R+1][cnt_C] = '\\';
				data[cnt_R][cnt_C+1] = '\\';
				data[cnt_R+1][cnt_C+1] = '/';
			}
		}

Label1:

		//結果出力
		fprintf(ofp,"Case #%d:\n", cnt_T);

		if (impossible == true){
			fprintf(ofp,"Impossible\n");
		}
		else{
			//データの読み込み
			for (cnt_R=1; cnt_R<=R; cnt_R++){
				for (cnt_C=1; cnt_C<=C; cnt_C++){
					fprintf(ofp,"%c", data[cnt_R][cnt_C]);
				}
				fprintf(ofp,"\n");
			}
		}


	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //終了前の入力待ち
	return 0;
}
