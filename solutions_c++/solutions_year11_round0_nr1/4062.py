#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

int MoveRobots(vector<int> &button, vector<char> &robot, int &num)
{
	int curPosB = 1;
	int curPosO = 1;
	int destPos = 1;
	int time = 0;
	bool isClear = false;
	vector<bool> isPressed(num);
	//vector<char>::iterator iteB = find(robot.begin(), robot.end(), 'O');
	//vector<char>::iterator iteB = find(robot.begin(), robot.end(), 'B');
	int curDest = 0;// index

	while(!isClear) {
		if (!isPressed[curDest]) {
			vector<char>::iterator iteO = find(robot.begin() + curDest, robot.end(), 'O');	// .begin()���ƍŏ�����ɂȂ邩��...
			vector<char>::iterator iteB = find(robot.begin() + curDest, robot.end(), 'B');
			int indexB = iteB - robot.begin();	// debug
			int indexO = iteO - robot.begin();	// debug

			if (robot[curDest] == 'O') { //|| (ite != robot.end() && *ite != 1)) {			// 'O'�������āA1����Ȃ�������i��ł���.
				// Orange�����C�����̎��̍s��: �ړI�n�Ɋ��ɂ����牟���A���Ȃ������������.
				if (curPosO == button[curDest]) {
					isPressed[curDest] = true;											// 1�ڂ̃T���v���ł͂����ƑS���������I�������! time�������Ă�
					curDest++;
				}
				else (button[curDest] > curPosO) ? curPosO++ : curPosO--;//curPosO++;															// button�̈ʒu�ɂ��Ȃ��Ȃ�i�܂���I
				// Blue�̍s��:	���i���ݑ������������Ă�button�̓Y���̎��ȍ~�Łj��'B'���Ɍ����Ă����āA�����܂łȂ�ׂ��i��ł���.
				if (indexB < button.size()) destPos = button[iteB - robot.begin()];	// �I��鎞�ɂ����ŃG���[���o�Ă��܂�(index�I�ȈӖ���)	// �ǉ�
				if (curPosB != destPos) 
					(destPos > curPosB) ? curPosB++ : curPosB--;	
			}
			else if (robot[curDest] == 'B') {
				// Blue�����C���F
				if (curPosB == button[curDest]) {
					isPressed[curDest] = true;
					curDest++;
				}
				else (button[curDest] > curPosB) ? curPosB++ : curPosB--;//curPosB++;
				// ���̎���Orange:
				if (indexO < button.size()) destPos = button[iteO - robot.begin()];
				if (curPosO != destPos) 
					(destPos > curPosO) ? curPosO++ : curPosO--;
			}
		}
		time++;

		if (curDest > isPressed.size() - 1)//isPressed.size())   3
			isClear = true;
		int test = isPressed.size() - 1;// 3�ō����Ă�
		//for(int i = 0; i < isPressed.size(); i++)
		//	if (isPressed[i])
		//if (count(isPressed.begin(), isPressed.end(), true) == isPressed.size())
		//	isClear = true;
	}

	return time;
}

int main() {
	ifstream cin("A-large.in");	// cin���t�@�C���Ɋ��蓖�ĂāA��͕��ʂɎg��.
	ofstream ofs("A-largeO.txt");

	int n, num, second;
	vector<int> button;
	vector<char> robot;

	cin >> n;
	//vector<int> second(n);
	for(int i = 0; i < n; i++) {
		cin >> num;
		button.resize(num);
		robot.resize(num);
		for (int j = 0; j < num; j++) {
			cin >> robot[j] >> button[j];
		}
		second = MoveRobots(button, robot, num);
		//cout << "Case #" << i + 1 << ": " << second << endl;
		ofs << "Case #" << i + 1 << ": " << second << endl;
	}
}

	

	