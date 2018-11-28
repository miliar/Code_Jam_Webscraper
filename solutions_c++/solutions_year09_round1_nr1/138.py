/*
 * happy.cpp
 *
 *  Created on: Sep 11, 2009
 *      Author: gatanov
 */

#include <iostream>
#include <vector>
#include <string>
#include <sstream>


using namespace std;

const int Max = 20000000;
bool happy[11][Max];

int sum_of_squares(int num,int base) {
	int sum = 0;
	while (num > 0) {
		int rem = num % base;
		num /= base;
		sum += rem * rem;
	}
	return sum;
}


int main(int argc, char **argv) {
	for (int base = 2;base <= 10;base++)
		happy[base][1] = true;
	for (int base = 2;base <= 10;base++) {
		int sum = 1; int so = 0;
		do {
			so = sum; sum = 0;
			for (int j = 0;j < Max;j++)
				if (happy[base][sum_of_squares(j,base)]) {
					happy[base][j] = true;
					sum ++;
				}
		} while (sum > so);
	}

	int T;
	char str[1000];
	cin.getline(str,1000);
	istringstream iss(str);
	iss >> T;
	for (int t = 1;t <= T;t++) {
		cin.getline(str,1000);
		istringstream iss(str);
		vector<int> bases;
		int d;
		while (iss >> d)
			bases.push_back(d);
		for (int i = 2;i < Max;i++)
		{
			bool flag = true;
			for (int b = 0;b < bases.size();b++)
				if (!happy[bases[b]][i]) {
					flag = false;
					break;
				}
			if (flag) {
				cout << "Case #" << t << ": " << i << endl;
				break;
			}
		}
	}

}
