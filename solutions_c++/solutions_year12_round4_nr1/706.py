#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>

using namespace std;

typedef long long int LL;
typedef pair<int,int> pii;

#define F first
#define S second
#define pb push_back
#define mp make_pair


int main (void)
{
	int T;

	scanf("%d", &T);


	LL vinex[10001];
	LL viner[10001];
	LL reach[10001];

	for(int t = 0; t < T; t++) 
	{
		printf("Case #%d: ", t+1);


		memset(reach, -1, sizeof reach);

		int n;
		LL d;

		scanf("%d", &n);

		for(int i = 0; i < n; i++) 
			scanf("%lld %lld", &vinex[i], &viner[i]);

		scanf("%lld", &d);
		
		reach[0] = min(viner[0], vinex[0]);
		int can = 0;
		
		for(int i = 0; !can && i < n; i++) {
		
			if(reach[i] == -1) continue;
		
			;
			LL rr = min(reach[i], viner[i]);

			for(int j = i+1; j < n; j++) {
					
				if(vinex[i] + rr >= vinex[j]) {
					reach[j] = max(reach[j], vinex[j] - vinex[i]);
				}
			}

			if(vinex[i] + rr >= d) can = 1;
		}

		if(can) printf("YES\n");
		else printf("NO\n");

	}

	return 0;
}
