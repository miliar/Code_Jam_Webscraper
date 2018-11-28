/*
 * C.cpp
 *
 *  Created on: 03/09/2009
 *      Author: Hamzawy
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
/*#include <ext/hash_map>
 using namespace __gnu_cxx;*/
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define EPS (1e-9)

char arr[600];
char str[]="welcome to code jam";
int n=strlen(str),len;
int dp[30][600];

int DP(int ind,int cur)
{
	if(ind>=n)
		return 1;
	if(cur>=len)
		return 0;
	if(dp[ind][cur]!=-1)
		return dp[ind][cur];
	int re=0;
	if(str[ind]==arr[cur])
		re+=DP(ind+1,cur+1)%10000;
	re+=DP(ind,cur+1)%10000;
	re=re%10000;
	return dp[ind][cur]=re;
}

int main() {
#ifndef ONLINE_JUDGE
	//freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
#endif
	int t;
	scanf("%d ",&t);
	for(int T=0;T<t;T++)
	{
		mem(dp,-1);
		gets(arr);
		len=strlen(arr);
		printf("Case #%d: %04d\n",T+1,DP(0,0));
	}
	return 0;
}
/*
 * so you've registered. we sent you a welcoming email, to welcome you to code jam. but it's possible that you still don't feel welcomed to code jam. that's why we decided to name a problem "welcome to code jam." after solving this problem, we hope that you'll feel very welcome. very welcome, that is, to code jam.
 */
