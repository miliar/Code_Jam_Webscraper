// esta3anna 3al sha2a belAllah ..
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define rep(i,n,m) for( int i = (int) n ; i < (int) m ; ++i )
#define	rrep(i,n,m) for( int i = (int) n ; i >= (int) m ; --i )
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define pb(x) push_back(x)
#define mp make_pair
#define mems(arr,v) memset(arr,v,sizeof arr)
#define setb(x,bit) (x|(1<<bit))
#define resetb(x,bit) (x&(~(1<<bit)))
#define is0(x,bit)((x&(1<<bit))==0)
#define is1(x,bit)((x&(1<<bit))!=0)
#define INT_MAX  2000000000
#define INT_MIN -2000000000
#define debug(x) cout << #x << " : " << x << endl
typedef long long ll;
typedef long double ld;
#define Read() freopen("input.txt","r",stdin)
#define Write() freopen("output.txt","w",stdout)
vector<vector<int> > adjList;
int dp[1001][1001];
int rec(int i, int j)
{
	if(i == j)
		return 1;
	if(dp[i][j] != -1)
		return dp[i][j];
	dp[i][j] = 0;
	rep(k,0,adjList[i].sz)
		dp[i][j] += rec(adjList[i][k],j);
	return dp[i][j];
}
int main ()
{
	Read();
	Write();
	int cases;
	int n,m,koko;
	cin >> cases;
	rep(C,1,cases+1)
	{
		cin >> n;
		adjList.clear();
		adjList.resize(n);
		rep(i,0,n){
			cin >> m;
			rep(j,0,m){
			cin >> koko;
			-- koko;
			adjList[i].pb(koko);
			}
		}
		mems(dp,-1);
		int Counter = 0;
		rep(i,0,n)
			rep(j,0,n)
			Counter += (rec(i,j) >= 2);
		if(Counter)
		cout << "Case #" << C << ": Yes" << endl;
		else
		cout << "Case #" << C << ": No" << endl;
	}
}