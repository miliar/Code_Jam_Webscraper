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

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		LL N, PD, PG;
		scanf("%lld %lld %lld", &N, &PD, &PG);
		printf("Case #%d: ", TC);
		if (PD > 0 && PG == 0) puts("Broken");
		else if (PD < 100 && PG == 100) puts("Broken");
		else {
			LL g = __gcd(PD, 100LL);
			LL pd = 100 / g;
			if (pd > N) puts("Broken");
			else puts("Possible");
		}
	}
	return 0;
}
