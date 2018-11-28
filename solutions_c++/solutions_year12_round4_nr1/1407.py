#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <utility>
#include <deque>
#include <list>
#include <string>
#include <cassert>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define forl(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<=int(b); ++i)
#define all(a) a.begin(), a.end()
#define allr(a) a.rbegin(), a.rend()
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define ll long long
#define pii pair <int,int>
#define sz(a) a.size()
#define np next_permutation
# define ull unsigned long long
const int INF = (int)1e9;
const long long INF64 = (long long) 1e8;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
bool ineedoutputfile = true;
vector < pair<int,int> > d; int dist; int n;
int dp[10001][10001];
int solve (int k, int l) {
	if (dp[k][l]!=-1)
		return dp[k][l];
	int q = min(d[k].first-d[l].first,d[k].second);
	if (dist - d[k].first<=q)
		return dp[k][l]=1;
	forab(i,k+1,n)
	{
		if (d[i].first-d[k].first<=q) {
			if (solve(i,k))
				return dp[k][l]=1;
		}
	}
	return dp[k][l]=0;
}
int main () {
#ifndef ONLINE_JUDGE
	freopen("input.txt","rt",stdin);
	if (ineedoutputfile)
		freopen("output.txt","wt",stdout);
#endif
	int testcases;
	cin >> testcases;
	for(int testcase = 1; testcase <= testcases; testcase++) {
		printf("Case #%d: ", testcase);
		cin >> n;
		d.clear();
		memset(dp,-1,sizeof(dp));
		d.resize(n+1);
		d[0].first = 0;
		d[0].second = 0;
		forn(i,n) {
			cin >> d[i+1].first >> d[i+1].second;
		}
		cin >> dist;
		if (solve(1,0)) 
			puts("YES");
		else
			puts("NO");
	}
}