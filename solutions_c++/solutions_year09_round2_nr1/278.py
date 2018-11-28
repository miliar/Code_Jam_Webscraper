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
using namespace std;

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

#define inf 1000000000
#define eps 1e-9

#define N 10000
#define M 1000

int n, m;
double A[N];
string B[N];
int C[N];
set<string> S;

char cc[2];
char &c = cc[0];
string s;
int t;

int mktr(int i)
{
	in(lf, A[i]);
	in(1s, c);
	if(c == ')')
	{
		B[i] = "";
		return i + 1;
	}
	s = c;
	for(; in(1s, c) > 0 && c != '(';) s += c;
	B[i] = s;
	C[i] = mktr(i + 1);
	in(1s, c);
	t = mktr(C[i]);
	in(1s, c);
	return t;
}

double cnt(int i)
{
	double res = A[i];
	if(B[i] == "") return res;
	if(S.find(B[i]) != S.end()) return res * cnt(i + 1);
	return res * cnt(C[i]);
}

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int i, j, k, d;
	char cc[2];
	char &c = cc[0];
	int a;
	
#if 1
	int T, iT;
	in(d, T);
	rep(iT, 1, T + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		in(d, n);
		in(1s, c);
		mktr(0);
		in(d, n);

		printf("Case #%d:\n", iT);
		rep(i, 0, n)
		{
			S.clear();
			string s;
			cin >> s;
			in(d, m);
			rep(j, 0, m) cin >> s, S.insert(s);
			out(.7lf, cnt(0)); nl;
		}
	}

	return 0;
}
