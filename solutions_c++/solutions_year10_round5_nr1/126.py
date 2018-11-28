#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define  maxn 1100000

int d, k;
int a[55];
bool f[maxn];

void init()
{
	f[0] = f[1] = true;
	for (int i = 2; i < maxn; i++) if (!f[i])
	{
		for (int j = i+i; j < maxn; j += i)
			f[j] = true;
	}
}

// Calculates inverse of b modulo a (gcd(a,b) should be 1)
LL calcinv(LL a, LL b) {
  LL t = a, a1 = 1, b1 = 0, a2 = 0, b2 = 1;
  while (b) {
    a1 -= a2 * (a / b);
    b1 -= b2 * (a / b);
    a = a % b;
    swap(a, b);
    swap(a1, a2);
    swap(b1, b2);
  }
  return (b1 % t + t) % t;  
}

void solvecase() {
	scanf("%d%d", &d, &k);
	int m = 0;
	for (int i = 0; i < k; i++)
	{
		scanf("%d", &a[i]);
		m = max(m, a[i]);
	}
	int t = 1;
	for (int i = 0; i < d; i++) t *= 10;

	int res = -1;
	int cnt = 0;

	if (k == 1)
	{
		cnt = 2;
	}
	else if (k == 2)
	{
		if (a[0] == a[1])
		{
			cnt = 1;
			res = a[0];
		}
		else
		{
			cnt = 2;
		}
	}
	else
	{
		for (int p = m+1; p < t; p++) if (!f[p])
		{
			int A = (((a[2]-a[1]+p) % p) * calcinv(p, (a[1]-a[0]+p) % p)) % p;
			int B = ((a[1] - (LL)A * a[0]) % p + p) % p;
			bool ok = true;
			for (int i = 2; i < k; i++)
			{
				int t = ((LL)A * a[i-1] + B) % p;
				if (t != a[i])
				{
					ok = false;
					break;
				}
			}
			if (ok)
			{
				int t = ((LL)A * a[k-1] + B) % p;
				if (res != t)
				{
					cnt++;
					res = t;
				}
			}
		}
	}

	if (cnt > 1)
	{
		printf("I don't know.");
	}
	else
	{
		printf("%d", res);
	}
}

void solve() {
	init();
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	//freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}