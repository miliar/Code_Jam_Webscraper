#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;

int L[1010];
int P[1010];
int V[1010];
int cmp(int a, int b)
{
	if (L[a]*P[a] == L[b]*P[b])
		return a < b;
	return (L[a]*P[a] > L[b]*P[b]);
}
void solve()
{
	int N;
	scanf ("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%d", &L[i]);
	}
	for (int i =0 ; i < N; ++i)
	{
		scanf ("%d", &P[i]);
		V[i] = i;
	}
	sort(V, V + N, cmp);
	for (int i = 0; i < N; ++i)
	{
		printf("%d ", V[i]);
	}
	puts("");
}
int main()
{
	freopen("Atest.txt", "r", stdin);
	freopen("Aout.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		fprintf(stderr, "%d/%d\n", i+1, T);
		solve();
	}
	return 0;
}