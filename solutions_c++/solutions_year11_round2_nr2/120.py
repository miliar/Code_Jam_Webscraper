#include <cstdio>

#include <algorithm>
#include <vector>

using namespace std;

typedef pair<__int64, int> TPoint;
typedef vector<TPoint> TPoints;

bool CanSolve(const TPoints& points, __int64 time, __int64 d) {
	__int64 min = -123456789012345678LL;
	for (size_t i = 0; i < points.size(); ++i) {
		__int64 lower = 2*points[i].first - time;
		__int64 upper = 2*points[i].first + time;
		__int64 lBound = max(lower, min);
		__int64 uBound = 2*d*(points[i].second - 1) + lBound;
		if (uBound > upper)
			return false;
		min = uBound + 2*d;
	}
	return true;
}

int main() {
	// freopen("input.txt", "r", stdin);
	
	// freopen("B-small-attempt0.in", "r", stdin);
	// freopen("B-small-attempt0.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (size_t iTest = 0; iTest < t; ++iTest) {
		int c;
		__int64 d;
		scanf("%d %I64d", &c, &d);
		TPoints points(c);
		for (size_t i = 0; i < c; ++i)
			scanf("%I64d %d", &(points[i].first), &(points[i].second));
		__int64 lBound = 0;
		__int64 uBound = 123456789012345678LL;
		while (uBound - lBound > 1) {
			__int64 mid = (uBound + lBound)/2;
			if (CanSolve(points, mid, d))
				uBound = mid;
			else
				lBound = mid;
		}
		while (!CanSolve(points, lBound, d))
			++lBound;
		printf("Case #%d: %lf\n", iTest + 1, double(lBound)/2);
	}

	return 0;
}