#include <iostream>
#include <algorithm>
using namespace std;

int T, N, S, p;
int DP[101][101];
int points[101];

int solve(int n, int s)
{
	if (s < 0) return -1;
	if (n < 0) return 0;
	if (DP[n][s] != -1)
		return DP[n][s];
	
	int po = points[n];
	int d = po / 3;
	if (po % 3 == 0) {
		return DP[n][s] = max(solve(n-1,s) + (d >= p ? 1 : 0), solve(n-1,s-1) + (d+1 >= p && d-1 >= 0 ? 1 : 0));
	} else if (po % 3 == 1) {
		return DP[n][s] = max(solve(n-1,s) + (d+1 >= p ? 1 : 0), solve(n-1,s-1) + (d+1 >= p && d-1 >= 0? 1 : 0));
	} else {
		return DP[n][s] = max(solve(n-1,s) + (d+1 >= p ? 1 : 0), solve(n-1,s-1) + (d+2 >= p ? 1 : 0));
	}
}

int main()
{
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		cin >> N >> S >> p;
		for (int i=0; i<N; i++)
		{
			cin >> points[i];
			for (int s=0; s<=S; s++)
				DP[i][s] = -1;
		}
		cout << "Case #" << t << ": " << solve(N-1, S) << endl;
		// for (int n=0; n<N; n++)
		// {
		// 	for (int s=0; s<=S; s++)
		// 		cout << DP[n][s] << " ";
		// 	cout << endl;
		// }
	}

	return 0;
}