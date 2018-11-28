#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

int wcount;
string W = "welcome to code jam";

void search_welcome(string& line, int pos, int num)
{
	if (num == 19) {
		wcount = (wcount + 1) % 10000;
//		wcount++;
		return;
	}
	if (pos >= line.size()) return;
	for (int i = pos; i < line.size(); i++) {
		if (line[i] == W[num]) {
			search_welcome(line, i + 1, num + 1);
		}
	}
}

void count_welcome(string line)
{
	wcount = 0;
	search_welcome(line, 0, 0);
}

int main(int argc, char *argv[])
{
	fstream fs("C-small-attempt1.in", ios_base::in);
	string line;
	stringstream ss;
	vector<string> lines;

	getline(fs, line);
	ss.str(line);
	int N;
	ss >> N;
	for (int i = 0; i < N; i++) {
		getline(fs, line);
		lines.push_back(line);
	}
	int cnt = 0;
	for (vector<string>::iterator p = lines.begin(); p != lines.end(); ++p) {
		count_welcome(*p);
		cout << "Case #" << ++cnt << ": " << setw(4) << setfill('0') << wcount % 10000 << endl;
	}

	return 0;
}
