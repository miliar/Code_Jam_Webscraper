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

int t,n;
string a[100];
char s[100];

int main()
{
freopen("a-large.in", "r", stdin);
freopen("a-large.out", "w", stdout);
	scanf("%d", &t);
REP(it, t)
{
	scanf("%d%c", &n, &s[0]);
	REP(i, n)
	{
		gets(s);
		a[i]=s;
	}
	int ans=0;
	REP(i, n)
	{
		int j;
		for(j=i; j<n; ++j)
		{
			bool t=1;
			FOR(k, i+1, n) if(a[j][k]=='1') { t=0; break; }
			if(t) break;
		}
		while(j>i) swap(a[j], a[j-1]), --j, ++ans;
	}
	printf("Case #%d: %d\n", it+1, ans);
}
	return 0;
}
