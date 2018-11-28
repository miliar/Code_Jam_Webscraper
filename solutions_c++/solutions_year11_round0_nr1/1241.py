#include <stdio.h>

enum {

	BODY_O
	, BODY_B
	, BODY_TERM

};

int main(void)
{
	// 境界条件として、始点は 1,1 。
	// あとは移動主体が交代するときは直前に消費した時間を再利用できるという点に注意。

	// 問題数を取得
	int T = 0;
	scanf("%d",&T);

	// 問題を取得
	for(int round = 0;round < T;++round){

		// 問題が持つシーケンスの数
		int N = 0;
		scanf("%d",&N);

		// OB の位置を初期化
		int pos[BODY_TERM] = {1,1,};

		// 作業した時間
		int work = 0;

		// 残っている時間
		int rem = 0;

		// 直前の移動主体
		int lastOB = BODY_TERM;

		// かかる時間
		int totalTime = 0;
		
		// シーケンスの数だけループ
		for(int seq = 0;seq < N;++seq){

			// 今回の命令
			char rawBody;
			int targetPos;
			scanf(" %c %d",&rawBody,&targetPos);

			// 今回の移動主体を enum 化
			int body;
			switch( rawBody )
			{
			case 'O':
				body = BODY_O;
				break;
			default:
				body = BODY_B;
				break;
			}

			// 今回の移動とぽっちで消費する時間は主体変化など関係なく計算可能

			// 距離
			int time = targetPos - pos[body];
			if( time < 0 ) time = -time;

			// 移動しましたよっと
			pos[body] = targetPos;

			// 移動主体が切り替わったら直前の work を rem に計上できる
			// このとき rem はリセットされる
			if( lastOB != BODY_TERM && lastOB != body ){
				rem = work;
				work = 0;
			}

			// 残り時間の利用
			if( time <= rem ){
				rem -= time;
				time = 0;
			}else{
				time -= rem;
				rem = 0;
			}

			// ボタンぽっちによる同期があるので残り時間は１回しか使えない
			rem = 0;

			// ぽっち
			++time;

			// ごまかしきれなかった時間を計上
			work += time;
			totalTime += time;

			// 移動主体を更新
			lastOB = body;

		}

		// 結果の表示
		printf("Case #%d: %d\n",round+1,totalTime);

	}

	return 0;

}