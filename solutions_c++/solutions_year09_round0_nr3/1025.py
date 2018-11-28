#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <sstream>
#include <cstring>
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,v) for (int i = 0; i < v.size(); i++)
#define fors(i,s) for (int i = 0; i < s.length(); i++)
#define rep(i,f,t) for (int i = (int)(f); i < (int)(t); i++)
#define per(i,f,t) for (int i = f; i > t; i--)
#define fe(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define ft first
#define sd second
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PIS pair< int, string >
#define VPIS vector< PIS >
#define VPII vector< PII >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pname "domino"
#define mod 1000000007LL
#define pi 3.1415926535
#define have(u,v) (u&(1<<v))
#define maxn 50000
#define inf (1<<20)
#define ll long long
#define maxnm 105
using namespace std;

string tpl="welcome to code jam";
int dp[600][20];
char buf[10000];
int solve() {
	gets(buf);
	string u(buf);
	int n=u.sz, m=tpl.sz;
	
	for (int i = 1; i <= m; i++)dp[0][i]=0;
	forn(i,n+1)dp[i][0]=1;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++) {
			dp[i][j]=0;
			if (u[i-1]==tpl[j-1])
				dp[i][j]+=dp[i-1][j-1]%10000;
			dp[i][j]+=dp[i-1][j]%10000;
			dp[i][j]%=10000;
		}
	
	return dp[n][m];
}

int main() {

   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);

	int t;
	scanf("%d\n",&t);
	forn(i,t) {
		printf("Case #%d: %04d\n",i+1, solve());
	}
	return 0;
}	

