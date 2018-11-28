#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

#define MAX_CASES 100

int Get2Y(int y) {
	if (y == 0)
		return 1;
	int res = 1;
	for (int i = 0; i < y; i++) {
		res = res * 2;
	}
	return res;
}

class Binary {
public:

	bool number[20];

	Binary() {
		for (int i = 0; i < 20; i++) {
			number[i] = 0;
		}
	}

	bool GetNumber(int i) {
		return number[i];
	}

	void SetNumber(int i, bool n) {
		number[i] = n;
	}

	void Set(int integer) {
		int high = 0, reminder;
		for (int i = 0; i < 20; i++) {
			number[i] = 0;
		}
		if (integer!=1){
			while (integer >= Get2Y(high)) {
				high++;
			}
			high--;
			if (high < 0)
				high = 0;
			if (high > 0) {
				reminder = integer;
				for (int i = high; i >= 0; i--) {
					if (reminder >= Get2Y(i)) {
						number[i] = 1;
						reminder = reminder - Get2Y(i);
					}
				}
			}
		}else{
		number[0] = 1;}
	}

	int GetInteger() {
		int res = 0;
		for (int i = 0; i < 20; i++) {
			res = res + number[i] * Get2Y(i);
		}
		return res;
	}

	friend Binary operator+(Binary a, Binary b) {
		Binary res;
		for (int i = 0; i < 20; i++) {
			if (a.GetNumber(i) == b.GetNumber(i))
				res.number[i] = 0;
			if (a.GetNumber(i) != b.GetNumber(i))
				res.number[i] = 1;
		}
		return res;
	}

	Binary & operator=(Binary a) {
		for (int i = 0; i < 20; i++) {
			number[i] = a.number[i];
		}
		return *this;
	}
};

class BitCombination {
public:
	bool member[1000];
	int k;

	BitCombination() {
		for (int i = 0; i < 20; i++) {
			member[i] = 1;
		}
		k = 0;
	}

	void Set(int integer) {
		int high = 0, reminder;
		for (int i = 0; i < k; i++) {
			member[i] = 0;
		}
		if (integer!=1){
			while (integer >= Get2Y(high)) {
				high++;
			}
			high--;
			if (high < 0)
				high = 0;

			if (high > 0) {
				reminder = integer;
				for (int i = high; i >= 0; i--) {

					if (reminder >= Get2Y(i)) {
						member[i] = 1;
						reminder = reminder - Get2Y(i);
					}
				}
			}
		}else{
		member[0] = 1;}
	}

	int GetInteger() {
		int res = 0;
		for (int i = 0; i < k; i++) {
			res = res + member[i] * Get2Y(i);
		}
		return res;
	}

};
class Case {
	int N;
	Binary binC[1000];

public:
	Case() {
		N = 0;
	}

	void AddCandy(int inC) {
		binC[N].Set(inC);
		N++;
	}

	int GetRes() {
		int result = -1, res[2], maxComb;
		Binary bag[2];
		BitCombination temp;

		temp.k = N;
		maxComb = temp.GetInteger();
		for (int i = 1; i < maxComb; i++) {
			temp.Set(i);
			bag[0].Set(0);
			bag[1].Set(0);

			for (int j = 0; j < N; j++) {
				if (temp.member[j]) {
					bag[0] = bag[0] + binC[j];
				} else {
					bag[1] = bag[1] + binC[j];
				}
			}
			if (bag[0].GetInteger() == bag[1].GetInteger()) {
				res[0] = res[1] = 0;
				for (int j = 0; j < N; j++) {
					if (temp.member[j]) {
						res[0] = res[0] + binC[j].GetInteger();
					} else {
						res[1] = res[1] + binC[j].GetInteger();
					}
				}
				if (res[0] > result)
					result = res[0];
				if (res[1] > result)
					result = res[1];
			}
		}
		return result;
	}
};

int main() {
	ifstream in("inputFile");
	ofstream out("outputFile");

	int number, T, candy;

	Case cases[MAX_CASES];

	in >> T;

	for (int i = 0; i < T; i++) {
		in >> number;
		for (int j = 0; j < number; j++) {
			in >> candy;
			cases[i].AddCandy(candy);
		}
	}
	in.close();

	for (int i = 0; i < T; i++) {
		number = cases[i].GetRes();
		if (number>0){
			out << "Case #" << i + 1 << ": " << number << endl;
		}else{
			out << "Case #" << i + 1 << ": NO" << endl;
		}
	}

	out.close();

	return 0;
}
