#include <vector>
#include <list>
#include <map>
#include <set>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define Long long long

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("data.out", "w", stdout);

	int T, R, k, N;
	int g[1024];
	
	scanf("%d", &T);
	
	for (int x = 1; x <= T; x++)
	{
		scanf("%d %d %d", &R, &k, &N);
		
		for (int i=0; i<N; i++)
			scanf("%d", g+i);
		
		Long sum = 0;
		for (int i=0; i<N; i++)
			sum += g[i];
			
		Long cash = 0;
		int ptr = 0;
		
		if (sum <= k) cash = sum*R;
		else 
			for (int i=0; i<R; i++)
			{
				int have = 0;
				while (have + g[ptr] <= k)
				{
					have += g[ptr++];
					ptr %= N;
				}
		
				cash += have;
			}
		
		printf("Case #%d: %lld\n", x, cash);
	}
}