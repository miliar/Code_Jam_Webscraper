/*
 * source.cpp
 *
 *  Created on: May 7, 2011
 *      Author: mamayu
 */

#include <fstream>
#include <cmath>
using namespace std;

int main() {
	int timer, number, order;
	char bot;
	ifstream cinf;
	ofstream coutf;
	cinf.open ("A-large.in");
	coutf.open ("A-large.out");
	cinf >> timer;
	for (int i = 0; i < timer; ++i) {
		cinf >> number;
		int temp = 0;
		int tempBlue = 0;
		int tempOrange = 0;
		int current = 0;
		int currentBlue = 1;
		int currentOrange = 1;
		for (int j = 0; j < number; ++j) {
			cinf >> bot >> order;
			if (bot == 'B') {
				temp = abs(order - currentBlue) - tempOrange + 1;
				if (temp < 1) temp = 1;
				tempOrange = 0;
				currentBlue = order;
				tempBlue += temp;
				current += temp;
			} else if (bot == 'O') {
				temp = abs(order - currentOrange) - tempBlue + 1;
				if (temp < 1) temp = 1;
				tempBlue = 0;
				currentOrange = order;
				tempOrange += temp;
				current += temp;
			}
		}
		coutf << "Case #" << i + 1 << ": " << current << endl;
	}
	cinf.close();
	coutf.close();
}
