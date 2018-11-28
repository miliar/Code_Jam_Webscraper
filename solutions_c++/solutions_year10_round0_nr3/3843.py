// gjamc.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T,N;
    int k, R;
	cin >> T;
	vector<int> data;
	for(int t = 0; t < T; ++t)
	{
		cin >> R >> k >> N;
		data.resize(N);
		for (int i=0; i<N; ++i)
		{
			cin >> data[i];
		}
		int idx = 0;
		int res = 0;
		for(int r=0; r<R; ++r)
		{
			int sum = 0;
			int oldidx = idx; 
			while(sum <= k && oldidx+N>=idx)
			{
				sum += data[idx%N];
				res += data[idx%N]; 
				++idx;
			}
			--idx;
			res -= data[idx%N];
		}
		cout << "Case #" << t+1 <<": " << res;
		if(t<T-1) {cout << endl;}
		
	}

	return 0;
}

