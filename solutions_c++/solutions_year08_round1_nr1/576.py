// codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <map>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <functional>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
//	freopen("codejam.in","r",stdin);
	int N;
	cin >>  N;
	for(int n=0;n<N;n++)
	{
		vector<int> x,y;
		int M,xi,yi;
		cin >> M;
		for(int m=0;m<M;m++)
		{
			cin >> xi;
			x.push_back(xi);
		}
		for(int m=0;m<M;m++)
		{
			cin >> yi;
			y.push_back(yi);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end(),greater<int>());
		long long s=0;
		for(int m=0;m<M;m++)
		{
			long long ss=x[m];
			ss*=y[m];
			s+=ss;
		}
		cout << "Case #" << n+1 <<": " << s << endl;
	}

	return 0;
}

