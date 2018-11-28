#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

int par[10001];

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d: ", q);
		
		int N, L, H;
		scanf("%d%d%d", &N, &L, &H);
		
		for (int i = 0; i < N; ++i)
			scanf("%d", &par[i]);
		int res = -1;
		for (int a = L; a <= H; ++a)
		{
			bool good = true;
			for (int i = 0; i < N; ++i)
			{
				if (par[i] % a == 0 || a % par[i] == 0)
					continue;
				good = false;
				break;
			}
			if (good)
			{
				res = a;
				break;
			}
		}
		if (res != -1)
			printf("%d\n", res);
		else
			printf("NO\n");
	}
	
	return 0;
}

