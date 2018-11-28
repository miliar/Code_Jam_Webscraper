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

	int B_from_A[10001];
	int T, N;
	int cnt_T, cnt_N, i, now;
	int intersection;

	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("%d\n", T);
	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		//N�̓ǂݍ���
		fscanf(fp, "%d", &N);
		printf("%d\n", N);

		//������
		for (i=0; i<=10000; i++){
			B_from_A[i] = 0;
		}
		intersection = 0;
		now = 0;

		//N�{�̃��C���̓ǂݍ���
		int buf1, buf2;
		for (cnt_N=1; cnt_N<=N; cnt_N++){
			fscanf(fp, "%d %d", &buf1, &buf2);
			B_from_A[buf1] = buf2;
		}

		for (now=1; now<=10000; now++){
			int now_B;
			now_B = B_from_A[now];
			if (now_B == 0) continue;

			for (i=1; i<now; i++){
				if (B_from_A[i] > now_B){
					intersection++;
				}
			}
		}

		//���ʕ\��
		printf("Case #%d: %d\n", cnt_T, intersection);
		fprintf(ofp,"Case #%d: %d\n", cnt_T, intersection);
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
