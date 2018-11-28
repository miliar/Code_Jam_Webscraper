#include <stdio.h>
#include <vector>

using namespace std;

typedef pair<int, int> Point;
//typedef pair<Point, bool> Entry;

int main(int argc, char** argv) {

	int numCases;

	freopen("C:\\input.txt", "r", stdin);
	freopen("C:\\output.txt", "wt", stdout);

	/* first token is number of test cases */
	scanf("%d", &numCases);

	for (int loop = 0; loop < numCases; loop++) {

		int numTrees, _A, _B, _C, _D, _X0, _Y0, _M;
		
		scanf("%d %d %d %d %d %d %d %d", &numTrees, &_A, &_B, &_C, &_D, &_X0, &_Y0, &_M);

		vector<Point> points;
		__int64 A = _A;
		__int64 B = _B;
		__int64 C = _C;
		__int64 D = _D;
		__int64 M = _M;
		__int64 X = _X0;
		__int64 Y = _Y0;
		points.push_back(Point(X, Y));
		/* generate all points and store */
		for (int loop5 = 1; loop5 < numTrees; loop5++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			points.push_back(Point(X, Y));
		}

		int count = 0;
		int test = points.size();
		for (int loop4 = 0; loop4 < points.size(); loop4++) {
			Point point1 = points[loop4];
			for (int loop2 = loop4 + 1; loop2 < points.size(); loop2++) {
				Point point2 = points[loop2];
				for (int loop3 = loop2 + 1; loop3 < points.size(); loop3++) {
					Point point3 = points[loop3];
					if (0 != (point1.first + point2.first + point3.first) % 3) continue;
					if (0 != (point1.second + point2.second + point3.second) % 3) continue;
					count++;
				}
			}
		}

		printf("Case #%d: %d\n", loop + 1, count);
	}

	return 0;
}