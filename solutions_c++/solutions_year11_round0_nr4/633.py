// ProblemD.cpp : Defines the entry point for the console application.
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
		long K,Hits,R;
		cin >> N;
		vector<long> B,C,D;
		C.clear();
		B.clear();
		for (n=0; n<N; n++)
		{
			cin >> K;
			C.push_back(K);
			B.push_back(K);
			D.push_back(0);
		}
		Hits = 0;
		sort(B.begin(), B.end());
		for (n=0; n<N; n++)
			if (C[n]==B[n]) D[n] = 1;
		for (int i=0; i<N; i++)
		{
			if (D[i]==0) 
			{
				for (int j=i, R=0; D[j] == 0; j=C[j]-1)
				{
					R++;
					D[j] = 1;
				}
				Hits +=R;
			}
		}
		cout << "Case #" << cur << ": " << Hits << ".000000" << endl;
	}
	return 0;

}
