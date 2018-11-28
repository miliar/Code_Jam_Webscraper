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

	int T, R, C;
	int cnt_T, cnt_R, cnt_C;
	char data[51][51];
	bool impossible;

	fscanf(fp, "%d", &T); //T�̓ǂݍ���
	printf("T:%d", T);

	for (cnt_T=1; cnt_T<=T; cnt_T ++){
		impossible = false;

		//R,C�̓ǂݍ���
		fscanf(fp, "\n%d %d\n", &R, &C);
		printf("\n R:%d, C:%d", R, C);

		//�f�[�^�̓ǂݍ���
		for (cnt_R=1; cnt_R<=R; cnt_R++){
			for (cnt_C=1; cnt_C<=C; cnt_C++){
				fscanf(fp, "%c", &data[cnt_R][cnt_C]);
			}
			fscanf(fp, "\n");
		}

		//Main
		for (cnt_R=1; cnt_R<=R; cnt_R++){
			for (cnt_C=1; cnt_C<=C; cnt_C++){
				
				//��(#)����Ȃ�������B�B�B
				if (data[cnt_R][cnt_C] != '#') continue;

				//������������ւ��ł��Ȃ�������B�B�B
				if (cnt_R == R || cnt_C == C || 
					(data[cnt_R+1][cnt_C] != '#' || 
					 data[cnt_R][cnt_C+1] != '#' || 
					 data[cnt_R+1][cnt_C+1] != '#')){

						 impossible = true;
						 goto Label1;
				}

				//�œ���ւ��ł���Ȃ�B�B�B
				data[cnt_R][cnt_C] = '/';
				data[cnt_R+1][cnt_C] = '\\';
				data[cnt_R][cnt_C+1] = '\\';
				data[cnt_R+1][cnt_C+1] = '/';
			}
		}

Label1:

		//���ʏo��
		fprintf(ofp,"Case #%d:\n", cnt_T);

		if (impossible == true){
			fprintf(ofp,"Impossible\n");
		}
		else{
			//�f�[�^�̓ǂݍ���
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
	scanf("%s", filename); //�I���O�̓��͑҂�
	return 0;
}
