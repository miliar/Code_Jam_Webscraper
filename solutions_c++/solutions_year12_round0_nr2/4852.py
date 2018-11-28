#include <cstdio>
using namespace std;

int N, S, p;

int main()
{
	int Z;
	scanf("%d", &Z);
	for(int t = 1; t <= Z; ++t)
	{
		int res = 0;
		scanf("%d %d %d", &N, &S, &p);
		for(int i = 0; i < N; ++i)
		{
			int t;
			scanf("%d", &t);
			
			int d = t / 3, r = t % 3;
			if(d + (r > 0) >= p) ++res;
			else if(d + r >= p && S) ++res, --S;
			else if(d + (d > 0) >= p && S) ++res, --S;
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
