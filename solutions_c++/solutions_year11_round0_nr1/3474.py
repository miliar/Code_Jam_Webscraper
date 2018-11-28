#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

#define LOCAL

int main()
{
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int T, N;
	scanf("%d", &T);
	
	for(int k  = 1; k <= T; k++)
	{
		scanf("%d", &N);
		int P[2] = {0, 0}, L[2] = {1, 1};
		for(int i = 0; i < N; i++)
		{
			char name[10];
			int val, pos;

			scanf("%s%d", name, &pos);
			
			if(name[0] == 'O')
			{
				val = max(P[0] + abs(L[0] - pos), P[1]) + 1;
				P[0] = val;
				L[0] = pos;
			}
			else
			{
				val = max(P[1] + abs(L[1] - pos), P[0]) + 1;
				P[1] = val;
				L[1] = pos;
			}
		}
		printf("Case #%d: %d\n", k, max(P[0], P[1]));
	}
	return 0;
}