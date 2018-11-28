#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Robot {
	int stepsUsed;
	int currentPos;
	queue<int> moveSeq;

public:
	Robot() : stepsUsed(0), currentPos(1), moveSeq() {};

	int moveTo(int newPos, int maxSteps = -1) {
		int neededSteps = newPos - currentPos;

		int actualSteps = maxSteps != -1
			? min(abs(maxSteps), abs(neededSteps))
			: abs(neededSteps);

		currentPos += neededSteps >= 0
			? (actualSteps)
			: (-actualSteps);

		return actualSteps;
	}
	
	void finishPos() {
		moveSeq.pop();
	}

	void addMove(int button) {
		moveSeq.push(button);
	}
		
	int doNextStepUnlimited() {
		if (hasNextPos()) {
			int totalSteps = moveTo(nextPos(), -1);
			finishPos(); ++totalSteps; // press button
			stepsUsed += totalSteps;
			return totalSteps;
		}
		return 0;
	}

	int doNextStepTimed(int maxSteps) {
		if (hasNextPos()) {
			int totalSteps = moveTo(nextPos(), maxSteps);
			stepsUsed += totalSteps;
			return totalSteps;
		}
		return 0;
	}

	int hasNextPos() {
		return !moveSeq.empty();
	}

	int nextPos() {
		return moveSeq.front();
	}

	int totalStepsTaken() {
		return stepsUsed;
	}
};

inline int robotIndex(string color)
{
	return color == "O";
}

int main() 
{
	ios_base::sync_with_stdio(false);

	int testCases;
	cin >> testCases;

	for (int testCase = 1; testCase <= testCases; ++testCase) {
		vector<pair<int, int> > seq;
		int seqSize;
		Robot robot[2];

		cin >> seqSize;
		if (!cin) break;
		
		for (int i = 0; i < seqSize; ++i) {
			string color;
			int button;
			cin >> color >> button;
			
			int index = robotIndex(color);
			Robot& r = robot[index];
			r.addMove(button);
			seq.push_back(make_pair(index, button));
		}

		int tot = 0;
		for (vector<pair<int, int> >::iterator itr = seq.begin(); itr != seq.end(); ++itr) {
			Robot& r = robot[itr->first];
			Robot& otherR = robot[(itr->first + 1) % 2];
			//int b = itr->second;

			int moveLength = r.doNextStepUnlimited();
			otherR.doNextStepTimed(moveLength);
			
			tot += moveLength;
		}

		//int result = max(robot[0].totalStepsTaken(), robot[1].totalStepsTaken());

		cout << "Case #" << testCase << ": " << tot << "\n";
		
	}
	return 0;
}