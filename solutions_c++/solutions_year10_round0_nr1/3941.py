// 1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <math.h>
#include <iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int numCases = 0;
	int N = 0, K = 0;
	cin >> numCases;
	for (int i = 0; i < numCases; ++i) {
		cin >> N >> K;
		if ((K+1) % (int) pow(2.0, N)) {
			cout << "Case #" << i+1 << ": " << "OFF" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << "ON" << endl;
		}
	}
	return 0;
}

