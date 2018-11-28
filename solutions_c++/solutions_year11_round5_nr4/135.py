#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
using namespace std;
#pragma comment(linker, "/STACK:255000000")

typedef long long ll;

#define rep(i, a, b) for(i = (a); i < (b); ++i)
#define repb(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define repd(i, a, b, d) for(i = (a); i < (b); i += (d))
#define repbd(i, a, b, d) for(i = (a) - 1; i >= (b); i -= (d))
#define reps(i, s) for(i = 0; (s)[i]; ++i)
#define repl(i, l) for(i = l.begin(); i != l.end(); ++i)

#define in(f, a) scanf("%"#f, &(a))

bool firstout = 1;

#define out(f, a) printf("%"#f, (a))
#define outf(f, a) printf((firstout) ? "%"#f : " %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

#define inf 1012345678
#define eps 1e-9

#define N 1012
#define M 1012

#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000009
#endif

int n, m;
int A[N];

bool sq(ll x)
{
	ll y = sqrt(1. * x) + 2;
	for(; y * y > x; --y);
	return y * y == x;
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
	int ts;	
#if 1
	int tss;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
		cerr << ts << endl;
		printf("Case #%d: ", ts);
		char s[66];
		scanf("%s", s);
		int n = strlen(s);
		vector<int> q;
		for(i = 0;i < n;i++) if(s[i]=='?') q.push_back(i);
		int m=q.size();
		char w[66];
		for(int mask=0;mask < (1 << m);mask++)
		{
			strcpy(w,s);
			for(i=0;i<m;i++) w[q[i]]=((mask >> i) & 1)?'0':'1';
			ll x=0;
			for(i=0;i<n;i++) x=2*x+w[i]-'0';
			if(sq(x)) break;
		}
		puts(w);
	}

	return 0;
}