#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <functional> 

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int MAX = 10000;

//bool cells[MAX];
//bool prisoner[MAX];
vector<int> prisoners;
//int dp[MAX][MAX];
int p, q;
map<long long, int> dp;

int DP(int start, int end)
{
	if(dp.find(start * MAX + end) != dp.end())
	{
		return dp[start * MAX + end];
	}

	int min = 2147483647;
	int curr;
	for(int i = 0; i < prisoners.size(); ++i)
	{
		if(prisoners[i] > end)
		{
			break;
		}
		if(prisoners[i] >= start)
		{
			curr = DP(start, prisoners[i] - 1) + DP(prisoners[i] + 1, end);
			if(curr < min)
			{
				min = curr;
			}
		}
	}

	if(min < 2147483647)
	{
		dp[start * MAX + end] = end - start + min;
	}
	else
	{
		dp[start * MAX + end] = 0;
	}

	//cout << start << "," << end << " " << dp[start * MAX + end] << endl;

	return dp[start * MAX + end];
}

//int Calc()
//{
//	//memset(cells, 0, sizeof(cells));
//	//memset(dp, 0, sizeof(dp));
//
//	return DP(0, p - 1);
//}

int main()
{
	int n;
	fin >> n;

	for(int i = 0; i < n; ++i)
	{
		fin >> p >> q;
		
		int num;
		prisoners.clear();
		dp.clear();
		for(int j = 0; j < q; ++j)
		{
			fin >> num;
			prisoners.push_back(num);
			//prisoner[p] = true;
		}

		//cout << i + 1 << endl;
		fout << "Case #" << i + 1 << ": " << DP(1, p) << endl;
	}

	return 0;
}