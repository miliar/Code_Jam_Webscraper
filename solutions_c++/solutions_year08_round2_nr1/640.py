#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <queue>
#include <vector>
#include <stack>

using namespace std;

struct Point {
	long long x, y;
	Point(long long  _x = 0, long long _y= 0) : x(_x), y(_y) { }
};

/*
int operator<(const S &a, const S &b) {
	return 0;
}
*/

int main() {
	int N;
	int n,A,B,C,D,x0,y0,M;

	cin >> N;
	for (int casen = 0; casen<N; casen++) {
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		vector<Point> points(n);

		long long X = x0, Y = y0;
		points[0] = Point(X,Y);

		for (int i = 1; i < n; i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			points[i] = Point(X,Y);
		}
		/*
		for (int i = 0; i < points.size() ;i++) {
			cout << points[i].x<< " " << points[i].y << endl;
			}*/

		int ans = 0;
//		cout << "cal" << endl;

		for (int p1 = 0; p1 < points.size()-2; p1++) {
			for (int p2 = p1 + 1; p2 < points.size()-1; p2++) {
				for (int p3 = p2 + 1; p3 < points.size(); p3++) {
					long long centerX = (points[p1].x + points[p2].x + points[p3].x);
					long long centerY = (points[p1].y + points[p2].y + points[p3].y);

					if (abs(centerX) % 3 == 0 && abs(centerY) % 3 == 0)
						ans++;
				}
			}
		}

		cout << "Case #" << casen+1 << ": " << ans << endl;
	}

}





