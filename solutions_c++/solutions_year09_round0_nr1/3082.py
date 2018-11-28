#include <stdio.h>
#include <windows.h>
#include "文字列.h"
#include "ファイル.h"

int main(void){

	char *filename="C:/まとめ/ダウンロード/A-large.in";
	char *バッファ=ファイル::ロード(filename);
	if(バッファ==NULL){
		return -1;
	}

	char *filename2="C:/まとめ/ダウンロード/A-large.out";
	FILE *file=fopen(filename2,"wb");
	if(file==NULL){
		free(バッファ);
		return -1;
	}

	char *文字列=バッファ;

	unsigned long L=文字列::数値に変換_long(文字列);文字列=文字列::検索(文字列," ");文字列++;
	unsigned long D=文字列::数値に変換_long(文字列);文字列=文字列::検索(文字列," ");文字列++;
	unsigned long N=文字列::数値に変換_long(文字列);文字列=文字列::検索(文字列,"\n");文字列++;

	char *辞書=文字列;//[16*5000];
	char *パターン=辞書+(L+1)*D;


	char *文字列1,*文字列2,*文字列3;
	unsigned long 次1=L+1;

	unsigned char フラグ[5010];
	unsigned char フラグ2;

	unsigned long 数;

	unsigned long i,j,k;
	文字列1=パターン;
	for(i=1;i<=N;i++){

		//
		memset(フラグ,1,D);
		for(j=0;j<L;j++){
			if(*文字列1=='('){
				文字列1++;
				文字列2=辞書+j;
				for(k=0;k<D;k++,文字列2+=次1){
					if(フラグ[k]){
						フラグ2=0;
						文字列3=文字列1;
						while(*文字列3!=')'){
							if(*文字列2==*文字列3){
								フラグ2=1;
								break;
							}
							文字列3++;
						}
						if(フラグ2==0)フラグ[k]=0;
					}
				}
				文字列1=文字列::検索(文字列1,")");
				//文字列1++;
			}else{
				文字列2=辞書+j;
				for(k=0;k<D;k++,文字列2+=次1){
					if(*文字列2!=*文字列1){
						フラグ[k]=0;
					}
				}
			}
			文字列1++;
		}
		文字列1++;//\n

		//
		数=0;
		for(j=0;j<D;j++){
			if(フラグ[j])数++;
		}

		//
		fprintf(file,"Case #%d: %d\n",i,数);
	}

	fclose(file);
	free(バッファ);

	return 0;
}
