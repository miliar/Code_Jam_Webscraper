#include <stdio.h>

int main(void)
{
	// ビットで全パターンを巡って、 xor する。
	// でも N=1000 とか耐えられる気がしない。

	int T = 0;
	scanf("%d",&T);
	int c[2000];
	int b[2000];

	for(int round = 0;round < T;++round){

		int N = 0;
		scanf("%d",&N);
		for(int i = 0;i < N;++i){
			scanf("%d",&(c[i]));
			b[i]=0;
		}

		//for(int i =0;i < N;++i){
		//	printf("%d ",c[i]);
		//}
		//printf("\n");

		int prize = 0;

		b[0] = 1;

		for(;;){

			bool toBeContinued = false;
			for(int i = 0;i < N - 1;++i){
				if( b[i] == 1 ){
					toBeContinued = true;
					break;
				}
			}

			//for(int i = 0;i < N;++i){
			//	printf("%d",b[i]);
			//}
			//printf("\n");

			if( toBeContinued == false ){
				if( b[N-1] == 1 ){
					break;
				}
			}

			// 分け合ってみよう。どうかな？
			int xor[2] = {0,};
			int sum[2] = {0,};
			for(int i = 0;i < N;++i){
				xor[ b[i] ] ^= c[i];
				sum[ b[i] ] += c[i];
			}

			// 割れていたら大きい方をもらう
			if( xor[0] == xor[1] ){
				int res = sum[0] > sum[1] ? sum[0] : sum[1];
				prize = prize > res ? prize : res;
			}

			// 次の組み合わせどうぞー
			for(int i = 0;i < N;++i){
				if( b[i] == 0 ){
					b[i] = 1;
					break;
				}
				b[i] = 0;
			}
		}

		if( prize ){
			printf("Case #%d: %d\n",round+1,prize);
		}else{
			printf("Case #%d: NO\n",round+1);
		}
	}

	return 0;
}