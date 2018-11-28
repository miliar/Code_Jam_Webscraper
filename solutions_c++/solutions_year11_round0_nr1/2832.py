#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>

using namespace std;
int solve();

int main()
{
	ifstream ifs;
	ofstream ofs("output.txt");
	
	int turns;
	cin >> turns;
	for (int i = 1; i <= turns; ++i) {
		ofs << "Case #" << i << ": " << solve() << endl;
	}
	
	system("pause");
	return 0;
}

int solve()
{
	int seq;
	cin >> seq;
	
	int orange[100];
	int blue[100];
	char order[100];
	int orange_move_size = 0;
	int blue_move_size = 0;
	int order_size = 0;
	char c;
	int num;
	for (; order_size != seq; ++order_size) {
		cin >> order[order_size] >> num;
		if (order[order_size] == 'O') {
			orange[orange_move_size] = num;
			++orange_move_size;
		}
		else {
			blue[blue_move_size] = num;
			++blue_move_size;
		}
	}
	
	int time = 0;
	int orange_position = 1;
	int blue_position = 1;
	int p = 0;
	int q = 0;
	int i = 0;
	for (; i != order_size; ++i) {
		if (p == orange_move_size || q == blue_move_size) {
			break;
		}
		if (order[i] == 'O') {
			int rest = abs(orange[p] - orange_position) + 1;
			time += rest;
			orange_position = orange[p];
			++p;
			if (abs(blue[q] - blue_position) <= rest) {
				blue_position = blue[q];
			}
			else {
				if (blue_position < blue[q]) {
					blue_position += rest;
				}
				else {
					blue_position -= rest;
				}
			}
		}
		else {
			int rest = abs(blue[q] - blue_position) + 1;
			time += rest;
			blue_position = blue[q];
			++q;
			if (abs(orange[p] - orange_position) <= rest) {
				orange_position = orange[p];
			}
			else {
				if (orange_position < orange[p]) {
					orange_position += rest;
				}
				else {
					orange_position -= rest;
				}
			}
		}
	}
	
	while (p != orange_move_size) {
		time += abs(orange[p] - orange_position) + 1;
		orange_position = orange[p];
		++p;
	}
	while (q != blue_move_size) {
		time += abs(blue[q] - blue_position) + 1;
		blue_position = blue[q];
		++q;
	}
	
	return time;
}
