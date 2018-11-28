// ProblemC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int cur=1;cur<=T;cur++)
	{
		int N,n;
		cin >> N;
		vector<long> C;
		C.clear();
		long Max,K;
		for (n=0; n<N; n++)
		{
			cin >> K;
			C.push_back(K);
		}
		sort(C.begin(),C.end());
		K=C[0];
		Max=0;
		for (n=1; n<N; n++)
		{
			Max+=C[n];
			K = K^C[n];
		}
		cout << "Case #" << cur << ": ";
		if (K==0) cout << Max << endl; else cout << "NO" << endl;
	}
	return 0;

}
