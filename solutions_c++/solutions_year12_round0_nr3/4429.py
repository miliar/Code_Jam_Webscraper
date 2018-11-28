#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

set<pair<int, int>> was;

void is_rec(int p, int A, int B, int maxd)
{
	int d = 10;

	while(d <= maxd)
	{
		int q = p / d + (p % d) * (maxd * 10 / d);

		int t1 = min(p, q);
		int t2 = max(p, q);

		if(p != q && q >= A && q <= B
			&& was.find(make_pair(t1, t2)) == was.end())
		{
			was.insert(make_pair(t1, t2));
		}

		d *= 10;
	}
}

int main(int argc, char **argv)
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++)
	{
		int A, B;
		int ans = 0;

		was.clear();

		scanf("%d %d", &A, &B);

		int maxd = 9;
		while(maxd < A)
		{
			maxd = maxd * 10 + 9;
		}
		maxd = (maxd + 1) / 10;

		for(int p = A; p <= B; p++)
		{
			is_rec(p, A, B, maxd);
		}

		printf("Case #%d: %d\n", i + 1, was.size());
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}