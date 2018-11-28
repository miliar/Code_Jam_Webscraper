#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

bool ok(int num, int base)
{
	//cout << num << ' ' << base << " : " << endl;
	int iter = 0;
	while (num > 1) {
		if (iter++ >= 10) return false;

		//cout << num << endl;
		int a = 0;
		while (num) {
			int r = num%base;
			num /= base;
			a += r*r;
		}
		num = a;
	}
	return num == 1;
}

int minNum(int base)
{
	for (int i=2; i<=1000; ++i) {
		if (ok(i, base)) cout << i << ' ';
	}
	cout << endl;
	return 0;
}

int seq[] = {7,6,8,9,10,3,5};

int calc(vector<int> &bases)
{
	if (bases.size() == 0) return 2;

	int i, j;
	vector<bool> exist(11, false);
	for (i=0; i<bases.size(); ++i) exist[bases[i]] = true;

	bases.clear();
	for (i=0; i<7; ++i) {
		if (exist[seq[i]]) bases.push_back(seq[i]);
	}

	for (i=2; 1; ++i) {
		for (j=0; j<bases.size(); ++j) {
			if (!ok(i, bases[j])) break;
		}

		if (j == bases.size()) return i;
	}

	return -1;
}


int main(void)
{
	int i, j;
	/*
	for (i=2; i<=10; ++i) {
		cout << "base " << i << ": " << endl;
		minNum(i);
	}

	for (i=2; 1; ++i) {
		if (!ok(i, 7) || !ok(i, 6) || !ok(i, 8)) continue;

		cout << i << endl;

		for (j=3; j<=10; ++j) if (j!=4 && j!=7 && j!=6 && j!=8) {
			if (!ok(i, j)) break;
		}

		if (j > 10) break;
	}

	cout << "found: " << i << endl;
	*/

	int T;
	string line;
	cin >> T;
	getline(cin, line);
	for (int ca=1; ca<=T; ++ca) {
		getline(cin, line);
		stringstream S(line);
		vector<int> bases;
		int a;
		while (S >> a) {
			if (a!=2 && a!=4) bases.push_back(a);
		}
		cout << "Case #" << ca << ": " << calc(bases) << endl;
	}
	return 0;
}
