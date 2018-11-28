#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



int n;
int p;
int m[3000];
int c[3111];



long long dp[3111][11];


void Load()
{
	cin >> p;
	n = 1 << p;
	int i, j;
	int k = 2*n-1;
	for (i = 0; i < n; i++)
		cin >> c[k--];
	for (i = p-1; i >= 0; i--)
	{
		for (j = 1; j <= (1 << (i)); j++)
			cin >> c[k--];
	}


}


long long F(int v, int l)
{
	if (dp[v][l] >= 0) return dp[v][l];
	if (v >= n)
	{
		if (l > c[v]) return 2000000000000ll;
		else return 0;
	}
	long long bst, cur;
	bst = F(2*v,l+1)+F(2*v+1,l+1);
	cur = c[v] + F(2*v,l)+F(2*v+1,l);
	if (cur < bst) 
		bst = cur;
	dp[v][l] = bst;
	return bst;
}


void Solve()
{
	memset(dp, -1, sizeof(dp));
	cout << F(1, 0) << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
