// testcpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"


#include "stdio.h"
#include "stdlib.h"
#include "signal.h"
#include "process.h"
#include "malloc.h"

#include "fstream"
#include "list"
#include "vector"
#include "algorithm"
#include "time.h"

#include "queue"
#include "stack"

using namespace std;

char c[40];

int main()
{
	int K, N;
	int T;
	cin >> T;

	int t = 1;
	for (t = 1; t <= T; ++t)
	{
		cin >> N >> K;
		if (N > 31)
		{
			cout << "error" << endl;
			break;
		}
		memset(c, 0, sizeof (c));

		int i = 0;
		while (i < N && K)
		{
			c[i++] = K%2;
			K /=2;
		}
		for (i = 0; i < N; ++i)
		{
			if (c[i] == 0) break;
		}
		cout << "Case #" << t << ": ";
		if (i == N)
		{
			cout << "ON" ;
		}
		else
		{
			cout <<"OFF";
		}
		if (t < T) cout << endl;
	}

	return 0;
}


