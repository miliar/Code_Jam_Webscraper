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
double X[50], Y[50], R[50];

double sqr(double x)
{
	return x*x;
}

double dist(int i, int j)
{
	double d = sqr(X[i] - X[j]) + sqr(Y[i] - Y[j]);
	d = sqrt(d) / 2.0;
	d += (R[i] + R[j]) / 2.0;
	return d;
}

double solve3()
{
	double best = 1.0e47;
	min2(best, max(R[2], dist(0,1)));
	min2(best, max(R[1], dist(0,2)));
	min2(best, max(R[0], dist(1,2)));
	return best;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d", &N);
		assert(N <= 3);
		for (int i = 0; i < N; ++i) {
			scanf("%lf %lf %lf", &X[i], &Y[i], &R[i]);
		}
		printf("Case #%d: ", TC);
		switch (N) {
		case 1:
			printf("%0.9lf\n", R[0]);
			break;
		case 2:
			printf("%0.9lf\n", max(R[0], R[1]));
			break;
		case 3:
			printf("%0.9lf\n", solve3());
			break;
		}
	}
	return 0;
}
