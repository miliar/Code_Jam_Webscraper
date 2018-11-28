#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;

//const string PATH = "B-small-attempt0";
const string PATH = "B-large";
//const string PATH = "B";

int main()
{
	stringstream inPath;
	inPath << PATH.c_str() << ".in";
	stringstream outPath;
	outPath << PATH.c_str() << ".out";
	ifstream inFile(inPath.str());
	ofstream outFile(outPath.str());
	int C;
	inFile >> C;
	for(int i = 0; i < C; i++)
	{
		__int64 N, K, B, T;
		inFile >> N >> K >> B >> T;
		vector<__int64> x(N);
		vector<__int64> v(N);
		vector<pair<__int64, __int64> > chick(N);
		for(int j = 0; j < N; j++)
		{
			inFile >> x[j];
		}
		for(int j = 0; j < N; j++)
		{
			inFile >> v[j];
		}
		reverse(x.begin(), x.end());
		reverse(v.begin(), v.end());
		vector<bool> m(N, false);
		for(int j = 0; j < N; j++)
		{
			if(T * v[j] + x[j] >= B)
			{
				m[j] = true;
			}
		}
		int k = 0;
		int p = 0;
		int res = 0;
		while(k < K && p < x.size())
		{
			if(m[p])
			{
				for(int j = 0; j < p; j++)
				{
					if(!m[j])
					{
						res++;
					}
				}
				k++;
			}
			p++;
		}
		if(k >= K)
		{
			outFile << "Case #" << (i+1) << ": " << res << endl;
		}
		else
		{
			outFile << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
		}
	}
	inFile.close();
	outFile.close();
	return 0;
}