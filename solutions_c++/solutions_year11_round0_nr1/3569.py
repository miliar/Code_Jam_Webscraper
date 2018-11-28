#include <iostream>
#include <map>
#include <cstdlib>

using namespace std;

int main() {
	int T, N, pos;
	map<char,int> currentPos, timeLast;
	char color;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cin >> N;
		int time, moveTime;
		currentPos['B'] = currentPos['O'] = 1;
		timeLast['B'] = timeLast['O'] = 0;
		time = 0;
		moveTime = 0;
		for(int j = 0; j < N; j++) {
			cin >> color >> pos;
			moveTime = abs(pos - currentPos[color]);
			if(moveTime <= time - timeLast[color]) time++;
			else time = timeLast[color] + moveTime + 1;
			timeLast[color] = time;
			currentPos[color] = pos;
		}
		cout << "Case #" << i << ": " << time << "\n";
	}
}
