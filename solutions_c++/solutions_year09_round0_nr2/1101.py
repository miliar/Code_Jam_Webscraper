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

const int dx[4]={-1,0,0,1}, dy[4]={0,-1,1,0};
int h,w, t, a[200][200], p[20000];
char c[20000], cc;
int f(int x, int y) { return x*w+y; }
int pr(int x) { return p[x]!=x ? p[x]=pr(p[x]) : p[x]; }

int main()
{
#ifdef LocalHost
freopen("b-large.in", "r", stdin);
freopen("b-large.out", "w", stdout);
#endif
	scanf("%d", &t);
REP(it, t)
{
	scanf("%d%d", &h, &w);
	REP(i, h) REP(j, w)
		scanf("%d", &a[i][j]), p[f(i,j)]=f(i,j);
	int ii,jj,v,r;
	REP(i, h) REP(j, w)
	{
		r=a[i][j]; v=f(i,j);
		REP(u, 4)
		{
			ii=i+dx[u]; jj=j+dy[u];
			if(ii<0 || ii>=h || jj<0 || jj>=w) continue;
			if(a[ii][jj]<r) r=a[ii][jj], v=f(ii,jj);
		}
		if(v!=f(i,j)) p[pr(f(i,j))]=pr(v);
	}
	CL(c, 0);
	cc='a';
	printf("Case #%d:\n", it+1);
	REP(i, h)
	{
		REP(j, w)
		{
			v=pr(f(i,j));
			if(!c[v]) c[v]=cc++;
			printf("%c ", c[v]);
		}
		printf("\n");
	}
}
	return 0;
}
