// GCJ 2010 Round 1
// 3. Number Game

// May 22, 2010
// wookayin

#include <math.h>
#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

int g(int x, int y)
{
	double t = (double)y / x - (double)x / y;
	if (t<0) t*=-1;
	return (int) t;
}

const double phi = (1 + sqrt(5.0)) / 2.0;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T, tt;
	scanf("%d", &T);
	//memset(cache, -1, sizeof(cache));
	for(tt=1; tt<=T; ++tt)
	{
		int A1,A2,B1,B2;
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		
		long long ans = 0;
		for(int x=A1; x<=A2; ++x)
		{
			int y1 = x / phi;
			int y2 = x * phi;
			int y3 = 2147483640;
			int y4 = -2147483640;
			for(int y=max(y1-2, 1); y<=y1+2; ++y)
			{
				if(g(x,y) == 0) {
					y3 = min(y3, y);
					y4 = max(y4, y);
				}
			}
			for(int y=max(y2-2, 1); y<=y2+2; ++y) {
				if(g(x,y) == 0) {
					y3 = min(y3, y);
					y4 = max(y4, y);
				}
			}
			int zeros = min(y4, B2) - max(y3, B1) + 1;
			if(zeros < 0) zeros = 0;
			ans += B2 - B1 + 1 - zeros;
		}

		fprintf(stderr, "%d\n", tt);
		printf("Case #%d: %lld\n", tt, ans);
	}
	return 0;
}