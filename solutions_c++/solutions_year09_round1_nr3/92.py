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

long double B[50][50];
int N, C;
long double F[50];

int main()
{
	B[0][0] = 1.0;
	for (int r = 1; r < 50; ++r) {
		B[r][0] = 1.0;
		for (int c = 1; c <= r; ++c) {
			B[r][c] = B[r-1][c-1] + B[r-1][c];
		}
	}
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d %d", &C, &N);
		for (int k = 1; k <= C; ++k) {
			double sum = B[C-k][N];
			for (int i = 1; i <= min(N, k); ++i)
				sum += B[k][i] * B[C-k][N-i] * (F[k-i] + 1.0);
			assert(B[C-k][N] < B[C][N]);
			F[k] = sum / (B[C][N] - B[C-k][N]);
		}
		printf("Case #%d: %0.7Lf\n", TC, F[C]);
	}
	return 0;
}
