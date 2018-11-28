#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(){
	//�t�@�C�����o�͕�
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

	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("%d\n", T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		y=0;
		Rold=2;
		notPwait = 0; // ���Ƀ{�^�����������ł͂Ȃ����{�b�g�̑҂����Ԃ��L�^
		Pold[0] = 1;	Pold[1] = 1;

		//N�̓ǂݍ���
		fscanf(fp, "%d", &N);
		printf("%d\n", N);
		for (cnt_N=1; cnt_N<=N; cnt_N++){
			//R,P�̓ǂݍ���
			fscanf(fp, " %c %d", &Rchar, &P);
			printf("%c %d ", Rchar, P);
			if (Rchar == 'O') R=0;
			if (Rchar == 'B') R=1;

			if (R == Rold || cnt_N == 1){ // �O��Ɠ������{�̂Ƃ��Ə���
				y += abs(P - Pold[R]) + 1;
				notPwait += abs(P - Pold[R]) + 1;
			}
			else if (R != Rold){	// �O��ƈႤ���{�̂Ƃ�
				if (abs(P - Pold[R]) > notPwait){ //���̃��{�̈ړ����ԓ��ł͈ړ����I���Ȃ�����
					y += abs(P - Pold[R]) - notPwait + 1;
					notPwait = abs(P - Pold[R]) - notPwait + 1;
				}else{ //���̃��{�̈ړ����ԓ��Ɉړ����I����Ă���
					y = y+1; //�{�^�����������Ԃ����K�v
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
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
