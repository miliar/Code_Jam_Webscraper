#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>

using namespace std;

//char ouci[50] = {"results_A_small.txt"};

/*void Snapper_Chain(int n, int k, int c)	{
	vector<int> on(n), rec(n);
	for(int i = 0; i < n; i++)	{
		on[i] = 0;
		rec[i] = 0;
	}
	rec[0] = 1;

	for(int i = 0; i < k; i++)	{
		if(on[0] == 0)	
			on[0] = 1;
		else
			on[0] = 0;

		for(int j = 1; j < n; j++)	{
			if(rec[j] == 1)	{
				if(on[j] == 0)	
					on[j] = 1;
				else
					on[j] = 0;
			}
			if(on[j-1] * rec[j-1] == 1)
				rec[j] = 1;
			else
				rec[j] = 0;
			
		}
	}

	ofstream ou(ouci);  

    if(!ou)	{
		cout << "file open error!\n";
		return;
	}

	if(rec[n - 1] * on[n - 1] == 1)
		ou << "Case #" << c <<": ON" << endl;
	else
		ou << "Case #" << c <<": OFF" << endl;
}*/

void main()	{
	char fi[100] = "D:\\Study\\Topcoder\\GCJ\\A-small-attempt1.in";	//	
	char ouci[50] = {"results_A_small.txt"};

	ifstream ifs(fi);
	if(!ifs) {
		cout << "File open error!" << endl;
		return;
	}

	ofstream ou(ouci);  

    if(!ou)	{
		cout << "file open error!\n";
		return;
	}

	int C, N, K;
	ifs >> C;
	for(int i = 0; i < C; i++)	{
		ifs >> N;
		ifs >> K;
		//Snapper_Chain(N, K, i + 1);
		vector<int> on(N), rec(N);
		for(int k = 0; k < N; k++)	{
			on[k] = 0;
			rec[k] = 0;
		}
		rec[0] = 1;

		for(int k = 0; k < K; k++)	{
			if(on[0] == 0)	
				on[0] = 1;
			else
				on[0] = 0;

			for(int j = 1; j < N; j++)	{
				if(rec[j] == 1)	{
					if(on[j] == 0)	
						on[j] = 1;
					else
						on[j] = 0;
				}
				if(on[j-1] * rec[j-1] == 1)
					rec[j] = 1;
				else
					rec[j] = 0;
			
			}
		}

		if(rec[N - 1] * on[N - 1] == 1)
			ou << "Case #" << i + 1 <<": ON" << endl;
		else
			ou << "Case #" << i + 1 <<": OFF" << endl;
	}
}