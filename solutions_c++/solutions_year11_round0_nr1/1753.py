#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

struct ROBOT_TYPE
{
	int pos, time;
};


int main()
{
	ROBOT_TYPE r[2];
	int T, caseT, n, i, j, k;
	char str[10];

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for (caseT=1; caseT<=T; ++caseT)
	{
		scanf("%d", &n);
		int res = 0;
		r[0].pos = r[1].pos = 1;
		r[0].time = r[1].time = 0;
		while (n--)
		{
			scanf("%s%d", str, &k);
			if (str[0] == 'O') 
			{
				int tmp = abs(k-r[0].pos);
				int tmp2 = 1;
				if (r[0].time < tmp) tmp2 += tmp-r[0].time;
				res += tmp2;
				r[1].time += tmp2;
				r[0].time = 0;
				r[0].pos = k;
			}
			else
			{
				int tmp = abs(k-r[1].pos);
				int tmp2 = 1;
				if (r[1].time < tmp) tmp2 += tmp-r[1].time;
				res += tmp2;
				r[0].time += tmp2;
				r[1].time = 0;
				r[1].pos = k;
			}
		}
		printf("Case #%d: %d\n", caseT, res);

	}

	return 0;
}