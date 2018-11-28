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

int x[4], y[4], R[4];

inline int sqr(int a) { return a * a; }

inline double dst(int i, int j)
{
	return sqrt((double)sqr(x[i]-x[j]) + (double)sqr(y[i]-y[j]));
}

inline double rad(int i, int j)
{
	return (dst(i, j) + R[i] + R[j]) / 2 >? R[3 - i - j];
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
int C;
scanf("%d", &C);
FOR(tc, 0, C)
{
	int N;
	scanf("%d", &N);
	FOR(i, 0, N)
		scanf("%d %d %d", &x[i], &y[i], &R[i]);

	double ret = 0;
	if (N == 1) ret = R[0];
	else if (N == 2) ret = R[0] >? R[1];
	else if (N == 3)
	{
		double ra = rad(0, 1), rb = rad(0, 2), rc = rad(1, 2);
		ret = ra <? rb <? rc;
	}
	printf("Case #%d: %lf\n", tc + 1, ret);
}
return 0;
}
