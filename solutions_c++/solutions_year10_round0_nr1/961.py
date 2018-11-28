#include <stdio.h>

typedef unsigned int u32;

int main(void){

	FILE* fp = 0;
	FILE* out = 0;
	fp = fopen("prob.txt","rb");
	out = fopen("out.txt","wb");

	u32 maxRound = 0;

	fscanf( fp, "%u\n", &maxRound );
	//printf("%u\n",maxRound);

	for(u32 i = 0;i < maxRound;++i){
		u32 light = 0;
		u32 snap = 0;
		fscanf( fp, "%u %u\n", &light, &snap );
		//printf("%d %d\n",light,snap);

		// ライトが全部リセットされるスナップ回数
		const u32 cycleSnap = 1 << light;

		// 次のスナップでリセットがかかるならそれはライトへ通電している状態
		const u32 validSnap = (snap + 1) % cycleSnap;

		fprintf(out,"Case #%u: %s\n", i+1, validSnap == 0 ? "ON" : "OFF");
	}

	fclose(fp);
	fclose(out);
}