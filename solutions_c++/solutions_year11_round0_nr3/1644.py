#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%d", &T);
	int cas = 0;
	for(cas = 1; cas <= T; cas++)
	{
		int N;
		scanf("%d", &N);
		int i;
		vector <int> a(N);
		for(i = 0; i < N; i++)
			scanf("%d", &a[i]);
		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());
		int tot = 0;
		long long sum = 0;
		for(i = 0; i < a.size(); i++)
		{
			tot = tot ^ a[i];
			sum += a[i];
		}
		if(tot == 0)
		{
			printf("Case #%d: %lld\n", cas, sum - a[a.size() - 1]);
		}
		else
		{
			printf("Case #%d: NO\n", cas);
		}
	}
	return 0;
}
