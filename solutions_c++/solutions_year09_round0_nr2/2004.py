#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <utility>

using namespace std;

pair<int, int> check_sink(vector<vector<int> >& v_list, int x, int y)
{
	int altitude = v_list[x][y];
	int next_x = x;
	int next_y = y;
	if (x - 1 >= 0 && v_list[x-1][y] < altitude) {
		altitude = v_list[x-1][y];
		next_x = x - 1;
		next_y = y;
	}
	if (y - 1 >= 0 && v_list[x][y-1] < altitude) {
		altitude = v_list[x][y-1];
		next_x = x;
		next_y = y - 1;
	}
	if (y + 1 < v_list[0].size() && v_list[x][y+1] < altitude) {
		altitude = v_list[x][y+1];
		next_x = x;
		next_y = y + 1;
	}
	if (x + 1 < v_list.size() && v_list[x+1][y] < altitude) {
		altitude = v_list[x+1][y];
		next_x = x + 1;
		next_y = y;
	}
	if (next_x == x && next_y == y) return make_pair(next_x, next_y);
	else return check_sink(v_list, next_x, next_y);
}

vector<vector<char> > check_map(vector<vector<int> >& v_list, int H, int W)
{
	map<pair<int, int>, char> sinks;
	pair<int, int> sink;
	int num_sinks = 0;
	vector<vector<char> > vv_char;

	for (int i = 0; i < H; i++) {
		vector<char> v_char;
		for (int j = 0; j < W; j++) {
			sink = check_sink(v_list, i, j);
			if (sinks.find(sink) == sinks.end()) sinks[sink] = 'a' + num_sinks++;
			v_char.push_back(sinks[sink]);
		}
		vv_char.push_back(v_char);
	}

	return vv_char;
}

int main(int argc, char *argv[])
{
	fstream fs("B-large.in", ios_base::in);
	string line;
	stringstream ss;
	vector<int> v;
	vector<vector<int> > v_list;

	int T, H, W;
	getline(fs, line);
	ss.str(line);
	ss >> T;
	ss.clear();
	int cnt = 0;
	for (int i = 0; i < T; i++) {
		getline(fs, line);
		ss.str("");  ss.clear();
		ss.str(line);
		ss >> H >> W;
		for (int j = 0; j < H; j++) {
			getline(fs, line);
			ss.str("");  ss.clear();
			int data;
			for (ss.str(line), v.clear(); ss >> data; v.push_back(data));
			v_list.push_back(v);
		}
		cout << "Case #" << ++cnt << ":" << endl;
		vector<vector<char> > result = check_map(v_list, H, W);
		for (vector<vector<char> >::iterator p = result.begin(); p != result.end(); ++p) {
			for (vector<char>::iterator q = p->begin(); q != p->end(); ++q) {
				if (q != p->begin()) cout << " ";
				cout << *q;
			}
			cout << endl;
		}
		v_list.clear();
	}

	return 0;
}
