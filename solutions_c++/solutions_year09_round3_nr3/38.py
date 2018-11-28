#include <iostream>

using namespace std;

int arr[200];
int dp[200][200];
int P, Q;

int go(int s, int e)
{
	if(dp[s][e] >= 0)
	{
		return dp[s][e];
	}
	int &res = dp[s][e];
	res = (int) 1E9;
	for(int i = s+1; i <= e; i++)
	{
		res = std::min(res, ((arr[e + 1] - arr[s] - 2) + go(s, i-1) + go(i, e)));
	}
	if(res == (int) 1E9)
		res = 0;
	return res;
}


int main()
{
	int N;
	cin >> N;
	for(int NN = 1; NN <= N; NN++)
	{
		cin >> P >> Q;
		memset(dp, -1, sizeof(dp));
		for(int i = 1; i <= Q; i++)
		{
			cin >> arr[i];
		}
		arr[0] = 0;
		arr [Q + 1] = P + 1;
		cout << "Case #" << NN << ": " << go(0, Q) << endl;
	}

	return 0;
}
