#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int n;scanf("%d",&n);
		int res = 0, sum = 0 , small = 987654321;
		for (int q=0;q<n;++q)
		{
			int x; scanf("%d",&x);
			res ^= x;
			sum += x;
			small = min(small,x);
		}
		printf("Case #%d: " ,kase);
		if (res) printf("NO\n");
		else     printf("%d\n",sum-small);
	}
	return 0;
}

