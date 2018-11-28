#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

struct Robot {
	// order, button
	deque<pair<int, int> > commands;
	int pos;
	bool done;
};

class BotTrust {
private:
	int order;
	Robot orange, blue;

public:
	BotTrust() {
		order = 0;
		orange.pos = 1;
		orange.done = false;
		blue.pos = 1;
		blue.done = false;
	}

	void set_robots(const vector<pair<char, int> >& v) {
		order = 0;
		orange.pos = 1;
		orange.done = false;
		blue.pos = 1;
		blue.done = false;
		orange.commands.clear();
		blue.commands.clear();

		int cnt = 0;
		for (vector<pair<char, int> >::const_iterator p = v.begin(); p != v.end(); ++p) {
			if (p->first == 'O') {
				orange.commands.push_back(make_pair(cnt++, p->second));
			} else {
				blue.commands.push_back(make_pair(cnt++, p->second));
			}
		}
	}

	int solve() {
		for (int i = 1;; i++) {
			if (!orange.commands.empty() && orange.commands.front().second == orange.pos) orange.done = true;
			if (!blue.commands.empty() && blue.commands.front().second == blue.pos) blue.done = true;

			if (!orange.commands.empty()) {
			if (orange.commands.front().second > orange.pos)
				orange.pos++;
			else if (orange.commands.front().second < orange.pos)
				orange.pos--;
			}

			if (!blue.commands.empty()) {
			if (blue.commands.front().second > blue.pos)
				blue.pos++;
			else if (blue.commands.front().second < blue.pos)
				blue.pos--;
			}

			if (!orange.commands.empty() && order == orange.commands.front().first) {
				if (orange.done) {
					order++;
					orange.commands.pop_front();
					orange.done = false;
					if (orange.commands.empty() && blue.commands.empty()) return i;
				}
			} else if (!blue.commands.empty()) {
				if (blue.done) {
					order++;
					blue.commands.pop_front();
					blue.done = false;
					if (orange.commands.empty() && blue.commands.empty()) return i;
				}
			} else return i;
		}

		return 0;
	}
};


void read_data(const string filename, vector<vector<pair<char, int> > >& v_list)
{
	fstream fs(filename.c_str(), ios_base::in);
	string line;
	vector<pair<char, int> > v;
	stringstream ss;

	getline(fs, line);
	while (getline(fs, line)) {
		ss.str("");  ss.clear();
		char r;
		int b;
		for (ss.str(line), v.clear(), ss >> b; ss >> r >> b; v.push_back(make_pair(r, b)));
		v_list.push_back(v);
	}
}

int main()
{
	vector<vector<pair<char, int> > > v;
	//read_data("test.in", v);
	read_data("A-large.in", v);

	BotTrust test;

	int cnt = 1;
	for (vector<vector<pair<char, int> > >::iterator p = v.begin(); p != v.end(); ++p) {
		test.set_robots(*p);
		cout << "Case #" << cnt++ << ": " << test.solve() << endl;
	}

	return 0;
}
