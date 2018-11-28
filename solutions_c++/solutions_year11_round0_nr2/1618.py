#include <fstream>
#include <map>
#include <string>
using namespace std;

map<char, int> base_map;

void init() {
	base_map['Q'] = 0;
	base_map['W'] = 1;
	base_map['E'] = 2;
	base_map['R'] = 3;
	base_map['A'] = 4;
	base_map['S'] = 5;
	base_map['D'] = 6;
	base_map['F'] = 7;
}

int main() {
	init();
	char com[8][8];
    bool opp[8][8];
	int exist[8];
	int T, C, D, N;
	string input;
	char output[101];
	int num;
	ifstream in("H:\\temp\\B-large.in");
	ofstream out("H:\\temp\\B-large.out");
	in >> T;
	for (int t = 1; t <= T; t++) {
		memset(com, 0, sizeof(com));
		memset(opp, 0, sizeof(opp));
		memset(exist, 0, sizeof(exist));
		num = 0;
		in >> C;
		for (int c = 0; c < C; c++) {
			in>> input;
			com[base_map[input[0]]][base_map[input[1]]] = input[2];
			com[base_map[input[1]]][base_map[input[0]]] = input[2];
		}
		in >> D;
		for (int d = 0; d < D; d++) {
			in>> input;
			opp[base_map[input[0]]][base_map[input[1]]] = true;
			opp[base_map[input[1]]][base_map[input[0]]] = true;
		}
		in >> N;
		in >> input;
		bool end = false;
		for (int n = 0; n < N; n++) {
			end = false;
			if (num) {
				if (base_map.find(output[num - 1]) != base_map.end() &&
					com[base_map[output[num - 1]]][base_map[input[n]]]) {
					exist[base_map[output[num - 1]]]--;
					output[num - 1] = com[base_map[output[num - 1]]][base_map[input[n]]];
					end = true;
				}
				for (int i = 0; !end && i < 8; i++)
					if (exist[i] && opp[i][base_map[input[n]]]) {
						num = 0;
						memset(exist, 0, sizeof(exist));
						end = true;
						break;
					}
			}
			if (!end) {
				output[num++] = input[n];
				exist[base_map[input[n]]]++;
			}
		}
		out << "Case #" << t << ": [";
		if (num)
			out << output[0];
		for (int i = 1; i < num; i++)
			out << ", " << output[i];
		out << "]" <<endl;
	}
	return 0;
}