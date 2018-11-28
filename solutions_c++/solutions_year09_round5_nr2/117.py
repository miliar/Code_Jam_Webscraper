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

const int m = 10009;
int n,k, l, o[111];
char p[60], a[111][50];
int ans;
int b[111][26], v[26];

int val ()
{
	int x=1, res=0;
	REP(i, l)
	{
		if(p[i]=='+') res+=x, x=1;
		else x=(x*v[p[i]-'a']) % m;
	}
	return (res+x) % m;
}

void go (int k)
{
	if(k==0)
	{
		ans = (ans+val()) % m;
		return;
	}
	REP(i, n)
	{
		REP(j, 26) v[j]+=b[i][j];
		go(k-1);
		REP(j, 26) v[j]-=b[i][j];
	}
}

int main()
{
freopen("B-small-attempt0.in", "r", stdin);
freopen("b-small.out", "w", stdout);
	int t;
	scanf("%d", &t);
REP(it, t)
{
	scanf("%s%d%d", p, &k, &n);
	CL(b, 0);
	REP(i, n)
	{
		scanf("%s", a[i]);
		l=strlen(a[i]);
		REP(j, l) ++b[i][a[i][j]-'a'];
	}
	l=strlen(p);
	printf("Case #%d:", it+1);
	FOR(d, 1, k+1)
	{
		ans=0;
		go(d);
		printf(" %d", ans);
	}
	printf("\n");
}	
	return 0;
}
