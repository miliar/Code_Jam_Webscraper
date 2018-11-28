#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int n;
pair<int , int> list[1002];
int main()
{
	int t;
	int cas = 0;
	int p;
	int tt;
	for(scanf("%d",&t) ; t-- ; )
	{
		scanf("%d",&n);
		for(int i = 1 ; i <= n ; i++)
			scanf("%d%d",&list[i].first , &list[i].second);
		std::sort( list+1 , list  + n + 1);
		list[n+1].second = -1;
		list[0].second = -1;
		int ans = 1;

		p = 0;
		tt = 0;
		for(int i = 1 ; i <= n + 1 ; i++)
		{
			if(list[i].second > list[i-1].second)
			{
				++p;
			}else
			{
				ans *= p;
				p = 1;
				tt++;
			}
		}
		if(tt == 1) ans = 0;
		printf("Case #%d: %d\n",++cas,ans);

	}
	return 0;
}
