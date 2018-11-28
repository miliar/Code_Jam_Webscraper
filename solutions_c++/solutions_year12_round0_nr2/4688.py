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

int pr(int x)
{
	return (x != 0);
};

int d(int x)
{
	return (x / 3 + pr(x % 3));
};

int s[1000];

int main()
{
	int T;
	scanf("%d",&T);	
	for (int T_t = 1; T_t <= T; T_t++)
	{
		printf("Case #%d: ",T_t);

		int n,p,k;

		scanf("%d%d%d",&n,&p,&k);

		for (int i = 0; i < n; i++)
			scanf("%d",&s[i]);
		
		int kp = 0,ans = 0;
		for (int i = 0; i < n; i++)
		{           
			int ts = d(s[i]);
			if (ts >= k) { ans++; continue; }
			if (kp == p) continue;
			if (s[i] < 2 || s[i] > 28 || (s[i] % 3 == 1)) continue;
			if (ts + 1 >= k) { kp++; ans++; }
		}
		printf("%d\n",ans);
	}
	return 0;	
}
