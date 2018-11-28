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
typedef unsigned char u8;

u8 field[600][600];
u32 ans[600];

#define EMPTY 2
#define W 1
#define B 0

bool check( u32 baseR, u32 baseC, u32 size ){

	if( size <= 1 ){
		return field[baseR][baseC] != EMPTY;
	}

	u32 prevBaseR = field[baseR][baseC];
	u32 prevBaseC = field[baseR][baseC];

	for(u32 r = 0;r < size;++r){
		if( r >= 1 ){
			if( prevBaseR == field[baseR+r][baseC] ){
				return false;
			}else if( field[baseR+r][baseC] == EMPTY ){
				return false;
			}
		}
		prevBaseR = field[baseR + r][baseC];
		for(u32 c = 0;c < size;++c){
			if( field[baseR+r][baseC+c] == EMPTY ){
				return false;
			}
			if( c >= 1 ){
				if( prevBaseC == field[baseR+r][baseC+c] ){
					return false;
				}
			}
			prevBaseC = field[baseR+r][baseC+c];
		}
	}

	// ok
	for(u32 r = 0;r < size;++r){
		for(u32 c = 0;c < size;++c){
			field[baseR+r][baseC+c] = EMPTY;
		}
	}

	return true;

}

int main(void){

	FILE* fp = 0;
	FILE* out = 0;
	fp = fopen("prob.txt","rb");
	out = fopen("out.txt","wb");

	u32 maxRound = 0;
	char line[1024];

	fscanf( fp, "%u\n", &maxRound );
	//printf("%u\n",maxRound);

	for(u32 i = 0;i < maxRound;++i){

		// 次元
		u32 w,h;
		fscanf(fp,"%u %u\n",&h,&w);

		u32 maxSize = std::min(w,h);

		// ボードデータ
		for(u32 g = 0;g < h;++g){
			memset(field[g],EMPTY,600);
			fscanf(fp,"%s\n",line);
			// 文字をひとつずつ16進と解釈してく
			for(u32 z = 0;z < w/4;++z){
				int ch = line[z];
				u32 val = 0;
				if( ch <= '9' ){
					val = ch - '0';
				}else{
					val = ch - 'A' + 10;
				}

				// 解釈した文字をフィールドに当てはめる
				field[g][z*4 + 0] = (val >> 3) & 1;
				field[g][z*4 + 1] = (val >> 2) & 1;
				field[g][z*4 + 2] = (val >> 1) & 1;
				field[g][z*4 + 3] = (val >> 0) & 1;
			}
		}

		//for(u32 r = 0;r < h;++r){
		//	for(u32 c = 0;c < w;++c){
		//		printf("%c",field[r][c] == W ? 'W' : (field[r][c] == B ? 'B' : 'e'));
		//	}printf("\n");
		//}printf("\n\n");

		// 調べる
		u32 typeNum = 0;
		memset(ans,0,600*sizeof(u32));

		// 大きいのから単純に
		for(u32 size = maxSize;size > 0;--size){

			for(u32 r = 0;r < h-size+1;++r){
				for(u32 c = 0;c < w-size+1;++c){

					if( check( r, c, size ) ){
						if(ans[size] == 0){
							++typeNum;
						}
						++ans[size];
					}

				}
			}

		}

		fprintf(out,"Case #%u: %d\n", i+1, typeNum);
		for(u32 size = maxSize;size > 0;--size){
			if( ans[size] > 0 ){
				fprintf(out,"%u %u\n", size, ans[size]);
			}
		}
	}

	fclose(fp);
	fclose(out);
}