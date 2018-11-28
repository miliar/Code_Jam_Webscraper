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
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int R, C;

int bitcount[2048];
char field[16][16];

bool row_ok(int row, int bm)
{
	int col = 0;
	while (bm != 0) {
		if ((bm%2==1) && field[row][col] == 'x')
			return false;
		bm /= 2;
		col += 1;
	}
	return true;
}

bool nextrow_ok(int prev, int next)
{
	int t = next;
	while (t != 0) {
		if (t%4 == 3)
			return false;
		t /= 2;
	}
	if ((prev>>1) & next)
		return false;
	if ((prev<<1) & next)
		return false;
	return true;
}

int cache[2048][16];

int max_stud(int prev_row, int row)
{
	if (row == R)
		return 0;
	int &res = cache[prev_row][row];
	if (res != -1)
		return res;
	for (int i = 0; i < (1<<C); ++i) {
		if (nextrow_ok(prev_row,i) && row_ok(row,i))
			max2(res, bitcount[i] + max_stud(i,row+1));
	}
	return res;
}

int main()
{
	for (int i = 1; i < 2048; ++i)
		bitcount[i] = bitcount[i/2] + i%2;

	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT) {
		memset(cache, -1, sizeof cache);
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; ++i)
			scanf("%s", field[i]);
		printf("Case #%d: %d\n", TT, max_stud(0,0));
	}

	return 0;
}
