// win32console_test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "math.h"

using std::cout;
using std::cin;
using std::endl;

int _tmain(int argc, _TCHAR* argv[])
{
	int N = 4;
	int K = 47;
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cin >> N;
		cin >> K;
		long int twon = (long int) pow((double)2, (double)N);
		cout << "Case #" << t << ": ";
		if((K % twon) == (twon - 1) )
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}
