#include <iostream>
using namespace std;

int tot[128], n, s, p, T, x=1;

int solve()
{
	int ret = 0;
	for (int i=0; i<n; i++)
		if ( (tot[i] + 2)/3 >= p) ret++;
		else if ( (tot[i] + 2)/3 == p-1 && s > 0 && tot[i]%3 != 1 && tot[i]>1) ret++, s--;
	return ret;
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> T;
	while (x<=T && cin >> n >> s >> p)
	{
		for (int j=0; j<n; j++) cin >> tot[j];
		printf("Case #%d: %d\n", x++, solve());
	}
}