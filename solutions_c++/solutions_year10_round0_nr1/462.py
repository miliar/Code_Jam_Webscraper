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

bool solve(int n, int k)
{
	int mask = (1 << n) - 1;
	return (k & mask) == mask;
	
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", TC, solve(n,k)?"ON":"OFF");
	}
	return 0;
}
