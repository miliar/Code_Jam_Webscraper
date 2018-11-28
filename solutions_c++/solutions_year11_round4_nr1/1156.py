
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;

inline int nextInt() {
	int x; scanf("%d", &x); return x;
}

struct cmp {
	inline bool operator() (const pair<int, int> &lhs, const pair<int, int> &rhs) {
		return lhs.second < rhs.second;
	}
};

int main() {
	int testcasesCount = nextInt();
	for (int test = 0; test < testcasesCount; ++test) {
		int corridorLength = nextInt();
		int walkingSpeed = nextInt();
		int runningSpeed = nextInt();
		int runningTime = nextInt();
		int walkwaysCount = nextInt();
		vector<pair<int, int> > segments;
		int previousEnd = 0;
		for (int i = 0; i < walkwaysCount; ++i) {
			int begin = nextInt();
			int end = nextInt();
			int plusSpeed = nextInt();
			if (previousEnd < begin) {
				segments.push_back(make_pair(begin - previousEnd, walkingSpeed));
			}
			segments.push_back(make_pair(end - begin, walkingSpeed + plusSpeed));
			previousEnd = end;
		}
		if (previousEnd < corridorLength) {
			segments.push_back(make_pair(corridorLength - previousEnd, walkingSpeed));
		}
		sort(segments.begin(), segments.end(), cmp());
		double runningTimeLeft = (double)runningTime;
		int plusSpeed = runningSpeed - walkingSpeed;
		if (plusSpeed < 0)
			plusSpeed = 0;
		double res = 0.0;
		for (int i = 0; i < (int)segments.size(); ++i) {
			double mayRunFor = (double) segments[i].first / ((double) segments[i].second + plusSpeed);
			if (mayRunFor > runningTimeLeft) {
				mayRunFor = runningTimeLeft;
			}
			runningTimeLeft -= mayRunFor;
			res += mayRunFor + (double) (segments[i].first - mayRunFor * (segments[i].second + plusSpeed)) / segments[i].second;
		}
		printf("Case #%d: %.6lf\n", test + 1, res);
	}
	return 0;
}