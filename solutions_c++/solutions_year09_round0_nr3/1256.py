#include <iostream>
#include <string>
          
using namespace std;

int n,i,j,p,q;
char s[501];
string c;
int dp[501][30],k;

int rec(int i,int j)
{
	if (j == q) return 1;
	if (i == p) return 0;
	if (dp[i][j] != -1) return dp[i][j];
	dp[i][j] = rec(i+1,j)%10000;
	if (s[i] == c[j]) dp[i][j] += rec(i+1,j+1);
	dp[i][j] = dp[i][j]%10000;
	return dp[i][j];
}

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cin >> n;
	c = "welcome to code jam";
	gets(s);
	for (i = 1;i<=n;i++)
	{
		gets(s);
		p = strlen(s);
		q = c.length();
		memset(dp,-1,sizeof(dp));
		k = rec(0,0);
		cout << "Case #" << i << ": ";
		if (k<10) cout << "000" << k << endl;
		else if (k<100) cout << "00" << k << endl;
		else if (k<1000) cout << "0" << k << endl;
		else cout << k%10000 << endl;  	
	}
	return 0;
}                              