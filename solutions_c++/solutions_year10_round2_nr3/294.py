#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MOD = 100003;

const int MAXN = 500;

int binom[MAXN+1][MAXN+1];
int ans[MAXN+1][MAXN+1];

int getAns(int n, int r)
{
	if (ans[n][r] == -1)
	{
		ans[n][r] = 0;
		if (r == 1)
			ans[n][r] = 1;
		for(int i=1; i<r; i++)
			ans[n][r] = (ans[n][r]+getAns(r, i)*binom[n-r-1][r-i-1])%MOD;
	}
	return ans[n][r];
}

void work()
{
	int n;
	cin >> n;
	int res = 0;
	for(int r=1; r<n; r++)
		res  = (res+getAns(n, r))%MOD;
	cout << res << endl;
}

void makeBinom()
{
	memset(binom, 0, sizeof(binom));
	binom[0][0] = 1;
	for(int i=1; i<=MAXN; i++){
		binom[i][0] = 1;
		for(int j=1; j<=MAXN; j++)
			binom[i][j] = (binom[i-1][j-1]+binom[i-1][j])%MOD;
	}
}

int main()
{
	int T;
	makeBinom();
	memset(ans, -1, sizeof(ans));
	cin >> T;
	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		work();
	}
}

