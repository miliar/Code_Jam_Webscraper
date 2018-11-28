#include <cstdio>

using namespace std;

long long abs(long long a)
{
	if (a<0) return -a;
	else return a;
}

long long area(long long x1, long long y1,
			   long long x2, long long y2,
			   long long x3, long long y3)
{
	return abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3);
}

int main()
{
	int C;
	scanf("%d",&C);
	for (int i=1;i<=C;i++)
	{
		long long N,M,A;
		scanf("%lld %lld %lld",&N,&M,&A);
		long long y1 = 0;
		long long x2 = 0;
		long long x1 = -1;
		long long y2 = -1;
		long long x3 = -1;
		long long y3 = -1;

 		bool need_break = false;
		for (x1 = 0;x1<=N;x1++)
		{
			for (y2 = 0;y2<=M;y2++)
			{
				for (x3 = 0;x3<=N;x3++)
				{
					for (y3 = 0;y3<=M;y3++)
					{
						if (area(x1,y1,x2,y2,x3,y3) == A) need_break = true;
						if (need_break) break;
					}
					if (need_break) break;
				}
				if (need_break) break;
			}
			if (need_break) break;
		}
		if (need_break)
		{
			printf("Case #%d: %lld %lld %lld %lld %lld %lld\n",i,x1,y1,x2,y2,x3,y3);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",i);
		}
	}
	return 0;
}