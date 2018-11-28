#include <iostream>
#include <map>
#include <vector>

using namespace std;

int test;
typedef pair<int,int> pii;
#define mp make_pair

map<pii, int> memo;

int N, Q;
int a[100];

int find(int s, int f)
{
	pii p(s, f);
	if (memo.count(p)) return memo[p];
	int res = (int)1e9;
	
	for (int i = 0; i < Q; i++)
	{	
		if (a[i] >= s && a[i] <= f)
			res = min(res, f - s + find(s, a[i]-1) + find(a[i]+1, f));
	}
	
	if (res == (int)1e9) res = 0;
	
	return memo[p] = res;
}

void solve()
{
	memo.clear();
	cin >> N >> Q;
	for (int i = 0; i < Q; i++) cin >> a[i];
	int ans = find(1, N);
	cout << "Case #" << ++test << ": " << ans << endl;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
		solve();
	return 0;
}