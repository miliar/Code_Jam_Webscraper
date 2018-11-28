#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int inf = 1000000;

int N, Q;
vector<string> A, S; // pretrazivaci, upiti
int dp[1005][105];

int main()
{
	int tests;
	scanf("%d", &tests);
	
	for (int test = 1; test <= tests ; ++test)
	{
		A.clear();
		S.clear();
		
		char buf[128];
		
		// ucitam
		scanf("%d ", &N);
		A.resize(N);
		for (int i = 0; i < N; ++i)
		{
			getline(cin, A[i]);
			//cout << "A[" << i << "] = " << A[i] << endl;
		}
		sort(A.begin(), A.end());
		A.resize(unique(A.begin(), A.end()) - A.begin());
		N = A.size();		
		
		scanf("%d ", &Q);
		S.resize(Q);
		for (int i = 0; i < Q; ++i)
		{
			getline(cin, S[i]);
		}
		
		if (Q == 0)
		{
			printf("Case #%d: 0\n", test);
			continue;
		}
		
		// radim posao
		for (int i = 0; i < Q; ++i)
			for (int j = 0; j < N; ++j)
				dp[i][j] = inf;

		for (int i = 0; i < N; ++i)
			if (A[i] != S[0])
				dp[0][i] = 0;

		for (int i = 0; i + 1 < Q; ++i)
		{
			int min1 = inf, min2 = inf;
			for (int j = 0; j < N; ++j)
			{
				min2 = min(min2, dp[i][j]);
				if (min1 > min2)
					swap(min1, min2);
			}
			
			for (int j = 0; j < N; ++j)
			{
				if (A[j] != S[i + 1])
					dp[i + 1][j] = dp[i][j];
				
				if (dp[i][j] == min1)
					dp[i + 1][j] = min(dp[i + 1][j], min2 + 1);
				else
					dp[i + 1][j] = min(dp[i + 1][j], min1 + 1);
			}
		}
		
		int sol = inf;
		for (int i = 0; i < N; ++i)
			sol = min(sol, dp[Q - 1][i]);
		printf("Case #%d: %d\n", test, sol);
	}
	
	//system("pause");
	
	return 0;
}
