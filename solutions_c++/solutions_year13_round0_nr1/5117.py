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
		// �u�����N�̃}�X�̐����[���ɏ�����
		nBlank = 0;

		// �e�X�g�P�[�X�ԍ��o��
		cout << "Case #" << repeat << ": ";

		// �{�[�h�ǂݍ���
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
						nBlank++; // �܂��󂢂Ă���Ƃ��낪����B
						break;
					default:
						cout << "ERROR INPUT :" << ch << endl;
						return 0;
				}
			}
		}

		// �����蔻��
		xwon = 0;
		owon = 0;

		// X�̏����H
		xwon += cX & board[0][0] & board[1][1] & board[2][2] & board[3][3];
		xwon += cX & board[0][3] & board[1][2] & board[2][1] & board[3][0];
		for(i = 0; i < 4; i++){
			xwon += cX & board[i][0] & board[i][1] & board[i][2] & board[i][3];
			xwon += cX & board[0][i] & board[1][i] & board[2][i] & board[3][i];
		}

		// O�̏����H
		owon += cO & board[0][0] & board[1][1] & board[2][2] & board[3][3];
		owon += cO & board[0][3] & board[1][2] & board[2][1] & board[3][0];
		for(i = 0; i < 4; i++){
			owon += cO & board[i][0] & board[i][1] & board[i][2] & board[i][3];
			owon += cO & board[0][i] & board[1][i] & board[2][i] & board[3][i];
		}

		// �ǂ��������������ȁH
		if(xwon == 0 && owon == 0){ // �ǂ������[��
			if(nBlank == 0){ // �󂢂Ă���}�X���Ȃ��̂ň�������
				cout << "Draw" << endl;
			}else{
				cout << "Game has not completed" << endl;
			}
		}else if(xwon > 0 && owon > 0){ // ���肦�Ȃ����ǁA�����r���S
			cout << "Draw" << endl; // ���������ł����ł���B
		}else if(xwon > 0){ // X�����I
			cout << "X won" << endl;
		}else{
			cout << "O won" << endl;
		}

	}


	return 0;
}

