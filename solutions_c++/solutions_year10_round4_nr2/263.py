#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <cstdio>

using namespace std;

long long dp[15][1024][12];

int main()
{	
// 	ofstream fout("B-small0.out");
// 	ifstream fin("B-small-attempt0.in");
// 	ofstream fout("B-test.out");
// 	ifstream fin("B-test.in");
	ofstream fout("B-large.out");
	ifstream fin("B-large.in");
	
	int T;
	fin >> T;
	
	for(int t = 0; t < T; t++)
	{
		int k;
		fin >> k;
		int M[1024];
		for(int p = 0; p < (1<<k); p++)
		{
			fin >> M[p];
			M[p] = k - M[p];
		}
		
		for(int i = 0; i < 15; i++)
		for(int j = 0; j < 1024; j++)
		for(int kk = 0; kk < 12; kk++)
			dp[i][j][kk] = 1000000000000000LL;
			
		for(int j = 0; j < (1<<k); j++)
		for(int kk = 0; kk < 12; kk++)
			if(kk >= M[j])
				dp[0][j][kk] = 0;
		
		int currTeams = (1<<k);
			
		for(int i = 1; i <= k; i++)
		{
			currTeams /= 2;
			int costs[1024];
			for(int p = 0; p < currTeams; p++)
				fin >> costs[p];
		
			for(int j = 0; j < currTeams; j++)
			for(int kk = 0; kk < 11-i; kk++)
			{
				dp[i][j][kk] = min(dp[i-1][2*j][kk] + dp[i-1][2*j+1][kk],
							    costs[j] + dp[i-1][2*j][kk+1] + dp[i-1][2*j+1][kk+1]);
			}
		}	
		
		cout << dp[k][0][0] << endl;
		
		
		fout << "Case #" << t+1 << ": "  << dp[k][0][0] << endl;
	}
	
	return 0;
}