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

int N;
int C[1010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d", &N);
		int xorsum = 0;
		int addsum = 0;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &C[i]);
			xorsum ^= C[i];
			addsum += C[i];
		}
		printf("Case #%d: ", TC);
		sort(C, C+N);
		if (xorsum == 0) printf("%d\n", addsum - C[0]);
		else puts("NO");
	}
	return 0;
}
