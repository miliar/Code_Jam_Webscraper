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
#define outf(f, a) printf((firstout) ? "%"#f : ", %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

#define inf 1000000000
#define eps 1e-9

#define N 111
#define M 1111

int n, m;
char A[26][26];
bool B[26][26];
char S[N];
char SS[N];
int D[26];

void add(char c)
{
	if(m == 0)
	{
		S[m++] = c;
		++D[c - 'A'];
		return;
	}
	if(A[S[m - 1] - 'A'][c - 'A'])
	{
		--m;
		--D[S[m] - 'A'];
		add(A[S[m] - 'A'][c - 'A']);
		return;
	}
	int i;
	rep(i, 0, 26) if(D[i] && B[i][c - 'A']) break;
	if(i < 26)
	{
		m = 0;
		rep(i, 0, 26) D[i] = 0;
		return;
	}
	S[m++] = c;
	++D[c - 'A'];
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
#if 1
	int tss, ts;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		rep(i, 0, 26) rep(j, 0, 26) A[i][j] = B[i][j] = 0;
		in(d, n);
		rep(k, 0, n)
		{
			in(s, S);
			i = S[0] - 'A';
			j = S[1] - 'A';
			A[i][j] = A[j][i] = S[2];
		}
		in(d, n);
		rep(k, 0, n)
		{
			in(s, S);
			i = S[0] - 'A';
			j = S[1] - 'A';
			B[i][j] = B[j][i] = 1;
		}
		m = 0;
		rep(i, 0, 26) D[i] = 0;
		in(d, n);
		in(s, SS);
		rep(k, 0, n) add(SS[k]);
		printf("Case #%d: ", ts);
		out(c, '[');
		rep(i, 0, m) outf(c, S[i]);
		out(c, ']'); nl;
	}

	return 0;
}
