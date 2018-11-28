#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>



using namespace std;


struct Circle {
	double x,y;
	double r;
};

bool is_inside(Circle in,Circle out) {
	return hypot(in.x - out.x,in.y - out.y) < out.r - in.r;
}

Circle create(Circle a, Circle b) {
	Circle c;

}

double min_circle(Circle a,Circle b) {
	return (hypot(a.x-b.x,a.y-b.y) + a.r + b.r) / 2.0;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1;t <= T;t++) {
		int n;
		cin >> n;
		vector<Circle> circles(n);
		for (int i = 0;i < n;i++) {
			int x,y,r;
			cin >> x >> y >> r;
			circles[i].x = x;
			circles[i].y = y;
			circles[i].r = r;
		}
		//small case
		if (n == 1) {
			cout << "Case #" << t << ": " << circles[0].r << endl;
			continue;
		}
		if (n == 2) {
			cout << "Case #" << t << ": " << max(circles[0].r,circles[1].r) << endl;
			continue;
		}
		double minr = 1e30;
		minr = min(minr,max(min_circle(circles[0],circles[1]),circles[2].r));
		minr = min(minr,max(min_circle(circles[1],circles[2]),circles[0].r));
		minr = min(minr,max(min_circle(circles[2],circles[0]),circles[1].r));
		cout << "Case #" << t << ": " << minr << endl;
	}

}
