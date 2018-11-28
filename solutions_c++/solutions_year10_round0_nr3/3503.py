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

void main()	{
	char fi[100] = "D:\\Study\\Topcoder\\GCJ\\C-small-attempt0.in";	//	
	char ouci[50] = {"results_C_small.txt"};

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
	
	int T, R, K, N;
	ifs >> T;
	for(int j = 0; j < T; j++)	{
		ifs >> R;
		ifs >> K;
		ifs >> N;
		deque<int> g(N), p;//(N)
		for(int k = 0; k < N; k++)	{
			ifs >> g[k];
		}
		int res = 0;
		for(int i = 0; i < R; i++)	{
			int n = 0;//, j = 0
			while(!g.empty())	{//1
				if(n + g[0] <= K)	{//&&!g.empty()
					n += g[0];
					int temp = g[0];
					g.pop_front();
					p.push_back(temp);
				}
				else	{//if(g.empty() || n + g[0] > K)
					res += n;
					break;
				}
			}

			if(g.empty())
				res += n;

			while(!p.empty())	{
				int temp = p[0];
				p.pop_front();
				g.push_back(temp);
			}
		}
		ou << "Case #" << j + 1 <<": " << res << endl;
	}
}