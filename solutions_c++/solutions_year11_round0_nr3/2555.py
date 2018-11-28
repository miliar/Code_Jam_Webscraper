#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


long my_add(long input1, long input2){
	long output = 0;
	output = input1 ^ input2; //XOR���Z�q
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

	printf("3^5^6 = %d\n", (3^5^6));
	int T, N;
	long C;
	int cnt_T, cnt_N;
	long min_C, sum_C, skew_sum;

	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("%d", T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		sum_C = 0;
		skew_sum = 0;

		//N�̓ǂݍ���
		fscanf(fp, "\n%d\n", &N);
		printf("\nN=%d\n", N);

		for (cnt_N=1; cnt_N<=N; cnt_N++){
			//C�̓ǂݍ���
			if (cnt_N==1) fscanf(fp, "%ld", &C);
			else fscanf(fp, " %ld", &C);

			printf("%d ", C);

			skew_sum = my_add(skew_sum, C);
			sum_C += C;


			if (cnt_N == 1 || C < min_C) min_C = C; //C�̍ŏ��l��ۑ�
		}

		printf("skew_sum = %ld, sum_C = %ld, min_C = %ld", skew_sum, sum_C, min_C);
		if (skew_sum == 0){
			//���܂���I
			fprintf(ofp,"Case #%d: %ld\n", cnt_T ,sum_C - min_C);
		} else {
			//���܂��Ȃ��I
			fprintf(ofp,"Case #%d: NO\n", cnt_T);
		}
	}

	//
	fclose(fp);fclose(ofp);
	printf("\nProngram is finished. Please enter a letter.\n");
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
