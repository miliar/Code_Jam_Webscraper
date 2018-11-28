#include <stdio.h>

int main(void)
{
	// 巡回置換を見つけて、(位数 - 1)x2 がソート回数期待値になる

	int T = 0;
	scanf("%d",&T);

	int n[2000];
	int b[2000];

	for(int round = 0;round < T;++round){
		int N = 0;
		scanf("%d",&N);
		for(int i = 0;i < N;++i){
			scanf("%d",&(n[i]));
			b[i] = 0;
		}

		// まだループが見つかっていない場所から順にサーチ
		int totalRank = 0;
		int rank = 0;
		for(int i = 0;i < N;++i){

			if(b[i] == 0){

				// ここまだ未サーチです。
				// これからループが形成されているか調べます。
				int start = i+1;
				int now = i+1;

				// now が n[now-1] に置換されている。
				// n[now-1] == start なら終了。
				// 違っていたら位数を増やして n = n[now-1] としてもう一回。
				rank = 1;
				while(n[now-1] != start){
					++rank;
					b[now-1] = 1;
					now = n[now-1];
				}
				b[now-1] = 1;

				totalRank += rank == 1 ? 0 : rank;//(rank - 1)*2;

			}

		}

		//for(int i = 0;i < N;++i){
		//	printf("%d",n[i]);
		//}printf("\n");

		printf("Case #%d: %d\n",round+1,totalRank);
	}

	return 0;
}