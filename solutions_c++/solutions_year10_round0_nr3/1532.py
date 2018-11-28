#include <stdio.h>
#include <vector>
#include <string>
#define maxn 1024
using namespace std;

struct ride{
	int earn;
	int firstGroup;
};
vector<ride> rides;

int T, t = 1;
int R, k, N, gi[maxn];
bool used[maxn];

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	for(scanf("%d", &T); T; --T, ++t)
	{
		int i, j, start, cyclen ;
		__int64 ans = 0, cycearn;
		ride cur;

		scanf("%d%d%d", &R, &k, &N);
		for(i = 0; i < N; ++i)
			scanf("%d", gi + i);
		
		rides.clear();
		memset(used, 0, sizeof(used));
		for(i = 0, j = 0; i < R && !used[j]; ++i)
		{
			start = j;
			used[start] = true;
			cur.earn = 0;
			cur.firstGroup = j;
			
			while(true)
			{
				if(cur.earn + gi[j] <= k)
					cur.earn += gi[j];
				else
					break;

				j = (j + 1) % N;
				if(j == start)
					break;
			}
			rides.push_back(cur);
		}
		if(i == R)
		{
			for(i = 0; i < rides.size(); ++i)
				ans += rides[i].earn;
			printf("Case #%d: %I64d\n", t, ans);
		}else
		{
			for(i = 0, start = j; i < rides.size() && rides[i].firstGroup != start; ++i)
				ans += rides[i].earn;
			R -= i;
			cyclen = rides.size() - i;
			cycearn = 0;

			for(j = 0; i < rides.size(); ++i, ++j)
			{
				cycearn += rides[i].earn;
				if(j < R % cyclen)
					ans += rides[i].earn;
			}
			ans += cycearn * (R / cyclen);
			printf("Case #%d: %I64d\n", t, ans);
		}
	}
}