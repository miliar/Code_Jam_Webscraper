#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <algorithm>
using namespace std;

int h[3000], x[3000];

long long ccw(long long dx1, long long dy1, long long dx2, long long dy2)
{
	return dy1 * dx2 - dx1 * dy2;
}

int main() {
	int tc, n, m;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen)
	{
		scanf("%d", &n);
		bool imposs = false;
		for (int i=0; i<n-1; i++)
		{
			scanf("%d", &h[i]);
			if (h[i] <= i+1 || h[i] > n)
				imposs = true;
		}
		x[n-1] = x[n-2] = 500000000;
		bool imposs2 = false;
		for (int i=n-3; !imposs && i>=0; --i)
		{
			int minval = -1, maxval = 1000000001;
			//printf("i = %d %d\n", i, h[i]);
			// check for impossible
			for (int j=i+1; j<n; ++j)
			{
				if (j+1 < h[i] && h[j] > h[i])
				{
					imposs2 = true;
				}
				// visibility line check
				if (j+1 < h[i])
				{
					int lo = 0, hi = 1000000001;
			//		printf("here with %d %d\n", lo, hi);
					while(lo < hi)
					{
						int mid = (lo+hi)/2;
						int dx1 = j - i;
						int dx2 = h[i]-i-1;
						int dy1 = x[j]-mid;
						int dy2 = x[h[i]-1]-mid;
				//		printf("%d %d %d %d\n", dx1, dy1, dx2, dy2);
						if (ccw(dx1, dy1, dx2, dy2) < 0)
						{
							hi = mid;
						}
						else
						{
							lo = mid + 1;
						}
					}
					int dx1 = j - i;
					int dx2 = h[i] - i - 1;
					int dy1 = x[j] - lo;
					int dy2 = x[h[i]-1]-lo;
			//		if (i == 0) printf("%d %d %d %d %lld %d\n", dx1, dy1, dx2, dy2, ccw(dx1, dy1, dx2, dy2), lo);
					if (lo > minval)
						minval = lo;
				}
				// no visibilty check
				else if (j+1 > h[i]) {
			//		printf("here2\n");
					int lo = 0, hi = 1000000001;
					int best = maxval;
					while(lo <= hi)
					{
						int mid = (lo+hi)/2;
						int dx1 = j - i;
						int dx2 = h[i]-i-1;
						int dy1 = x[j]-mid;
						int dy2 = x[h[i]-1]-mid;
						if (ccw(dx1, dy1, dx2, dy2) >= 0)
						{
							hi = mid-1;
						}
						else {
							lo = mid+1;
							best = mid;
						}
					}
					if (best < maxval)
						maxval = best;
				}
			}
			if (maxval < minval)
			{
				imposs = true;
				break;
			}
//			printf("%d %d\n", maxval, minval);
			if (maxval <= 1000000000)
				x[i] = maxval - 2;
			else
				x[i] = minval + 2;
			assert(maxval >= minval);
		}
		printf("Case #%d:", scen);
		if (imposs) {
			puts(" Impossible");
			assert(imposs2);
		}
		else {
			assert(!imposs2);
			for (int i=0; i<n; ++i) {
				assert(x[i] >= 0 && x[i] <= 1000000000);
				printf(" %d", x[i]);
			}
			puts("");
		}
	}
	return 0;
}
