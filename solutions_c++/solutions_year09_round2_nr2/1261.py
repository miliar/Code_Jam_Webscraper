#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector <short> vi;
typedef vector <vi> vvi;

int powers[] = {0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};

int getHash(int n)
{
	int result = 0;
	while (n) {
		result += powers[n % 10];
		n /= 10;
	}
	return result;
}

int main()
{
	ifstream fin("B-small-attempt0(2).in");
	ofstream fout("file.out");
	
	int T;
	fin >> T;
	for (int testCase = 1; testCase <= T; ++testCase) {
		int N;
		fin >> N;
		int Nhash = getHash(N);
		int cur = N + 1;
		while (getHash(cur) != Nhash)
			++cur;
		fout << "Case #" << testCase << ": " << cur << endl;
	}

	return 0;
}
