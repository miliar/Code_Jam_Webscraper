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

bool test(Wire& a, Wire& b){

	s32 v1 = (b.to - a.from) - (a.to - a.from);
	s32 v2 = (b.from - a.from);

	return v1*v2 < 0;

}

u32 calc(Wire* w, u32 num){

	u32 ans = 0;

	for(u32 i = 0;i < num-1;++i){
		for(u32 g = 1;g < num;++g){

			if(test(w[i],w[g])){
				++ans;
			}

		}
	}

	return ans;

}

int main(void){

	FILE* fp = 0;
	FILE* out = 0;
	fp = fopen("prob.txt","rb");
	out = fopen("out.txt","wb");

	u32 maxRound = 0;
	char line[1024];
	Wire w[1010];

	fscanf( fp, "%u\n", &maxRound );
	//printf("%u\n",maxRound);

	for(u32 i = 0;i < maxRound;++i){

		// 何本あるかなー
		u32 num = 0;
		fscanf(fp, "%d\n", &num);

		// ワイヤ構築
		for(u32 g = 0;g < num;++g){
			fscanf(fp,"%d %d\n",&(w[g].from),&(w[g].to));
		}

		// 交差計算
		u32 ans = calc(w,num);

		fprintf(out,"Case #%u: %d\n", i+1, ans);
	}

	fclose(fp);
	fclose(out);
}