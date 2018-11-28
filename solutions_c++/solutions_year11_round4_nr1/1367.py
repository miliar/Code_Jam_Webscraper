#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

int x, s, r, n;
double t;

struct step {
	double d, s; //distance, speed
};

bool operator<(step a, step b) {
	return a.s > b.s;
}

void proc() {
	scanf("%d %d %d %lf %d", &x, &s, &r, &t, &n);
	priority_queue<step> st;
	double usualTime = x / (double)s;
	double walkingDistance = x;
	for (int i = 0; i < n; i++) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		int d = b - a;
		usualTime -= d / (double)s;
		walkingDistance -= d;
		usualTime += d / (double)(s + c);
		st.push((step){d, c + s});
	}
	st.push((step){walkingDistance, s});

	while (!st.empty() && t > 1e-10) {
		step ts = st.top();
		st.pop();
		double runningSpeed = ts.s - s + r;
		double timeUsable = min((double)t, ts.d / runningSpeed);
		t -= timeUsable;
		double distanceRan = timeUsable * runningSpeed;
		double timeSaved = (distanceRan / ts.s) - distanceRan / runningSpeed;
		usualTime -= timeSaved;
	}

	printf("%.9lf", usualTime);
	return;
}

int main() {
	int c;
	scanf("%d", &c);
	for (int i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		proc();
		printf("\n");
	}
	return 0;
}
