// GCJJ2011.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <stdio.h>
#include <stdlib.h>
enum RobotColor {O,B};
struct Sequence{
	RobotColor color;
	int buttonPos;
};
// 次のシーケンス番号を探索する
int searchNextSeq(int nowseqnum, RobotColor col, Sequence* seq, int seqmax) 
{
	for (int i = nowseqnum+1; i < seqmax; i++) {
		if(seq[i].color == col) {
			return i;
		}
	}
	return seqmax;
}
int main(int argc, char* argv[])
{
	FILE* fp;
	int TestcaseNum;
	int SequenceNum[100];
	char str[100];
	Sequence seq[100][100];
	
	//問題文の読み込み
	fp = fopen("A-large.in", "r");
	if (fp == NULL) {
		return -1;
	}
	//1行目：問題数を読む
	fscanf(fp, "%d", &TestcaseNum);

	for (int j = 0; j < TestcaseNum; j++) {
		//行頭：シーケンス数を読む
		fscanf(fp, "%d", &SequenceNum[j]);
		for (int i = 0; i < SequenceNum[j]; i++) {
			//ロボ色(O/B)
			fscanf(fp, "%s%d", str, &seq[j][i].buttonPos);
			if(str[0] == 'O') {
				seq[j][i].color = O;
			} else {
				seq[j][i].color = B;
			}
		}
	}
	fclose(fp);

	fp = fopen("output.txt","w");
	

	for (int testcase = 0; testcase < TestcaseNum; testcase++) {
		// 初期位置
		int OrangePos,BluePos;
		OrangePos = BluePos = 1;
		int OrangeTargetSeq, BlueTargetSeq;
		int OrangeNextSeq, BlueNextSeq;
		OrangeTargetSeq = searchNextSeq(-1, O, seq[testcase], 100);
		BlueTargetSeq = searchNextSeq(-1, B, seq[testcase], 100);

		int time = 0;
		int step = 0;//成功すると加算

		while(1) {
			OrangeNextSeq = OrangeTargetSeq;
			BlueNextSeq = BlueTargetSeq;

			time ++;
			if (OrangePos > seq[testcase][OrangeTargetSeq].buttonPos) {
				OrangePos--;
			} else if(OrangePos < seq[testcase][OrangeTargetSeq].buttonPos) {
				OrangePos++;
			} else {
				if (OrangeTargetSeq < BlueTargetSeq) {
					OrangeNextSeq = searchNextSeq(OrangeTargetSeq, O, seq[testcase], 100);
					step++;
				}
			}
			if (BluePos > seq[testcase][BlueTargetSeq].buttonPos) {
				BluePos--;
			} else if(BluePos < seq[testcase][BlueTargetSeq].buttonPos) {
				BluePos++;
			} else {
				if (BlueTargetSeq < OrangeTargetSeq) {
					BlueNextSeq = searchNextSeq(BlueTargetSeq, B, seq[testcase], 100);
					step++;
				}
			}
 			OrangeTargetSeq = OrangeNextSeq;
			BlueTargetSeq = BlueNextSeq;

			if (step >= SequenceNum[testcase])
			{
				break;
			}
		}
		fprintf(fp, "Case #%d: %d\n", testcase+1, time);
	}
	fclose(fp);
	return 0;
}

