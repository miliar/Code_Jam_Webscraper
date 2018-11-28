#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <deque>
#include <string>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#define eps 1e-11
using namespace std;
void solve(vector<int> &v, vector<int> &a)
{
	a.assign(v.size(), 0);
	vector<bool> used(v.size(), 0);
	for (int i=0, l, j; i<v.size(); i++)
		if (!used[i])
		{
			for (l=0, j=i; !used[j]; used[j]=1, j=v[j], l++); a[l-1]++;
		}
}
int n, t, r; vector<int> in, q;
int main()
{
	scanf("%d", &t);
	for (int T=0; T<t; T++)
	{
		scanf("%d", &n);
		in.resize(n); for (int i=0; i<n; i++) scanf("%d", &in[i]), in[i]--;
		solve(in, q); r=0;
		for (int i=1; i<n; i++) r+=q[i]*(i+1);
		printf("Case #%d: %d.000000\n", T+1, r);
	}
	return 0;
}
