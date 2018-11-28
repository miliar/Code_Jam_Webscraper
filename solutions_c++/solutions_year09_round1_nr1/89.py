#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int was[1024];

int square_sum(int num, int base)
{
	int sum = 0;
	while (num != 0) {
		int d = num % base;
		num /= base;
		sum += d*d;
	}
	return sum;
}

int happy_cache[12*1024*1024];

int ishappy(int num, int base)
{
	memset(was, 0, sizeof was);
	for (int i = 0; num != 1 && was[num] == 0; ++i) {
		was[num] = 1;
		num = square_sum(num, base);
	}
	return num == 1;
}

int main()
{
	for (int j = 2; j <= 10; ++j)
		happy_cache[1] |= 1 << j;
	int maxcnt = 0;
	fprintf(stderr, "precalculating\n");
	for (int i = 2; i < 1024; ++i) {
		int cnt = 0;
		for (int j = 2; j <= 10; ++j) {
			happy_cache[i] |= ishappy(i, j) << j;
			if (happy_cache[i] & (1 << j))
				cnt += 1;
		}
		if (maxcnt < cnt) {
			maxcnt = cnt;
			fprintf(stderr, "maxcnt = %d, i = %d\n", maxcnt, i);
		}
	}
	for (int i = 1024; i < 12*1024*1024; ++i) {
		int cnt = 0;
		for (int j = 2; j <= 10; ++j) {
			happy_cache[i] |= happy_cache[square_sum(i, j)] & (1 << j);
			if (happy_cache[i] & (1 << j))
				cnt += 1;
		}
		if (maxcnt < cnt) {
			maxcnt = cnt;
			fprintf(stderr, "maxcnt = %d, i = %d\n", maxcnt, i);
		}
	}
	fprintf(stderr, "precalculation done\n");


	int T;
	char buf[1024];
	fgets(buf, 1024, stdin);
	sscanf(buf, "%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		fgets(buf, 1024, stdin);
		istringstream iss(buf);
		int bm = 0;
		int i;
		while (iss >> i)
			bm |= 1 << i;

		for (i = 2; (happy_cache[i] & bm) != bm; ++i)
			;
		printf("Case #%d: %d\n", TC, i);
	}

	return 0;
}
