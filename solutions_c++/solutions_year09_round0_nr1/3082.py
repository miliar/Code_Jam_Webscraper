#include <stdio.h>
#include <windows.h>
#include "������.h"
#include "�t�@�C��.h"

int main(void){

	char *filename="C:/�܂Ƃ�/�_�E�����[�h/A-large.in";
	char *�o�b�t�@=�t�@�C��::���[�h(filename);
	if(�o�b�t�@==NULL){
		return -1;
	}

	char *filename2="C:/�܂Ƃ�/�_�E�����[�h/A-large.out";
	FILE *file=fopen(filename2,"wb");
	if(file==NULL){
		free(�o�b�t�@);
		return -1;
	}

	char *������=�o�b�t�@;

	unsigned long L=������::���l�ɕϊ�_long(������);������=������::����(������," ");������++;
	unsigned long D=������::���l�ɕϊ�_long(������);������=������::����(������," ");������++;
	unsigned long N=������::���l�ɕϊ�_long(������);������=������::����(������,"\n");������++;

	char *����=������;//[16*5000];
	char *�p�^�[��=����+(L+1)*D;


	char *������1,*������2,*������3;
	unsigned long ��1=L+1;

	unsigned char �t���O[5010];
	unsigned char �t���O2;

	unsigned long ��;

	unsigned long i,j,k;
	������1=�p�^�[��;
	for(i=1;i<=N;i++){

		//
		memset(�t���O,1,D);
		for(j=0;j<L;j++){
			if(*������1=='('){
				������1++;
				������2=����+j;
				for(k=0;k<D;k++,������2+=��1){
					if(�t���O[k]){
						�t���O2=0;
						������3=������1;
						while(*������3!=')'){
							if(*������2==*������3){
								�t���O2=1;
								break;
							}
							������3++;
						}
						if(�t���O2==0)�t���O[k]=0;
					}
				}
				������1=������::����(������1,")");
				//������1++;
			}else{
				������2=����+j;
				for(k=0;k<D;k++,������2+=��1){
					if(*������2!=*������1){
						�t���O[k]=0;
					}
				}
			}
			������1++;
		}
		������1++;//\n

		//
		��=0;
		for(j=0;j<D;j++){
			if(�t���O[j])��++;
		}

		//
		fprintf(file,"Case #%d: %d\n",i,��);
	}

	fclose(file);
	free(�o�b�t�@);

	return 0;
}
