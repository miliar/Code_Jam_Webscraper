#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<long long> readVector(int n) {
	int value;
	vector<long long> result;
	for (size_t i = 0; i < n; i++)	{
		cin >> value;
		result.push_back(value);
	}
	return result;
}

bool canPush(pair<int,int> push, int position, int robot) {
	return push.first == robot && push.second == position;
}

int sgn(int a) {
	if (a < 0)
		return -1;
	if (a == 0)
		return 0;
	return 1;
}

int push;
vector<pair<int,int>> pushes;
vector<int> places[2];

bool moveRobot(int &pos, int &target, int robot) {
	if(canPush(pushes[push], pos, robot)) {
		target++;
		return true;
	}
	
	int nextPos = pos;
	if(target < places[robot].size())
		nextPos = places[robot][target];

	pos += sgn(nextPos - pos);

	return false;
}

void spike() {
	int n;
	cin >> n;

	push = 0;
	pushes.clear();
	places[0].clear(); places[1].clear();

	for (size_t i = 0; i < n; i++) {
		int button;
		char robot;
		cin >> robot >> button;
		pushes.push_back(make_pair(robot=='O', button));
		places[robot=='O'].push_back(button);
	}

	int pos[2] = {1, 1};
	int targets[2] = {0, 0};
	int time = 0;
	while(push < pushes.size()) {
		
		bool a = moveRobot(pos[0], targets[0], 0);
		bool b = moveRobot(pos[1], targets[1], 1);
		if(a || b) {
			push++;
		}
		time++;
	}
	cout << time << endl;
}

int main() {
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}