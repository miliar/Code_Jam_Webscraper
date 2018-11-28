#include <functional> 
#include <algorithm> 
#include <iostream> 
#include <complex> 
#include <cstring> 
#include <numeric> 
#include <sstream> 
#include <limits> 
#include <string> 
#include <vector> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <set> 
using namespace std; 

template <class T, bool B> struct cmp_ { inline static bool cmp(T a, T b) { return a < b; } };  
template <class T> struct cmp_<T, false> { inline static bool cmp(T a, T b) { return a != b; } };  
#define FOR(i, b, e) for (typeof(b) i = (b); cmp_< typeof(b), numeric_limits< typeof(b) >::is_specialized >::cmp(i, e); ++i)

#define MAXN 50

// ADJACENT :(

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
int T;
scanf("%d", &T);
FOR(tc, 0, T)
{
	int m[MAXN][MAXN];
	int rp[MAXN];
	char c;
	int N;

	scanf("%d", &N);
	FOR(i, 0, N)
	{
		getchar();
		rp[i] = 0;
		FOR(j, 0, N)
		{
			scanf("%c", &c);
			m[i][j] = c - '0';
			if (m[i][j]) rp[i] = j;
		}
	}

	int nSwaps = 0;

	FOR(i, 0, N - 1)
	{
		if (rp[i] > i)
			FOR(j, i + 1, N)
				if (rp[j] <= i)
				{
					for (int k = j - 1; k >= i; --k)
					{
						swap(rp[k], rp[k+1]);
						++nSwaps;
					}
					break;
				}
	}

	printf("Case #%d: %d\n", tc + 1, nSwaps);
}

	return 0;
}
