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
			vector<char>::iterator iteO = find(robot.begin() + curDest, robot.end(), 'O');	// .begin()だと最初からになるから...
			vector<char>::iterator iteB = find(robot.begin() + curDest, robot.end(), 'B');
			int indexB = iteB - robot.begin();	// debug
			int indexO = iteO - robot.begin();	// debug

			if (robot[curDest] == 'O') { //|| (ite != robot.end() && *ite != 1)) {			// 'O'があって、1じゃなかったら進んでおく.
				// Orangeがメイン時の時の行動: 目的地に既にいたら押す、いなかったら向かう.
				if (curPosO == button[curDest]) {
					isPressed[curDest] = true;											// 1つ目のサンプルではちゃんと全部押した！やったね! timeも合ってる
					curDest++;
				}
				else (button[curDest] > curPosO) ? curPosO++ : curPosO--;//curPosO++;															// buttonの位置にいないなら進ませる！
				// Blueの行動:	次（現在相方が向かってるbuttonの添字の次以降で）の'B'を先に見つけておいて、そこまでなるべく進んでおく.
				if (indexB < button.size()) destPos = button[iteB - robot.begin()];	// 終わる時にここでエラーが出てしまう(index的な意味で)	// 追加
				if (curPosB != destPos) 
					(destPos > curPosB) ? curPosB++ : curPosB--;	
			}
			else if (robot[curDest] == 'B') {
				// Blueがメイン：
				if (curPosB == button[curDest]) {
					isPressed[curDest] = true;
					curDest++;
				}
				else (button[curDest] > curPosB) ? curPosB++ : curPosB--;//curPosB++;
				// その時のOrange:
				if (indexO < button.size()) destPos = button[iteO - robot.begin()];
				if (curPosO != destPos) 
					(destPos > curPosO) ? curPosO++ : curPosO--;
			}
		}
		time++;

		if (curDest > isPressed.size() - 1)//isPressed.size())   3
			isClear = true;
		int test = isPressed.size() - 1;// 3で合ってた
		//for(int i = 0; i < isPressed.size(); i++)
		//	if (isPressed[i])
		//if (count(isPressed.begin(), isPressed.end(), true) == isPressed.size())
		//	isClear = true;
	}

	return time;
}

int main() {
	ifstream cin("A-large.in");	// cinをファイルに割り当てて、後は普通に使う.
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

	

	