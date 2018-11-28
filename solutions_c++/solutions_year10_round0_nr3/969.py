#include <stdio.h>
#include <queue>

using namespace std;

typedef unsigned int u32;
typedef unsigned long long u64;

int main(void){

	FILE* fp = 0;
	FILE* out = 0;
	fp = fopen("prob.txt","rb");
	out = fopen("out.txt","wb");

	u32 maxRound = 0;

	fscanf( fp, "%u\n", &maxRound );
	//printf("%u\n",maxRound);

	for(u32 i = 0;i < maxRound;++i){

		// R k N を読み取る
		u32 runTimes = 0;
		u32 maxSeat = 0;
		u32 groupMax = 0;
		fscanf( fp, "%u %u %u\n", &runTimes, &maxSeat, &groupMax );

		// 待ち人と乗ってる人
		queue<u32> waitQueue;
		queue<u32> riderQueue;

		// グループを読み取る
		for(u32 z = 0;z < groupMax;++z){
			u32 group = 0;
			fscanf(fp,"%u",&group);
			waitQueue.push( group );
		}

		// よめてるー。
		// ではコースターに乗せられるだけ乗せて、
		// 走らせて、もどす、ってのを営業回数だけ繰り返す。
		u32 earn = 0;
		for(u32 k = 0;k < runTimes;++k){

			// waitQueue から maxSeat の限界まで引っ張り出す
			u32 currentSeat = 0;
			while( waitQueue.empty() == false ){

				// 今のグループを突っ込んだとして、
				// シート制限を越えるか越えないか？
				if( currentSeat + waitQueue.front() <= maxSeat ){

					// セーフ。乗っけてしまおう。
					currentSeat += waitQueue.front();
					riderQueue.push( waitQueue.front() );
					waitQueue.pop();

				}else{

					// あれ、もう乗れない。
					// 抜ける。
					break;

				}

			}

			// シートに限界まで乗ったようだ。
			// 走らせて、現金回収！
			earn += currentSeat;

			// んで、再び乗り待ちキューに乗っける
			while( riderQueue.empty() == false ){
				waitQueue.push( riderQueue.front() );
				riderQueue.pop();
			}
		}

		// 稼ぎの表示
		fprintf(out,"Case #%u: %u\n",i+1,earn);

	}

	fclose(fp);
	fclose(out);
}