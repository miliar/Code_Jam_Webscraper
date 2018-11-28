#include <cstdio>
#include <algorithm>
#include <vector>
#include <memory>
#include <iostream>

using namespace std;

int let[1100];
long long k[1100];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		int P,K,L;
		scanf("%d%d%d", &P, &K, &L);
		for (int i=0; i<L; i++)
		{
			scanf("%d", &let[i]);
		}
		memset(k,0,sizeof(k));
		sort(let,let+L);
		long long res = 0;
		int index = 0;
		for (int i=L-1; i>=0; i--)
		{
			k[index]++;
			res += k[index]*let[i];
			index++;
			if (index >= K)
				index = 0;
		}
		printf("Case #%d: %lld\n", tt, res);
	}
	return 0;
}