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

#define N 50
#define M 1000

int n;
int A[N];
bool B[N];
char S[N];

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int i, j, k, d;
	char c;
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
		rep(i, 0, n)
		{
			in(s, S);
			for(j = n - 1; j >= 0 && S[j] == '0'; --j);
			A[i] = n - j - 1;
			B[i] = 0;
		}
		int res = 0;
		rep(i, 0, n)
		{
			d = 0;
			rep(j, 0, n) if(!B[j])
			{
				if(A[j] >= n - i - 1) break;
				++d;
			}
			assert(j < n);
			res += d;
			B[j] = 1;
		}
		printf("Case #%d: %d\n", iT, res);
	}

	return 0;
}
