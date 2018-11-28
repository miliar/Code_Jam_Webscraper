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

int K;
string S;
string R;
int perm[10];

void apply()
{
	R = S;
	for (int i = 0; i < SZ(S); i += K) {
		for (int j = 0; j < K; ++j)
			R[i+j] = S[i+perm[j]];
	}
}

int cnt()
{
	int c = 1;
	for (int i = 1; i < SZ(R); ++i)
		if (R[i-1] != R[i])
			c += 1;
	return c;
}

int main()
{
	int T;
	scanf("%d", &T);
	char buf[1024];
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &K);
		scanf("%s", buf);
		S = buf;
		for (int i = 0; i < K; ++i)
			perm[i] = i;
		int mn = 123456;
		do {
			apply();
			min2(mn, cnt());
			//printf("%d => %s\n", cnt(), R.c_str());
		} while (next_permutation(perm,perm+K));
		printf("Case #%d: %d\n", tt, mn);
	}

	return 0;
}
