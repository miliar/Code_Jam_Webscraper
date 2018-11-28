// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void solve()
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		int N,K;
		cin >> N >> K;
		cout << "Case #" << (t+1) << ": ";
		bool bOn = true;
		for (int i=0;i<N;i++)
			if ((K&(1<<i))==0)
			{
				bOn = false;
				break;
			}
		if (bOn) cout << "ON"; else cout << "OFF";
		cout << endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

