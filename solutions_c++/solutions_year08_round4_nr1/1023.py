#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define sz(X) ((int)(X.size()))
#define ln(X) ((int)(X.length()))
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define rrep(i,s,n) for(int i=n-1; i>=s; i--)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define err 1E-15
#define INF 1000000

using namespace std;
int M;
struct node
{
	int type, val;
	bool isleaf, ch;
};
node nodes[2002];
int dp[1001][2];
int solve(int s, int v)
{
	//cout<<s<<v<<endl;
	if(dp[s][v] != -1) return dp[s][v];
	int ret0 = INF, ret1 = INF;
	int l0 = solve(2 * s + 1, 0);
	int l1 = solve(2 * s + 1, 1);
	int r0 = solve(2 * s + 2, 0);
	int r1 = solve(2 * s + 2, 1);
	if(v == 1)
	{
		ret0 = min(l1,r1);
		ret1 = l1 + r1;
	}
	else
	{
		ret0 = l0 + r0;
		ret1 = min(l0,r0);
	}
	int ret;
	if(nodes[s].type == 0) ret =  ret0; 
	else ret = ret1;
	if(nodes[s].ch) ret = min(ret,1 + min(ret0,ret1));
	return dp[s][v] = ret;
	
	
}
int main()
{
	//freopen("sin.txt","r",stdin) ;
	//freopen("sout.txt","w",stdout) ;
	int runs;
	cin>>runs;
	rep(cnt,1,runs+1)
	{
		int v;
		cin>>M>>v;
		rep(i,0,M) rep(j,0,2) dp[i][j] = -1;
		int i = 0;
		for(; i < (M - 1) / 2; i++)
		{
			int t;
			cin>>nodes[i].type>>t;
			nodes[i].ch = (t == 1);
			nodes[i].isleaf = false;
			nodes[i].val = -1;
		}
		
		for(; i < M; i++)
		{
			nodes[i].isleaf = true;
			nodes[i].ch = false;
			cin>>nodes[i].val;
			dp[i][nodes[i].val] = 0;
			dp[i][1 - nodes[i].val] = INF;
		}
		int ans = solve(0,v);
		//rep(i,0,M) { cout<<i<<" ";rep(j,0,2) cout<<dp[i][j]<<' '; cout<<endl;}  
		cout<<"Case #"<<cnt<<": ";
		if(ans >= INF)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
