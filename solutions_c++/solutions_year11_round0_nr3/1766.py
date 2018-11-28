#pragma comment(linker, "/STACK:10000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
#include <string>
#include <cstring>
#define ldb long double
#define LL long long
#define fi first
#define se second
#define fill(a, c) memset(a, c, sizeof(a))
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define getBit(mask, k) (((mask) / pw[k]) % pw[1])
#define setBit(mask, k, l) (((mask) / pw[k + 1] * pw[1] + (l)) * pw[k] + ((mask) % pw[k]))
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 1 << 30;
const ldb pi = fabsl(atan2(0.0, -1.0));
using namespace std;

int n;

int a[10010];

void Load()
{
	cin >> n;
	int i;
	for (i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	int sum = 0;
	int i;
	for (i = 0; i < n; i++)
		sum ^= a[i];
	if (sum != 0) 
	{
		cout << "NO\n";
		return;
	}
	sort(a, a + n);
	sum = 0;
	for (i = 1; i < n; i++)
	{
		sum += a[i];
	}
	cout << sum << "\n";
}

#define file "c"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}
