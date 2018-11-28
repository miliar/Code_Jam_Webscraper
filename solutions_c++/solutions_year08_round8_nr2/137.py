#pragma comment(linker, "/STACK:60777216")
#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <set>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>

using namespace std;
#define ll long long;

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}
int dp[10001];

int numbits(int n)
{
	return (n) ? 1 + numbits(n & (n - 1)) : 0;
}

int main()
{
	cout.precision(18);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int QWR; cin >> QWR;
	
	for(int qwr = 0; qwr < QWR; qwr++)
	{
		int N;
		cin >> N;
		int result = 10000;
		vector< pair<int,int> > which;
		vector< string > colors;
		map< string, int > col;
		int color = 0;

		for(int i = 0; i < N; i++)
		{
			string temp;
			pair<int, int> np;
			cin >> temp >> np.first >> np.second;
			which.push_back(np);
			colors.push_back(temp);
			if(col.count(temp) == 0)
			{
				col[temp] = color; 
				color++;
			}
		}
		int mask = (1 << N);
		for(int i = 1; i < mask; i++)
		{
			memset(dp, 0, sizeof(dp));
			int temporary = 0;
			for(int j = 0; j < N; j++)
				if((1<<j)&i)
				{
					for(int k = which[j].first; k <= which[j].second; k++)
						dp[k] = 1;
					temporary |= (1<<col[colors[j]]);
				}
			bool OK = true;
			if(numbits(temporary) > 3)
				OK = false;
			for(int j = 1; j < 10001; j++)
				if(!dp[j])
					OK = false;
			if(OK)
				result = min(result, numbits(i));
		}
		if(result != 10000)
			cout << "Case #" << qwr + 1 << ": " << result << "\n";
		else
			cout << "Case #" << qwr + 1 << ": " << "IMPOSSIBLE" << "\n";
	}
	return 0;
}