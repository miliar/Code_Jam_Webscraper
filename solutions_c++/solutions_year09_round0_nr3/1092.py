#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define UN(v) sort(all(v)),(v).erase(unique((v).begin(),(v).end()),(v).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const char *s="welcome to code jam";
int t, m,n;
char a[1000];
int v[1000][21];

int main()
{
#ifdef LocalHost
freopen("c-large.in", "r", stdin);
freopen("c-large.out", "w", stdout);
#endif
	scanf("%d%c", &t, &a[0]);
	m=strlen(s);
REP(it, t)
{
	gets(a);
	n=strlen(a);
	CL(v, 0);
	v[0][0]=1;
	REP(i, n)
	{
		REP(j, m+1) v[i+1][j]=v[i][j];
		REP(j, m) if(a[i]==s[j])
			v[i+1][j+1]=(v[i+1][j+1]+v[i][j])%10000;
	}
	printf("Case #%d: %04d\n", it+1, v[n][m]);
}
	return 0;
}
