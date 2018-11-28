#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>
#include <fstream>

using namespace std;

const string welc = "welcome to code jam";

int main()
{
	ifstream ifs ("in.in");
	freopen("out.out", "wt", stdout);
	
	int n;
	ifs >> n;
	string t;
	getline(ifs,t);
	int welsz = welc.length();
	for (int kk = 0; kk < n;kk++)
	{
		string t;
		getline(ifs,t);
		int tsz = t.length();
		vector<vector<int> > sol;
		sol.resize(welsz + 1);
		for (int i = 0; i < welsz + 1;i++)
			sol[i].resize(tsz + 1);
		for(int i = 1; i <= welsz;i++)
			for (int j = 1; j <= tsz;j++)
			{
				sol[i][j] = sol[i][j - 1];
				if (t[j - 1] == welc[i - 1] && i != 1)
					sol[i][j]+= 1*sol[i-1][j-1];
				if (i == 1 && t[j - 1] == welc[i - 1])
					sol[i][j]++;
				sol[i][j]%=10000;
			}

		printf("Case #%d: %.4d\n",kk + 1,sol[welsz][tsz]);
	}

	return 0;
}