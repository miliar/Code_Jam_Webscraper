#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

int main(){
	//�t�@�C�����o�͕�
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
	int head; //�s��̐擪�ʒu
	int euro;
	int riding;

	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("%d\n", T);
	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		fscanf(fp, "%d %d %d", &R, &K, &N); //R��,K�l,N�O���[�v�̓ǂݍ���
		printf("%d %d %d\n", R, K, N);
		for (cnt_N=1; cnt_N<=N; cnt_N++){
			fscanf(fp, "%d", &gp[cnt_N]); //�O���[�v�̓ǂݍ���
			printf("%d ", gp[cnt_N]);
		}
		printf("\n");

		//������
		head = 1;
		euro = 0;
		skip_flag = false;


		//R�񏈗�
		int buf_head;
		for (cnt_R=1; cnt_R<=R; cnt_R++){
			riding = 0;
			buf_head = head;
			while (riding + gp[head] <= K){
				riding += gp[head];
				head++;
				if (head > N) head = 1;
				if (head == buf_head) break; //�q���S������Ă��܂���
			}
			euro += riding;
			
			//�v�Z���Ԃ�Z�����鏈��
			if (head != 1) continue;
			if (skip_flag == true) continue;
			skip_flag = true;
			euro = euro * int(R/cnt_R);
			R = R % cnt_R;
			cnt_R = 0;
			
		}

		//���ʕ\��
		printf("Case #%d: %d\n", cnt_T, euro);
		fprintf(ofp,"Case #%d: %d\n", cnt_T, euro);
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
