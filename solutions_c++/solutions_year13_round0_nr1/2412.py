#include<fstream>
#include<iostream>

using namespace std;

int main(int argc, char **argv) {
	ifstream f(argv[1]);
	int case_num;
	f >> case_num;
	case_num++;
	char b[4][4];
	for (int i = 1; i < case_num; ++i) {
		int won = 0;
		char who_won;
		int has_point = 0;
		for (int m = 0; m < 4; m++) {
			for (int n = 0; n < 4; n++) {
				f >> b[m][n];
			}
		}
		for (int m = 0; m < 4; ++m) {
			char start = b[m][0];
			if (start == '.') {
				has_point = 1;
				continue;
			}
			int cur_won = 1;
			for (int n = 0; n < 4; ++n) {
				if (b[m][n] == '.') {
					has_point = 1;
					cur_won = 0;
					break;
				}
				if (b[m][n] == 'T') {
					continue;
				}
				if (b[m][n] != start) {
					cur_won = 0;
					break;
				}
			}
			if (cur_won) {
				won = 1;
				who_won = start;
				break;
			}
		}
		if (won) {
			cout << "Case #" << i << ": " << who_won << " won" << endl;
			continue;
		}
		for (int n = 0; n < 4; ++n) {
			char start = b[0][n];
			if (start == '.') {
				has_point = 1;
				continue;
			}
			int cur_won = 1;
			for (int m = 0; m < 4; ++m) {
				if (b[m][n] == '.') {
					has_point = 1;
					cur_won = 0;
					break;
				}
				if (b[m][n] == 'T') {
					continue;
				}
				if (b[m][n] != start) {
					cur_won = 0;
					break;
				}
			}
			if (cur_won) {
				won = 1;
				who_won = start;
				break;
			}
		}
		if (won) {
			cout << "Case #" << i << ": " << who_won << " won" << endl;
			continue;
		}
		char start = b[0][0];
		if (start == '.') {
			has_point = 1;
		} else {
			int cur_won = 1;
			for (int m = 0; m < 4; ++m) {
				if (b[m][m] == '.') {
					has_point = 1;
					cur_won = 0;
					break;
				}
				if (b[m][m] == 'T') {
					continue;
				}
				if (b[m][m] != start) {
					cur_won = 0;
					break;
				}
			}
			if (cur_won) {
				won = 1;
				who_won = start;
			}
		}
		if (won) {
			cout << "Case #" << i << ": " << who_won << " won" << endl;
			continue;
		}
		start = b[0][3];
		if (start == '.') {
			has_point = 1;
		} else {
			int cur_won = 1;
			for (int m = 0; m < 4; ++m) {
				if (b[m][3-m] == '.') {
					has_point = 1;
					cur_won = 0;
					break;
				}
				if (b[m][3-m] == 'T') {
					continue;
				}
				if (b[m][3-m] != start) {
					cur_won = 0;
					break;
				}
			}
			if (cur_won) {
				won = 1;
				who_won = start;
			}
		}
		if (won) {
			cout << "Case #" << i << ": " << who_won << " won" << endl;
			continue;
		}
		if (has_point) {
			cout << "Case #" << i << ": Game has not completed" << endl;
			continue;
		}
		cout << "Case #" << i << ": Draw" << endl;
	}
}
