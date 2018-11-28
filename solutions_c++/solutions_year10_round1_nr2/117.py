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
#include <stdio.h>

using namespace std;

int dp[105][256];
		
int main()
{	
	ofstream fout("B-small-1.txt");
	
//	ifstream fin("B-test.txt");
	ifstream fin("B-small-attempt1.in");
//	ifstream fin("B-large.txt");
		
	int T;
	fin >> T;
	
	for(int t = 0; t < T; t++)
	{
		int D,I,M,N;
		fin >> D >> I >> M >> N;
		
		int a[105];
		for(int i = 0; i < N; i++)
			fin >> a[i];
		
		for(int p = 0; p < 105; p++)
		for(int q = 0; q < 256; q++)
			dp[p][q] = 999999999;
		
		int bestans = D*(N-1);
		for(int p = 0; p < N; p++)
			dp[p+1][a[p]] = D*p;
		for(int p = 0; p <= 255; p++)
			dp[1][p] = min(dp[1][p], abs(a[0]-p));
	
		for(int i = 0; i < N; i++)
		for(int j = 0; j <= 255; j++)
			if(dp[i][j] < 999999999)
			{
				dp[i+1][j] = min(dp[i+1][j], dp[i][j] + D);
				if(M != 0)
				for(int k = 0; k <= 255; k++)
					dp[i+1][k] = min(dp[i+1][k], dp[i][j] + I*((max(abs(k-j)-1,0))/M) + abs(k-a[i]));
			
				for(int k = 0; k <= 255; k++)
					if(abs(k-j)<=M)
					dp[i+1][k] = min(dp[i+1][k], dp[i][j] + abs(a[i]-k));
			}
			
		for(int j = 0; j <= 255; j++)
			bestans = min(bestans, dp[N][j]);
		
		fout << "Case #" << t+1 << ": " << bestans << endl;
	}
	
	return 0;
}