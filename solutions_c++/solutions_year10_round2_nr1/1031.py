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

typedef vector< string > Strings;

const u32 EMPTY = 0;
const u32 RED = 1;
const u32 BLUE = 2;
u32 field[50][50];

s32 calcmkdir( Strings& ready, string& targetRaw ){

	// ターゲットの深さを計算する
	u32 depth = 0;
	u32 pos = 0;
	while(pos < targetRaw.length()){
		pos = targetRaw.find('/',pos);
		if( pos < targetRaw.length() ){
			++depth;
			++pos;
		}
	}

	string target = targetRaw + "/";

	// ready の中に target と部分一致するものがあるか調べる
	u32 mkdir = 0;
	for(u32 i = 0;i < depth;++i){
		for(Strings::iterator g = ready.begin();g != ready.end();++g){
			//printf("[%s] vs [%s]\n",g->c_str(),target.c_str());
			if(g->find(target) == 0){
				ready.push_back(targetRaw+"/");
				return mkdir;
			}else if(*g == target){
				ready.push_back(targetRaw+"/");
				return mkdir;
			}
		}
		// みつからないらしい。
		// ディレクトリをひとつ浅くしてみる。

		// / をリバースファインド
		u32 rfindres = target.rfind('/');

		// 末尾の / を削る
		if( rfindres < target.length() ){
			target = target.substr(0,rfindres);
		}

		// / をリバースファインド
		rfindres = target.rfind('/');

		// / の次を閉じておく
		if( rfindres < target.length() - 1 ){
			target = target.substr(0,rfindres+1);
		}

		++mkdir;
	}

	ready.push_back(targetRaw+"/");
	return mkdir;

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

		s32 ready = 0;
		s32 target = 0;

		fscanf(fp,"%d %d\n",&ready,&target);

		// すでにあるディレクトリの読み込み
		Strings readyDir;
		for(s32 g = 0;g < ready;g++){
			fscanf(fp,"%s\n",line);
			readyDir.push_back( string(line) + "/" );
		}

		// 作りたいディレクトリを読み取りつつ mkdir をカウント
		u32 mkdir = 0;
		for(s32 g = 0;g < target;++g){
			fscanf(fp,"%s\n",line);
			mkdir += calcmkdir( readyDir, string(line) );
		}

		fprintf(out,"Case #%u: %d\n", i+1, mkdir);
	}

	fclose(fp);
	fclose(out);
}