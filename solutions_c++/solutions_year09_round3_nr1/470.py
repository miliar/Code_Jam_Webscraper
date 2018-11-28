#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int hash[300];
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca = 1;
	int t;
	cin >> t;
	char c[10000];
	while (t--)
	{
		memset(hash, 0, sizeof (hash));
		cin >> c;
		int len = strlen (c);
		for (int i = 0; i < len; i++)
			hash[c[i]] = -1;
		int cnt = 0;
		for (int i = 0; i < 300; i++)
		{
			if (hash[i] != 0)cnt++;
		}
		hash[c[0]] = 1;
		int now = 0;
		for (int i = 1; i < len; i++)
		{
			if (hash[c[i]] == -1)
			{
				hash[c[i]] = now;
				now++;
				if (now == 1)now++;
			}
		}
		if (cnt == 1)cnt++;
		int ans[10000];
		long long sum = 0;
		//cout << cnt << endl;
		for (int i = 0; i < len; i++)
		{
			ans[i] = hash[c[i]];
			sum = sum * cnt + ans[i];
		}
		printf ("Case #%d: %lld\n",ca++, sum);
		//cout << sum << endl;
	}
}