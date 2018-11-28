#include<iostream>
#include<vector>

using namespace std;

int makeStep(const vector<vector<long long> > & people, int startPos, int freePlace, bool firstTime, int * queuePos) {
	int maxLevel = people.size() - 1;
	int result = 0;
	int level = 0;
	int startBlock = startPos;
	//cout << "making step: start pos " << startPos << " free place " << freePlace << " queue pos " << *queuePos << endl;
	if ((*queuePos % people[0].size() == startBlock) && (!firstTime)) {
		return 0;
	}
	if (people[0][*queuePos] > freePlace) {
		return 0;
	}
	while ((*queuePos % 2 == 0) && (level < maxLevel) &&
		(*queuePos / 2 < people[level + 1].size()) &&
		(result + people[level + 1][*queuePos / 2] < freePlace) && 
		((startBlock / 2 != (*queuePos / 2) % people[level].size()) || firstTime)) {
			++level;
			*queuePos /= 2;
			startBlock /= 2;
	}
	result += people[level][*queuePos];
	++(*queuePos);
	while(level > 0) {
		--level;
		(*queuePos) *= 2;
	}
	if (*queuePos == people[0].size()) {
		*queuePos = 0;
	}
	//cout << "result is " << result << " new queue pos " << *queuePos << endl;
	return result;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int r, k, n;
		cin >> r;
		cin >> k;
		cin >> n;
		vector<vector<long long> > people;
		long long sum = 0;
		for(int l = n; l > 0; l /= 2) {
			vector<long long> temp(l);
			people.push_back(temp);
		}
		for (int j = 0; j < n; ++j) {
			cin >> people[0][j];
		}
		int level = 1;
		for(int l = n / 2; l > 0; l /= 2) {
			for (int m = 0; m < l; ++m) {
				people[level][m] = people[level - 1][m * 2] + people[level - 1][m * 2 + 1];
			}
			++level;
		}
		/*for(int l = 0; l < people.size(); ++l) {
			for (int m = 0; m < people[l].size(); ++m) {
				cout << people[l][m] << " ";
			}
			cout << endl;
		}*/
		int queuePos = 0;
		for (int time = 0; time < r; ++time) {
			//cout << time << ":\n";
			int peopleOn = 0;
			int startPos = queuePos;
			int stepResult = makeStep(people, startPos, k, true, &queuePos);
			while(stepResult > 0) {
				peopleOn += stepResult;
				stepResult = makeStep(people, startPos, k - peopleOn, false, &queuePos);
			}
			sum += peopleOn;
		}
		cout << "Case #" << i + 1 << ": " << sum << endl;
	}
	return 0;
}