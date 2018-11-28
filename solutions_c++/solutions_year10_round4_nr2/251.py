#include <iostream>

using namespace std;

int M[1024];
int A[10][512], dp[10][512][10];

int fun(int r, int n, int le)
{
	if(r == -1) return (le>M[n]?-2:0);
	if(dp[r][n][le] != -1) return dp[r][n][le];
	dp[r][n][le] = -2;
	int p,q;
	p = fun(r-1,n*2,le+1); q = fun(r-1,n*2 + 1,le+1);
	if(p != -2 && q != -2) dp[r][n][le] = p+q;
	p = fun(r-1,n*2,le); q = fun(r-1,n*2 + 1,le);
	if(p != -2 && q != -2)
	{
		if(dp[r][n][le] == -2) dp[r][n][le] = p+q+A[r][n];
		else dp[r][n][le] <?= p+q+A[r][n];
	}
	return dp[r][n][le];
}

int main()
{
	int T,cn=1;
	cin >> T;
	while(T--)
	{
		int N;
		cin >> N;
		for(int i=0;i<(1<<N);i++) cin >> M[i];
		for(int i=0;i<N;i++) for(int j=0;j<(1<<(N-i-1));j++) cin >> A[i][j];
		memset(dp,-1,sizeof(dp));
		cout << "Case #" << cn << ": " << fun(N-1,0,0) << endl;
		cn++;
	}
	return 0;
}
