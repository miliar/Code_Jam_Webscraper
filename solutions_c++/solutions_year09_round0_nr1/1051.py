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

char a[6000][20], b[1000];
int l,d,n;
bool y[20][30];

int main()
{
#ifdef LocalHost
freopen("A-large.in", "r", stdin);
freopen("a-large.out", "w", stdout);
#endif
	scanf("%d%d%d", &l, &d, &n);
	REP(i, d) scanf("%s", a[i]);
	REP(i, n)
	{
		scanf("%s", b);
		CL(y, 0);
		int u=0;
		REP(j, l) if(b[u]=='(')
		{	++u;
			while(b[u]!=')') y[j][b[u++]-'a']=1;
			++u;
		}
		else y[j][b[u++]-'a']=1;
		int k=0;
		bool t=0;
		REP(v, d)
		{
			t=1;
			REP(j, l) if(!y[j][a[v][j]-'a']) { t=0; break; }
			if(t) ++k;
		}
		printf("Case #%d: %d\n", i+1, k);
	}
	return 0;
}
