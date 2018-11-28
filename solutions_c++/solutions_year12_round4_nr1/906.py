#include <iomanip>
#include <algorithm>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

using namespace std;

int d[10100];
int l[10100];
int was[10100];

int main()
{
	int T;
	scanf("%d",&T);	
	for (int T_t = 1; T_t <= T; T_t++)
	{
		printf("Case #%d: ",T_t);

		int n;
		scanf("%d",&n);

		for (int i = 0; i < n; i++)
		{
			scanf("%d%d",&d[i],&l[i]);
			was[i] = 0;
		}
		int L;
		scanf("%d",&L);

		was[0] = min(d[0],l[0]);
		bool f = false;
		
		for (int i = 0; i < n; i++)
		{
			if (was[i] == 0) continue;
			if (d[i] + was[i] >= L) { f = true; break; }
			int j = i+1;
			while (j < n)
			{
				if (d[j] - d[i] <= was[i]) was[j] = max(was[j], min(d[j]-d[i],l[j]) );
				j++;
			}
		}
		if (f) printf("YES\n");
		else printf("NO\n");
	}

	return 0;	
}
