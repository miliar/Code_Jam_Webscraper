#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <string>
#include <set>

using namespace std;

typedef unsigned int u32;
typedef signed int s32;
struct Wire { s32 from; s32 to; };

#define ANY ' '
#define EMPTY '_'

int main(void){

	FILE* fp = 0;
	FILE* out = 0;
	fp = fopen("prob.txt","rb");
	out = fopen("out.txt","wb");
	char dia[2][300][300];
	

	u32 maxRound = 0;
	char line[1024];

	fscanf( fp, "%u\n", &maxRound );
	//printf("%u\n",maxRound);

	for(u32 round = 0;round < maxRound;++round){

		// バクテリア定義領域数
		s32 linenum = 0;
		fscanf(fp,"%d\n",&linenum);

		// 領域初期化
		int cur = 0;
		int next = 1 - cur;
		memset(dia,EMPTY,sizeof(char)*300*300*2);

		// バクテリア定義
		for(int i = 0;i < linenum;++i){
			s32 x1,x2;
			s32 y1,y2;
			fscanf(fp,"%d %d %d %d\n",&x1,&y1,&x2,&y2);
			if( x1 > x2 ){
				x1 ^= x2;
				x2 ^= x1;
				x1 ^= x2;
			}
			if( y1 > y2 ){
				y1 ^= y2;
				y2 ^= y1;
				y1 ^= y2;
			}
			// バクテリアセット
			for(int r = y1;r <= y2;r++){
				for(int c = x1;c <= x2;++c){
					dia[cur][r][c] = 'o';
				}
			}
		}

		// 計算
		bool exist = false;
		int ans = 0;
		do{
			++ans;

			// 世代交代
			bool gen = false;
			exist = false;
			for(int r = 1;r <= 100;++r){
				for(int c = 1;c <= 100;++c){

					// 生成チェック
					if( dia[cur][r][c] == EMPTY ){
						if( dia[cur][r-1][c] != EMPTY && dia[cur][r][c-1] != EMPTY ){
							gen = true;
							dia[next][r][c] = 'o';
						}else{
							dia[next][r][c] = EMPTY;
						}
					}else if( dia[cur][r][c] != EMPTY ){
						// 消滅チェック
						if( dia[cur][r-1][c] == EMPTY && dia[cur][r][c-1] == EMPTY ){
							dia[next][r][c] = EMPTY;
						}else{
							// 生き残った
							exist = true;
							dia[next][r][c] = 'o';
						}
					}

				}
			}

			//printf("CURRENT\n");
			//for(int r = 1;r <= 10;++r){
			//	for(int c = 1;c <= 10;++c){
			//		printf("%c",dia[cur][r][c]);
			//	}printf("\n");
			//}printf("\n");
			//printf("NEXT\n");
			//for(int r = 1;r <= 10;++r){
			//	for(int c = 1;c <= 10;++c){
			//		printf("%c",dia[next][r][c]);
			//	}printf("\n");
			//}printf("\n");
			//printf("\n");

			exist = exist | gen;
			cur = !cur;
			next = 1 - cur;

		}while(exist);

		//for(int i = 0;i < linenum;++i){
		//	printf("%s\n",dia[i]);
		//}


		fprintf(out,"Case #%u: %d\n", round+1, ans);
	}

	fclose(fp);
	fclose(out);
}