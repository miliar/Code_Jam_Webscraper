#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int my_char2int(char input){
	int output;
	switch (input){
		case 'Q': output = 0; break;
		case 'W': output = 1; break;
		case 'E': output = 2; break;
		case 'R': output = 3; break;
		case 'A': output = 4; break;
		case 'S': output = 5; break;
		case 'D': output = 6; break;
		case 'F': output = 7; break;
		default:  output = 8; break;
	}

	return output;
}

int main(){
	//�t�@�C�����o�͕�
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T, C, D, N;
	int cnt_T, cnt_C, cnt_D, cnt_N;
	char EleChar1, EleChar2, CombChar, y[100];
	int EleInt1, EleInt2;
	int cur_y;
	int cur_yInt;

	char comb_matrix[9][9], opps_matrix[9][9];
	int kisyutsu[8];	//Oppose�p�̊��o�`�F�b�N�ϐ�

	int i, j;
	bool flag;

	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("%d", T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		cur_y = -1;
		//�}�g���b�N�X�̏�����
		for (i=0; i<9; i++){
			for (j=0; j<9; j++){
				comb_matrix[i][j] = 'n';
				opps_matrix[i][j] = 'n';
			}
		}
		//Oppose�p�̊��o�`�F�b�N�ϐ��̏�����
		for (i=0; i<8; i++){
			kisyutsu[i] = false;
		}


		//C�̓ǂݍ���
		fscanf(fp, "%d", &C);
		printf("\n%d", C);
		for (cnt_C=1; cnt_C<=C; cnt_C++){
			//Combine�̓ǂݍ���
			fscanf(fp, " %c%c%c", &EleChar1, &EleChar2, &CombChar);
			printf(" %c%c%c",  EleChar1, EleChar2, CombChar);
			EleInt1 = my_char2int(EleChar1);
			EleInt2 = my_char2int(EleChar2);

			comb_matrix[EleInt1][EleInt2] = CombChar;
			comb_matrix[EleInt2][EleInt1] = CombChar;
		}

		//D�̓ǂݍ���
		fscanf(fp, " %d", &D);
		printf("\n %d", D);
		for (cnt_D=1; cnt_D<=D; cnt_D++){
			//Opposed�̓ǂݍ���
			fscanf(fp, " %c%c", &EleChar1, &EleChar2);
			printf(" %c%c",  EleChar1, EleChar2);
			EleInt1 = my_char2int(EleChar1);
			EleInt2 = my_char2int(EleChar2);

			opps_matrix[EleInt1][EleInt2] = 'x';
			opps_matrix[EleInt2][EleInt1] = 'x';
		}

		//N�̓ǂݍ���
		fscanf(fp, " %d ", &N);
		printf("\n %d ", N);
		for (cnt_N=1; cnt_N<=N; cnt_N++){

			//Invoke�̓ǂݍ���
			fscanf(fp, "%c", &EleChar1);
			printf("%c", EleChar1);
			EleInt1 = my_char2int(EleChar1);

			//Combine�̃`�F�b�N
			if (cur_y >= 0){
				cur_yInt = my_char2int(y[cur_y]);
				if (comb_matrix[cur_yInt][EleInt1] != 'n'){
					y[cur_y] = comb_matrix[cur_yInt][EleInt1];
					kisyutsu[cur_yInt] --;
					continue; //for(N)���̎��̃X�e�b�v��
				}
			}

			//Oppose�̃`�F�b�N
			if (cur_y >= 0){
				flag = false;
				for (i=0; i<8; i++){
					if (kisyutsu[i] >= 1 && opps_matrix[i][EleInt1] == 'x'){
						flag = true;
						break;
					}
				}
				if (flag == true){
					//�S����
					cur_y = -1;
					for (i=0; i<8; i++){
						kisyutsu[i] = 0;
					}
					continue; //for(N)���̎��̃X�e�b�v��
				}
			}

			//���ʂ�Invoke�̂Ƃ�
			cur_y ++;
			y[cur_y] = EleChar1;
			kisyutsu[EleInt1] ++;

		}

		fprintf(ofp,"Case #%d: [", cnt_T);
		for (i=0; i<=cur_y; i++){
			if (i==0) fprintf(ofp,"%c", y[i]);
			else fprintf(ofp,", %c", y[i]);
		}
		fprintf(ofp,"]\n");
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
