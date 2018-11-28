#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

#define FORI(N) for (int i = 0; i < (N); i++)
#define FORIE(N) for (int i = 1; i <= (N); i++)
#define FORJ(N) for (int j = 0; j < (N); j++)
#define FORK(N) for (int k = 0; k < (N); k++)

char buf[1000];
int getInt()
{
	cin.getline (buf, 1000);
	int nu;
	sscanf (buf, "%ld", &nu);
	return nu;
}

int dp[1001][100];

int main()
{
	int T;
	T = getInt();
	for (int t = 1; t <= T; t++)
	{
		int N, M;
		N = getInt();
		map < string , int > A;
		int k = 0;
		FORI(N)
		{
			cin.getline (buf, 1000);
			string tmp (buf);
			A[tmp] = k++;
		}
		vector <int> L;
		M = getInt();
		FORI(M)
		{
			cin.getline (buf, 1000);
			string tmp (buf);
			L.push_back (A[buf]);
		}
		FORIE(M) FORJ(N) dp[i][j] = 1000000000;
		FORJ(N) dp[0][j] = 0;
		FORIE(M) FORJ(N) if (L[i-1] != j) FORK(N)
				dp[i][j] = min (dp[i][j], dp[i-1][k] + (j != k));
		int be = 1000000000;
		FORI(N) be = min (be, dp[M][i]);
		cout << "Case #" << t << ": " << be << endl;
	}
	return 0;
}
