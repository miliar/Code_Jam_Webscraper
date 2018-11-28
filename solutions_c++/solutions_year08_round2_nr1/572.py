#include <iostream>
#include <vector>

struct Point {
	long long x;
	long long y;

	Point(long long xx, long long yy): x(xx), y(yy) {}
};

int main() {
	long long N;

	std::cin >> N;

	for (long long ncase = 1; ncase <= N; ++ncase) {
		std::vector<Point> points;

		long long n, A, B, C, D, x, y, M;
		std::cin >> n >> A >> B >> C >> D >> x >> y >> M;
		points.push_back(Point(x, y));

		for (long long i = 1; i < n; ++i) {
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			points.push_back(Point(x, y));
		}
#if 0
		std::cout << "Case " << ncase << std::endl;
		for (unsigned i = 0; i < points.size(); ++i) {
			std::cout << points[i].x << " " << points[i].y << std::endl;
		}
#endif
		long long answer = 0;
		for (long long i = 0; i < n; ++i) {
			for (long long j = i + 1; j < n; ++j) {
				for (long long k = j + 1; k < n; ++k) {
					if (((points[i].x + points[j].x + points[k].x) % 3 == 0) &&
					    ((points[i].y + points[j].y + points[k].y) % 3 == 0)) {
						++answer;
					}
				}
			}
		}
		std::cout << "Case #" << ncase << ": " << answer << std::endl;
	}
	
	return 0;
}
