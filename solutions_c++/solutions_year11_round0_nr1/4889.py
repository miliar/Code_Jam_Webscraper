#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

int main(int argc, char** argv) {
	if (argc != 2) {
		printf("Bad arg count\n");
		return -1;
	}

	char buf[1024];
	int c;
	int j;
	int color;
	int but;
	deque<int> blue;
	deque<int> orange;
	deque<char> order;
	blue.clear();
	orange.clear();
	order.clear();

	ifstream* inFileStr = new ifstream(argv[1]);
	ofstream* outFileStr = new ofstream("results.txt");

	inFileStr->getline(buf, 100);
	int T(atoi(buf));
	int N(0);
	int bPos(1);
	int oPos(1);
	int time(0);
	int steps;

	for (int i = 0; i < T; i++) {
		inFileStr->get(buf, 1024, ' ');
		N = atoi(buf);
		for (j = 0; j < N-1; j++) {
			do {
				color = inFileStr->get();
			} while (color == (int)' ');
			do {
				c = inFileStr->get();
			} while (c == (int)' ');
			inFileStr->unget();
			inFileStr->get(buf, 1024, ' ');
			but = atoi(buf);
			order.push_back(color);
			if (color == 'B')
				blue.push_back(but);
			else
				orange.push_back(but);
		}
		do {
			color = inFileStr->get();
		} while (color == (int)' ');
		do {
			c = inFileStr->get();
		} while (c == (int)' ');
		inFileStr->unget();
		inFileStr->get(buf, 1024);
		but = atoi(buf);
		order.push_back(color);
		if (color == 'B')
			blue.push_back(but);
		else
			orange.push_back(but);

		bPos = 1;
		oPos = 1;
		time = 0;
		while (!order.empty()) {
			if (order[0] == 'B') {
				steps = abs(bPos - blue[0]) + 1;
				time += steps;
				bPos = blue[0];
				blue.pop_front();
				if (!orange.empty()) {
					if (abs(oPos - orange[0]) <= steps)
						oPos = orange[0];
					else if (oPos > orange[0])
						oPos -= steps;
					else
						oPos += steps;
				}
			}
			else {
				steps = abs(oPos - orange[0]) + 1;
				time += steps;
				oPos = orange[0];
				orange.pop_front();
				if (!blue.empty()) {
					if (abs(bPos - blue[0]) <= steps)
						bPos = blue[0];
					else if (bPos > blue[0])
						bPos -= steps;
					else
						bPos += steps;
				}
			}
			order.pop_front();
		}
		*outFileStr << "Case #" << i + 1 << ": " << time << endl;
	}

	delete inFileStr;
	delete outFileStr;

	return 0;
}
