#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;

#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

int X[100];
int Y[100];
int R[100];

double dist(double x, double y, double xx, double yy)
{
	return sqrt((x-xx)*(double)(x-xx) + (y-yy)*(double)(y-yy));
}

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t <T; ++t)
	{
		int N;
		scanf("%d", &N);
		int i;
		for (i = 0; i < N; ++i)
			scanf("%d%d%d", &X[i], &Y[i], &R[i]);
		double res;
		if (N == 1)
		{
			res = R[0];
		}
		else if (N == 2)
		{
			res = max(R[0], R[1]);
		}
		else
		{
			res = max((double)R[0], (R[1]+R[2]+dist(X[1], Y[1], X[2], Y[2]))/2.0);
			res = min(res, max((double)R[1], (R[0]+R[2]+dist(X[0], Y[0], X[2], Y[2]))/2.0));
			res = min(res, max((double)R[2], (R[0]+R[1]+dist(X[0], Y[0], X[1], Y[1]))/2.0));
		}
		printf("Case #%d: %.9lf\n", t+1, res);
	}


	return 0;
}