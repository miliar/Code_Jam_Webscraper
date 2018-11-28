#include <stdio.h>
#include <queue>

using namespace std;

class Walkway {
	public:
		int B, E, w;
		Walkway() {}
		Walkway(int _B, int _E, int _w) : B(_B), E(_E), w(_w) {}
};

bool operator< (const Walkway & w1, const Walkway & w2) {
	if (w1.w == w2.w) {
		return w1.E - w1.B < w2.E - w2.B;
	}
	return w1.w > w2.w;
}

int main() {
	int T;
	scanf("%d", &T);

	for (int _t = 1; _t <= T; _t++) {
		priority_queue<Walkway> walkways;

		int X, S, R, t, N;
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		Walkway w[1000];

		int lastend = 0;
		for (int i = 0; i < N; i++) {
			int B, E, _w;
			scanf("%d%d%d", &B, &E, &_w);
			w[i] = Walkway(B, E, S + _w);
			walkways.push(w[i]);
			if (w[i].B > lastend) {
				walkways.push(Walkway(lastend, w[i].B, S));
			}
			lastend = E;
		}

		if (X > lastend) {
			walkways.push(Walkway(lastend, X, S));
		}

		double time = 0;
		while (!walkways.empty()) {
			Walkway walk = walkways.top();
			walkways.pop();
			if (time > t) {
				time += (double)(walk.E - walk.B) / walk.w;
			} else {
				double runtime = (double)(walk.E - walk.B) / (walk.w - S + R);
				if (time + runtime >= t) {
					double dist = ((double)t - time) * (walk.w - S + R);
					time = t;
					time += ((double)walk.E - walk.B - dist) / (walk.w);
				} else {
					time += runtime;
				}
			}
		}

		printf("Case #%d: %lf\n", _t, time);
	}

	return 0;
}
