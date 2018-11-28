#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

const int MAX = 1009;

int v[MAX], N;

int main()
{
	freopen("C_small.in", "r", stdin);
	freopen("C_small.out", "w", stdout);
	
	int T; cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> N;
		for(int i = 0; i < N; i++)  cin >> v[i];
		
		int ans = -1;
		for(int i = 1; i < (1 << N)-1; i++)
		{
			int a = 0, b = 0;
			int s1 = 0, s2 = 0;			
			for(int k = 0; k < N; k++)
			{
				if(i & (1<<k)){  a ^= v[k];  s1 += v[k]; }
				else { b ^= v[k];	s2 += v[k]; }
			}		
			if(a == b)  ans = max(ans, max(s1, s2)); 
		}	
		printf("Case #%d: ", t);
		if(ans == -1) puts("NO");
		else printf("%d\n", ans);
	}	
		
	return 0;
}
