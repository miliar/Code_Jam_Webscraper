#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;

int dp[510][19];
string a = "welcome to code jam";
string in;
int calc(int ind,int c)
{
	if(c>18)return 1;
	if(ind>=sz(in))return 0;
	int & r = dp[ind][c];
	if(r!=-1)return r;
	int rs = 0;
	if(a[c]==in[ind])
		rs = calc(ind+1,c+1)%10000;
	rs+=(calc(ind+1,c))%10000;
	rs%=10000;
	return r = rs;
}
int main()
{
	//freopen("inp.in","rt",stdin);
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);

	int tt;
	cin>>tt;
	int n = 0;
	getline(cin,in);
	while(tt--)
	{
		getline(cin,in);
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %.4d\n",++n,calc(0,0)%10000);
	}

	return 0;
}
