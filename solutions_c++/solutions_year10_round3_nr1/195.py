// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void solve()
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		int N;
		cin >> N;
		vector<int> A, B;
		A.resize(N);
		B.resize(N);
		for (int i=0;i<N;i++)
		{
			cin >> A[i] >> B[i];
		}
		int cnt = 0;
		for (int i1=0;i1<N;i1++)
			for (int i2=i1+1;i2<N;i2++)
			{
				if (A[i1]<A[i2] && B[i1]>B[i2]) cnt++;
				else if (A[i1]>A[i2] && B[i1]<B[i2]) cnt++;
			}
		cout << "Case #" << (t+1) << ": " << cnt << endl;

	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

