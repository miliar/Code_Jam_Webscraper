#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;

int A[110];
void solve(int T)
{
	int N, S, p;
	scanf ("%d%d%d", &N, &S, &p);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%d", &A[i]);
	}
	sort(A, A + N);
	reverse(A, A + N);
	int ans = 0;
	for (int i = 0; i < N; ++i)
	{
		int v = A[i];
		if ((v + 2)/3 >= p)
		{
			++ans;
			continue;
		}
		if (v%3 == 0 || v%3 == 2)
		{
			if (v > 0 && S > 0 && (v + 2)/3 + 1 >= p)
			{
				--S;
				++ans;
			}
		}
	}
	printf("Case #%d: %d\n", T, ans);
}

int main()
{
#ifdef _DEBUG
	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		solve(i+1);
	}
	return 0;
}