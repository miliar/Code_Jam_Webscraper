#include <iostream>

using namespace std;

int c[510][510];
int f[601][601];
int n;
int mod = 100003;

void prepare()
{
	memset(c,0,sizeof(c));
	c[0][0] = 1;
	c[1][1] = c[1][0] = 1;
	for (int i=2; i<=500; i++) {
		c[i][0] = c[i][i] = 1;
		for (int j=1; j<i; j++)
			c[i][j] = (c[i-1][j-1]+c[i-1][j])%mod;
	}	
	memset(f,-1,sizeof(f));
}
int calc(int n, int k) {	
	if (f[n][k]!=-1) return f[n][k];
	if (k==1) return f[n][k] = 1;
	int s =0;
	for (int l=k-1;l>0 && k-l<=n-k; l--)
		s=(s+calc(k,l)*c[n-k-1][k-l-1])%mod;
	f[n][k] = s;
	return s;
}
int calc()
{
	int ans = 0;
	for (int i=1; i<n; i++)
		ans = (ans+calc(n,i))%mod;
	return ans;
}
int main()
{
	prepare();
	int t;
	cin>>t;
	for (int i=1; i<=t; i++) {
		cin>>n;
		printf("Case #%d: %d\n", i, calc());
	}
}
