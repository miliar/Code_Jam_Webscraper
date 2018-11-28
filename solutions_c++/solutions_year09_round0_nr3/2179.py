#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define S(n) scanf("%d",&n)
#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

int dp[600][20];
string istr, sstr;

int solve(int iind, int sind)
{
	int i;
	if(dp[iind][sind] != -1) return dp[iind][sind];
	if(istr[iind] != sstr[sind])
	{
		dp[iind][sind] = 0;
		int ans = 0;
		//for(i = iind + 1; i < istr.SZ; i++)
			//	ans += solve(i, sind);
	
		dp[iind][sind] = ans;
		return ans;
	}
	
	if(sind == sstr.SZ - 1)
	{
		dp[iind][sind] = 1;
		return 1;
	}
	
	int ans = 0;
	REPA(i, iind + 1, istr.SZ)	
	 ans = (ans+ solve(i, sind + 1)) % 10000;
	
	dp[iind][sind] = ans; 
	return ans;
}   


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int n, i;
	cin >> n;
	sstr = "welcome to code jam";
	//fflush(stdin);
	getline(cin,istr,'\n');
	int i1 = 1;
	while(n--)
	{
		memset(dp, -1, sizeof(dp));
		//char buf[600];
		//getline(buf,600, '\n');
		//istr = string(buf);
		//cin >> istr;
		getline(cin,istr,'\n');
		//cin.ignore();
		REP(i,istr.SZ)
			solve(i, 0);
		
		long long ans = 0;
		ans %= 10000;
		REP(i,istr.SZ)
			ans = (ans + (dp[i][0] != -1 ? dp[i][0] : 0)) % 10000;
		stringstream ss;
		ss << ans;
		string res = ss.str();
		if(res.SZ == 1) res = "000" + res;
		else if(res.SZ == 2) res = "00" + res;
			else if(res.SZ==3) res = "0" + res;
		cout << "Case #" << i1++  << ": "<< res << "\n";
	}
	
	return 0;
}
