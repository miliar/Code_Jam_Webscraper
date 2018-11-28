/*
 * C_1.cpp
 *
 *  Created on: 13/09/2009
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
using namespace std;

/*
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
*/

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
const long double PI = (2.0*acos(0.0));


int dp[10001][10001];
int arr[101];
int q,p,t;

int DP(int s,int e)
{
	if(dp[s][e]!=-1)return dp[s][e];
	int re=OO;
	bool f=0;
	for(int i=0;i<q;i++)
	{
		if(arr[i]>=s&&arr[i]<=e)
			re=min(re,DP(s,arr[i]-1)+DP(arr[i]+1,e)+arr[i]-s+e-arr[i]),f=1;
	}
	if(!f)return dp[s][e]=0;
	return dp[s][e]=re;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "rt", stdin);
	freopen("2.txt", "wt", stdout);
#endif
	scanf("%d", &t);
	rep(K,t) {
		scanf("%d%d", &p, &q);
		rep(i,q)
			scanf("%d", arr + i);
		mem(dp,-1);
		printf("Case #%d: %d\n",K+1,DP(1,p));
	}
	return 0;
}
