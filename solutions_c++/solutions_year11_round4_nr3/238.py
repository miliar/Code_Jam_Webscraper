#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>;

using namespace std;

int T;
long long N;
int a[1000010];

void prepare()
{
	memset(a,0,sizeof(a));
	for (int i=2; i<1010; i++)
		if (a[i]==0)
		{
			int t = i;
			while (t+i<1000010)
			{
				t+=i;
				a[t] = 1;
			}
		}
}

int solve()
{
	int ret = 0;
	for (int i=2; i<1000010; i++)
		if (a[i]==0)
		{
			long long K = (long long)i*(long long)i;
			while (K<=N)
			{
				ret++;
				K*=i;
			}
		}
	return ret;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	prepare();
	for (int i=1; i<=T; i++)
	{
		cin >> N;
		int ans = solve();
		if (N>1)
			ans += 1;
		printf("Case #%d: %d\n", i, ans);
	}
}