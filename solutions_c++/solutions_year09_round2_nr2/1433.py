#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.txt", "w", stdout);
	char ch[100];
	int T, n;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc)
	{
		scanf("%d", &n);
		sprintf(ch, "%d", n);
		int len = strlen(ch);
		ch[len] = '0'; ch[len + 1] = 0;
		sort(ch, ch + len + 1);
		int cur = 1 << 29, t;
		do
		{
			sscanf(ch, "%d", &t);
			if(t > n && cur > t) cur = t;
		}while(next_permutation(ch, ch + len + 1));
		printf("Case #%d: %d\n", tc, cur);

	}

	return 0;

}
