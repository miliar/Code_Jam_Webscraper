#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#define LL long long
#define ldb long double
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define addEdge(a, b) next[edges] = first[a]; first[a] = edges; end[edges] = a;
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb eps = 1e-9;
const ldb pi = fabsl(atan2(0.0, -1.0));
const LL LINF = 1ll << 60;
const ldb LDINF = 1e42;
const int INF = 0x7f7f7f7f;
using namespace std;
#define problem "b"

LL a[1000010];
int L, N, C;
LL t;
LL x[1000010];
LL all[1000010];
int sz;

void Load()
{
	cin >> L >> t >> N >> C;
	for (int i = 0; i < C; i++)
	{
		scanf("%I64d", &a[i]);
	}
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	int i;
	sz = 0;
	x[0] = 0;
	for (i = 1; i <= N; i++)
	{
		x[i] = x[i - 1] + a[(i - 1) % C];
		if (x[i] >= t / 2ll)
		{
			all[sz++] = min(x[i] - t / 2ll, x[i] - x[i - 1]);
		}
	}
	LL res = x[N] * 2ll;
	sort(all, all + sz);
	reverse(all, all + sz);
	for (int i = 0; i < sz && i < L; i++)
	{
		res -= all[i];
	}
	cout << res << "\n";
}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		Load();
		Solve(i + 1);
	}
	return 0;
}

