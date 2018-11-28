#include <iomanip>
#include <algorithm>
#include <map>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#include <time.h>
#include <sys/time.h>

using namespace std;


int main()
{
//	freopen("anarc05b.in","r",stdin);
//	freopen("anarc05b.out","w",stdout);
	int t;
	scanf("%d",&t);

	for (int T = 0; T < t; T++)
	{
		int n;
		scanf("%d",&n);
		long long ans = 0;
		long long sum = 0;
		long long mx = 1001000;
		for (int i = 0; i < n; i++)
		{
			long long x;
			scanf("%I64d",&x);
			sum+=x;
			ans ^= x;
			mx = min(mx,x);
		}
		printf("Case #%d: ",T+1);
		if (ans == 0) printf("%I64d\n",sum - mx);
		else printf("NO\n");
	}
//	in.getline(s);

	return 0;	
}
