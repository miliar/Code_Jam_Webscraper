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

#define N 1000010
#define M 1000

int n, m;
bool P[N];
int A[N];
int K[N];

void sieve(int n)
{
	int i, j, k;
	P[0] = P[1] = 0;
	P[2] = 1;
	for(i = 4; i < n; i += 2) P[i] = 0;
	for(i = 3; i < n; i += 2) P[i] = 1;
	for(i = 3; i * i < n; i += 2) if(P[i]) for(j = i * i; j < n; j += i) P[j] = 0;
}

int fnd(int p)
{
	int i, j;
	for(i = 0; i < p; ++i)
	{
		int b = K[1] - (ll)K[0] * i % p;
		if(b < 0) b += p;
		A[i] = b;
	}
	for(j = 2; j < n; ++j) for(i = 0; i < p; ++i) if(A[i] >= 0) if(((ll)i * K[j - 1] + A[i]) % p != K[j]) A[i] = -1;
	int res = -1;
	for(i = 0; i < p; ++i) if(A[i] >= 0)
	{
		int r = ((ll)K[n - 1] * i + A[i]) % p;
		if(res < 0) res = r;
		else if(res != r) return -2;
	}
	return res;
}

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	sieve(N);

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
		in(d, m); in(d, n);
		for(d = 1; m > 0; d *= 10, --m);
		int mx = 0;
		for(i = 0; i < n; ++i) scanf("%d", K + i), mx = max(K[i], mx);
		int res = -1;
		for(i = mx + 1; i <= d; ++i) if(P[i])
		{
			if(n == 1)
			{
				res = -2;
				break;
			}
			int r = fnd(i);
			if(r == -2)
			{
				res = -2;
				break;
			}
			if(r >= 0) if(res != -1 && res != r)
			{
				res = -2;
				break;
			}
			else res = r;
		}
		if(res == -1) printf("sdjfkedsjfls\n");
		printf("Case #%d: ", iT);
		if(res < 0) out(s, "I don't know.");
		else out(d, res);
		nl;
	}

	return 0;
}
