// SnapperChain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>

using namespace std;

void print(const int caseNum, const char * result)
{
	cout << "Case #" << caseNum << ": " << result << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int numCases = 0;
	int N = 0, K = 0;
	cin >> numCases;
	for (int i = 0; i < numCases; ++i) {
		cin >> N >> K;
		if ((K+1) % (int) pow(2.0, N)) {
			print(i+1, "OFF");
		} else {
			print(i+1, "ON");
		}
	}
	return 0;
}

