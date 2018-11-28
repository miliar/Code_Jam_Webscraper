#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

int TC, N;

int X[100];
int Y[100];
double R[100];

double DIST (int _i, int _j) {
	return sqrt ((double)(X[_j]-X[_i])*(X[_j]-X[_i]) + (Y[_j]-Y[_i])*(Y[_j]-Y[_i]));
}

int main()
{
    freopen("in.in", "rt", stdin);
	//freopen("out.out", "wt", stdout);

	scanf ("%d", &TC);
	for (int tc = 0; tc < TC; tc++)
	{
		scanf ("%d", &N);
		for (int i = 0; i < N; i++)
			scanf ("%d %d %lf", X+i, Y+i, R+i);

		double ans;
		if (N == 1) ans = R[0];
		else if (N == 2) ans = max (R[0], R[1]);
		else {
			double d12 = DIST (0, 1) + R[0] + R[1];
			double d13 = DIST (0, 2) + R[0] + R[2];
			double d23 = DIST (1, 2) + R[1] + R[2];
			if (d12 < d13 && d12 < d23) {
				ans = max (R[2], d12/2);
			}
			else if (d13 < d12 && d13 < d23) {
				ans = max (R[1], d13/2);
			}
			else {
				ans = max (R[0], d23/2);
			}
		}
		printf ("Case #%d: %.6lf\n", tc+1, ans);
	}

	return 0;
}