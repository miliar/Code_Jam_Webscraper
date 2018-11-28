// codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <map>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;

int main()
{
	int N;
	cin>>N;
	for(int n=0;n<N;n++)
	{
		int P,K,L;
		cin>>P>>K>>L;
		if(P*K<L)
		{
			cout << "Case " << n+1 << ": " << "Impossible" <<endl;
			continue;
		}
		vector<int> x;
		for(int i=0;i<L;i++)
		{
			int t;
			cin >> t;
			x.push_back(t);
		}
		sort(x.begin(),x.end(),greater<int>());
		int s=0;
		for(int i=0;i<L;i++)
		{
			s+=x[i]*(i/K+1);
		}
		cout << "Case " << n+1 << ": " << s <<endl;
	}
	return 0;
}

