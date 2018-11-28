#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char *input_file = "A-large-0.in";
const char *output_file = "A-large-0.out";

struct Action {
    int time, pos;

    Action() {}
    Action(int t, int p) : time(t), pos(p) {}
};

void solveCase(int case_num, istream &in, ostream &out) {
    int n, lastO = 0, lastB = 0;
    vector<Action> v;

    v.push_back(Action(0, 1));
    in >> n;
    for (int i = 0; i < n; ++i) {
	char bot;
	int time, pos, walk_time;

	in >> bot >> pos;
	switch (bot) {
	case 'B':
	    walk_time = v[lastB].time + abs(v[lastB].pos - pos);
	    time = max(walk_time, v[lastO].time) + 1;
	    lastB = v.size();
	    v.push_back(Action(time, pos));
	    break;
	default: // 'O'
	    walk_time = v[lastO].time + abs(v[lastO].pos - pos);
	    time = max(walk_time, v[lastB].time) + 1;
	    lastO = v.size();
	    v.push_back(Action(time, pos));
	}
    }
    out << "Case #" << case_num << ": " << v.back().time << endl;
}

int main() {
    ifstream in(input_file);
    ofstream out(output_file);

    int t;
    in >> t;
    for (int i = 1; i <= t; ++i)
	solveCase(i, in, out);

    in.close();
    out.close();

    return EXIT_SUCCESS;
}
