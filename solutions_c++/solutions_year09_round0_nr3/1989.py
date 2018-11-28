#include <iostream>
#include <fstream>
#include <cstdlib> // for exit function
#include <algorithm>
#include <math.h>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <string>

using namespace std;

const int SIZE = 501;
const char* str = "welcome to code jam";
const int strSize = 19;
int n;
vector<pair<char*,int>> strings;

int vec[SIZE][strSize];

char* formatStr(int count) {
	const int TEMPLEN = 20;
	char* c = new char[TEMPLEN];
	memset(c, 0, sizeof(char) * TEMPLEN);
	_itoa_s(count, c, sizeof(char) * TEMPLEN, 10);
	int len = 0;
	if (count < 10)
		len = 3;
	else if (count < 100)
		len = 2;
	else if (count < 1000)
		len = 1;
	//cout << "sdfsdf: " << c << endl;
	for (int i = TEMPLEN - 1; i >= len; i--)
		c[i] = c[i - len];
	for (int i = 0; i < len; i++)
		c[i] = '0';
	return c;
}

int getCount(char* c, int len, int strPos) {
	if (len <= 0 || strPos >= strSize) {
		if (strPos >= strSize) {
			return 1;
		}
		return 0;
	}
	int count = 0;
	if (c[0] == str[strPos]) {
		if (vec[len - 1][strPos + 1] == -1)
			count += getCount(c + 1, len - 1, strPos + 1);
		else count += vec[len - 1][strPos + 1];
	}
	if (vec[len - 1][strPos] == -1)
			count += getCount(c + 1, len - 1, strPos);
		else count += vec[len - 1][strPos];
	if (count > 10000)
		count = count % 10000;
	vec[len][strPos] = count;
	return count;
}

void solve(ofstream& outdata) {
	for (int i = 0; i < n; i++) {
		outdata << "Case #" << (i + 1) << ": ";
		cout << "Progress: " << i << " out of " << n << endl;
		memset(vec, -1, sizeof(vec));
		pair<char*,int> p = strings[i];
		int count = getCount(p.first, p.second, 0);
		if (count > 10000)
			count = count % 10;
		outdata << formatStr(count) << endl;
		//cout << "Count=" << formatStr(count) << " for string:" << p.first << endl;
	}
}

int main() {
	ifstream indata; 
	ofstream outdata;
	indata.open("A-small.in"); // opens the file
	outdata.open("A-small.out");
	if(!indata) { // file couldn't be opened
		cerr << "Error: file could not be opened" << endl;
		exit(1);
	}
	indata >> n;
	strings.reserve(n);

	char* c = new char[SIZE];
	memset(c, 0, sizeof(char) * SIZE);
	indata.getline(c, SIZE); // read first EOL after n

	for (int i = 0; i < n; i++) {
		char* c = new char[SIZE];
		memset(c, 0, sizeof(char) * SIZE);
		indata.getline(c, SIZE);
		int size = indata.gcount();
		//cout << c << endl;
		pair<char*,int> p = make_pair<char*,int>(c, size);
		strings.push_back(p);
	}
	solve(outdata);	

	outdata.close();
	return 0;
}