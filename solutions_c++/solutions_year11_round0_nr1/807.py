#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>

using namespace std;

struct task {
	int id;
	int where;
};

bool robot_logic(int & pos,int taskid,task next) {
	if (next.where == pos) {
		return taskid == next.id;
	}
	else
	{
		pos+= abs(next.where-pos)/(next.where-pos);
	}
	return false;
}

int solve(const vector<task> & orange,const vector<task> & blue) {
	int orange_pos=1,blue_pos=1;
	int orange_task=0,blue_task = 0;

	int taskid = 0;

// 	cout << "orange_tasks: ";
// 	for (int i=0;i < orange.size();++i) cout << orange[i].id << " " << orange[i].where << " --- ";
// 	cout << "blue_tasks: ";
// 	for (int i=0;i < blue.size();++i) cout << blue[i].id << " " << blue[i].where << " --- ";

	for (int time=1;time < 10000000;++time) {
		int orange_res = 0,blue_res = 0;

		if (orange_task < orange.size())
			orange_res = robot_logic(orange_pos,taskid,orange[orange_task]);
		if (blue_task < blue.size())
			blue_res = robot_logic(blue_pos,taskid,blue[blue_task]);

		if (blue_res) blue_task++;
		if (orange_res) orange_task++;

		assert(! (blue_res && orange_res));
		if (blue_res || orange_res) taskid++;

		if (orange_task >= orange.size() && blue_task >= blue.size())
			return time;
	}
	return -1;
}

int main(int argc, char **argv) {
	int T;

	cin >> T;

	for(int i=0;i < T;++i) {
		int N;
		cin >> N;

		vector<task> orange,blue;
		for (int j=0;j < N;++j) {
			char w;
			int where;
			cin >> w >> where;
			task t;
			t.id = j;
			t.where = where;
			if (w == 'O')
				orange.push_back(t);
			else
				blue.push_back(t);
		}
		cout << "Case #" << (i+1) << ": " << solve(orange,blue) << endl;
	}
	
    return 0;
}
