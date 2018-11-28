/**
 * Code Jam 2012 Problem A
 *
 * beware of pair (1212, 2121), as hinted by Case #4
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <complex>
#include <algorithm>
using namespace std;

#define MAX 2000001
//#define MAX 10000

typedef complex<int> Point;
namespace std {
	bool operator < (const Point &a, const Point &b) {
		return real(a) < real(b) || (real(a) == real(b) && imag(a) < imag(b));
	}
}

Point pool[7300000];
int n_pool;

int tens[10]; // tens[i] = 10^i
char number[20];

int main()
{
	{
		tens[0] = 1;
		for (int i=1; i<10; ++i)
			tens[i] = 10 * tens[i-1];

		Point p;

		for (int x=12, y; x<MAX; ++x) {
			sprintf(number, "%d", x);
//			printf("%d:", n);

			for (int i=1, len=strlen(number); i<len; ++i) {
				y = x / tens[i] + x % tens[i] * tens[len-i];
				if (y > x) { // we only need points with y > x
					p = Point(x, y);
					if (! n_pool || (n_pool && pool[n_pool-1] != p)) {
						// avoid adding repeated points
						pool[n_pool++] = p;
					}
				}
			}
		}
//		printf("n_pool = %d\n", n_pool); // 7299363

		sort(pool, pool+n_pool); // sort lexicographically
//		for (int p=0; p<n_pool; ++p) {
//			printf("(%d, %d)\n", real(pool[p]), imag(pool[p]));
//		}
//		return 0;
	}

	{
		int kase, serial=1, a, b, pos, soln;
		scanf("%d", &kase);
		while (kase--) {
			scanf("%d %d", &a, &b); // a < b

			// We are to count number of points inside the square bounded by (a, a) and (b, b)

			// binary search on x
			int left = 0, right = n_pool-1, mid;
			while (left <= right) {
				mid = (left + right) >> 1;
				if (a == real(pool[mid])) break;
				else if (a < real(pool[mid])) right = mid-1;
				else left = mid+1;
			}

			soln = 0;

			// the followings are stupid

//			puts("move leftward");
			pos = mid;
			while (pos >= 0 && real(pool[pos]) >= a) {
				if (imag(pool[pos]) <= b) {
//					printf("(%d, %d)\n", real(pool[pos]), imag(pool[pos]));
					++soln;
				}
				--pos;
			}

//			puts("move rightward");
			pos = mid+1;
			while (pos < n_pool && real(pool[pos]) <= b) {
				if (imag(pool[pos]) <= b) {
//					printf("(%d, %d)\n", real(pool[pos]), imag(pool[pos]));
					++soln;
				}
				++pos;
			}

			printf("Case #%d: %d\n", serial++, soln);
		}
	}

	return 0;
}
