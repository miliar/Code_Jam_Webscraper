#define DEBUG 1

using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep(i, a, b, x) for(int i(a), _b(b); i <= _b; i += x )
#define rep(i, n) _rep( i, 0, n - 1, 1 )
#define rrep(i, a, b) for(int i(a),_b(b); i >= (_b); --i)
#define xrep( i, a, b ) _rep(i, a, b, 1)
#define foreach(type, v, it) for(type::iterator it = v.begin(); it!=v.end(); ++it)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

#define dbg(x) if(DEBUG) cerr << __LINE__ << ": " << #x << " -> " << (x) << "\t";
#define dbge(x) if(DEBUG) cerr << __LINE__ << ": "<<#x << " -> " << (x) << endl;


typedef vector <int> vi;

// She
// May be the reason I survive
// The why and wherefore I'm alive
// The one I'll care for through the rough in ready years

//...
const int N = 50;
char brd[N+2][N+2];
char rot[N+2][N+2];

int n;

void ROT()
{
	rep(i,n) rep(j,n)
	{
		rot[j][n-i-1] = brd[i][j];
	}
}

void GRAV()
{
	ms(brd,0);
	
	bool flag;
	
	while (true)
	{
		flag = false;
		rrep(i,n-1,0) rep(j,n)
		{
			if (rot[i][j] == '.') continue;
			if (rot[i+1][j] == '.') swap(rot[i+1][j], rot[i][j]), flag = true;
		}
		
		if (!flag) break;
		
	}
}

int dp[50][50][2][5];

int main()
{
	int t, K;
	
	freopen("f:/data/A-large.in.txt","r",stdin);
	freopen("f:/data/orah.txt","w",stdout);
	
	scanf("%d",&t);
	
	xrep(tc,1,t)
	{
	ms(brd,0); ms(rot,0);
	scanf("%d %d",&n, &K);
	rep(i,n) scanf("%s",brd[i]);
	ROT();
	GRAV();
	ms(dp,0);
	
	rep(i,n) rep(j,n)
	{
		if (rot[i][j] == '.') continue;
		
		int type = rot[i][j] == 'R' ? 0 : 1;
		dp[i][j][type][0] = dp[i][j][type][1] = dp[i][j][type][2] = dp[i][j][type][3] = dp[i][j][type][4] = 1;
		if (i-1>=0 && rot[i][j] == rot[i-1][j]) dp[i][j][type][1] >?= max(dp[i-1][j][type][1] + 1, dp[i-1][j][type][0] + 1);
		if (j-1>=0 && rot[i][j] == rot[i][j-1]) dp[i][j][type][2] >?= max(dp[i][j-1][type][2] + 1, dp[i][j-1][type][0] + 1);
		if ((i-1>=0 && j-1>=0) && rot[i][j] == rot[i-1][j-1]) dp[i][j][type][3] >?= max(dp[i-1][j-1][type][3] + 1, dp[i-1][j-1][type][0] + 1);
		if (i-1>=0 && j+1<n && rot[i][j] == rot[i-1][j+1]) dp[i][j][type][4] >?= max(dp[i-1][j+1][type][4] + 1, dp[i-1][j+1][type][0] + 1);
	}

	bool okr = false, okb = false;
	rep(i,n) rep(j,n) rep(x,5)
	{
		if (dp[i][j][0][x] == K) okr = true;
		else if (dp[i][j][1][x] == K) okb = true;
	}
	
	string ans;
	if (okr && okb) ans = "Both";
	else if (okr) ans = "Red";
	else if (okb) ans = "Blue";
	else ans = "Neither";
	
	printf("Case #%d: %s\n", tc, ans.c_str());
	
	}
	
	//system("pause");
	
	return 0;
}
