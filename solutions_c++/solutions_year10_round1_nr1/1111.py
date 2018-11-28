#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

char data[64][64];

int main(){
	//�t�@�C�����o�͕�
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T, N, K;
	int cnt_T, row, col, d_row;
	int i;
	char buf[64];
	bool flag_R, flag_B;
	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("%d\n", T);
	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		fscanf(fp, "%d %d", &N, &K); //N��,K��̓ǂݍ���
		printf("%d %d\n", N, K);

		//������
		for (row=1; row<64; row++){
			for (col=1; col<64; col++){
				data[row][col] = '\0';
			}
		}
		for (row=1; row<=N; row++){
			for (col=1; col<=N; col++){
				data[row][col] = '.';
			}
		}
		//�f�[�^���
		for (row = 1; row<=N; row++){
			d_row = N;
			fscanf(fp, "%s", buf);
			for (col=N; col>=1; col--){
				//�E����"."�łȂ����̂�I��ő�����Ă���
				if (buf[col-1] == '.') continue;

				data[d_row][N-row+1]=buf[col-1];
				d_row--;
			}
		}

		//�\��
		for (row = 1; row<=N; row++){
			printf("%s \n", &data[row][1]);
		}

		//������
		flag_R = false; flag_B = false;
		//��r�p������
		char comp_R[64], comp_B[64], comp_data[64];
		for (col=0; col<K; col++){
			comp_R[col] = 'R';
			comp_B[col] = 'B';
		}
		for (col=K; col<64; col++){
			comp_R[col] = '\0';
			comp_B[col] = '\0';
		}

		//����
		for (row=1; row<=N; row++){
			for (i=0; i<64; i++){ comp_data[i] = '\0';} //������

			for (col=1; col<=N; col++) comp_data[col-1] = data[row][col];
			if (strstr(comp_data, comp_R) != NULL) {
				flag_R = true;
//				printf("Suihei");
			}
			if (strstr(comp_data, comp_B) != NULL){
				flag_B = true;
//				printf("Suihei");
			}
		}

		//����
		for (col=1; col<=N; col++){
			for (i=0; i<64; i++){ comp_data[i] = '\0';} //������

			for (row=1; row<=N; row++) comp_data[row-1] = data[row][col];
			if (strstr(comp_data, comp_R) != NULL){
				flag_R = true;
//				printf("Suichoku");
			}
			if (strstr(comp_data, comp_B) != NULL){
				flag_B = true;
//				printf("Suichoku");
			}

		}

		//�΂߁i���ォ��E���j
		for (row=1; row<=N; row++){
			for (i=0; i<64; i++){ comp_data[i] = '\0';} //������

			for (col=1; col<=N; col++){
				if (data[row+col-1][col] == '\0') break;
				comp_data[col-1] = data[row+col-1][col];
			}
			if (strstr(comp_data, comp_R) != NULL){
				flag_R = true;
//				printf("Miginaname 1");
			}
			if (strstr(comp_data, comp_B) != NULL){
				flag_B = true;
//				printf("Miginaname 1");
			}
		}

		for (col=1; col<=N-K+1; col++){
			for (i=0; i<64; i++){ comp_data[i] = '\0';} //������

			for (row=1; row<=N-col+1; row++) comp_data[row-1] = data[row][col+row-1];
			if (strstr(comp_data, comp_R) != NULL){
				flag_R = true;
//				printf("Miginaname 2");
			}
			if (strstr(comp_data, comp_B) != NULL){
				flag_B = true;
//				printf("Miginaname 2");
			}
		}

		//�΂߁i�E�ォ�獶���j
		for (row=1; row<=N-K+1; row++){
			for (i=0; i<64; i++){ comp_data[i] = '\0';} //������

			for (col=N; col>=row; col--) comp_data[N-col] = data[row+(N-col)][col];
			if (strstr(comp_data, comp_R) != NULL) flag_R = true;
			if (strstr(comp_data, comp_B) != NULL) flag_B = true;
		}
		for (col=K; col<=N; col++){
			for (i=0; i<64; i++){ comp_data[i] = '\0';} //������

			for (row=1; row<=col; row++) comp_data[row-1] = data[row][col-row+1];
			if (strstr(comp_data, comp_R) != NULL) flag_R = true;
			if (strstr(comp_data, comp_B) != NULL) flag_B = true;
		}

		//���ʕ\��
		if (flag_R==false && flag_B==false){
			printf("Case #%d: Neither\n", cnt_T);
			fprintf(ofp,"Case #%d: Neither\n", cnt_T);
		}
		else if (flag_R==true && flag_B==false){
			printf("Case #%d: Red\n", cnt_T);
			fprintf(ofp,"Case #%d: Red\n", cnt_T);
		}
		else if (flag_R==false && flag_B==true){
			printf("Case #%d: Blue\n", cnt_T);
			fprintf(ofp,"Case #%d: Blue\n", cnt_T);
		}
		else if (flag_R==true && flag_B==true){
			printf("Case #%d: Both\n", cnt_T);
			fprintf(ofp,"Case #%d: Both\n", cnt_T);
		}
 

	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
