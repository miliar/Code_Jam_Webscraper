#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<cstring>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;
char s[510];
int n;
char* targ = "welcomeXtoXcodeXjam";
int ntarg;
int dp[510][30];
#define MOD 10000;
int foo(int pos, int tpos)
{
	if(tpos >= ntarg)
		return 1;
	if(pos >= n)
		return 0;
	int i, j, k;
	int &ret = dp[pos][tpos];
	if(ret != -1)
	{
		return ret;
	}
	ret = 0;
	ret += foo(pos + 1, tpos);
	ret %= MOD;
	if(targ[tpos] == s[pos])
	{
		ret += foo(pos + 1, tpos + 1);
		ret %= MOD;
	}
	return ret;
}
void solve()
{
	int i, j, k;
	CLRM(dp);
	int ans = foo(0, 0);
	int t = 1000;
	for(i = 0; i < 4; i++)
	{
		printf("%d",ans/t);
		ans %= t;
		t /= 10;
	}
	printf("\n");
}
int main()
{
	ntarg = strlen(targ);
	int tes;
	scanf("%d", &tes);
	int tot;
	getchar();
	for(tot = 1; tot <= tes; tot++)
	{
		gets(s);
		//cout << s << endl;
		//getchar();
		int i, j, k;
		n = strlen(s);
		for(i = 0; i < n; i++)
		{
			if(s[i] == ' ')
				s[i] = 'X';
		}
		printf("Case #%d: ", tot);
		solve();
	}
	return 0;
}
