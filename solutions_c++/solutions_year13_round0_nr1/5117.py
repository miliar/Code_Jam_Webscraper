#include <iostream>


using namespace std;

typedef long long int int64;


//jamA
int main(void)
{
	int nTestCase, repeat;
	int i, j;
	int xwon, owon, nBlank;

	char board[4][4];
	char ch;
	const char cX = 1; // X
	const char cO = 2; // O
	const char cT = 3; // T
	const char cB = 0; // blank

	cin >> nTestCase;
	for(repeat = 1; repeat <= nTestCase; repeat++){
		// ブランクのマスの数をゼロに初期化
		nBlank = 0;

		// テストケース番号出力
		cout << "Case #" << repeat << ": ";

		// ボード読み込み
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> ch;
				switch(ch){
					case 'X':
						board[i][j] = cX;
						break;
					case 'O':
						board[i][j] = cO;
						break;
					case 'T':
						board[i][j] = cT;
						break;
					case '.':
						board[i][j] = cB;
						nBlank++; // まだ空いているところがある。
						break;
					default:
						cout << "ERROR INPUT :" << ch << endl;
						return 0;
				}
			}
		}

		// 当たり判定
		xwon = 0;
		owon = 0;

		// Xの勝ち？
		xwon += cX & board[0][0] & board[1][1] & board[2][2] & board[3][3];
		xwon += cX & board[0][3] & board[1][2] & board[2][1] & board[3][0];
		for(i = 0; i < 4; i++){
			xwon += cX & board[i][0] & board[i][1] & board[i][2] & board[i][3];
			xwon += cX & board[0][i] & board[1][i] & board[2][i] & board[3][i];
		}

		// Oの勝ち？
		owon += cO & board[0][0] & board[1][1] & board[2][2] & board[3][3];
		owon += cO & board[0][3] & board[1][2] & board[2][1] & board[3][0];
		for(i = 0; i < 4; i++){
			owon += cO & board[i][0] & board[i][1] & board[i][2] & board[i][3];
			owon += cO & board[0][i] & board[1][i] & board[2][i] & board[3][i];
		}

		// どっちが勝ったかな？
		if(xwon == 0 && owon == 0){ // どっちもゼロ
			if(nBlank == 0){ // 空いているマスがないので引き分け
				cout << "Draw" << endl;
			}else{
				cout << "Game has not completed" << endl;
			}
		}else if(xwon > 0 && owon > 0){ // ありえないけど、両方ビンゴ
			cout << "Draw" << endl; // 引き分けでいいでしょ。
		}else if(xwon > 0){ // X勝ち！
			cout << "X won" << endl;
		}else{
			cout << "O won" << endl;
		}

	}


	return 0;
}

