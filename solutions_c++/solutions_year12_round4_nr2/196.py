#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>

const int MAX_N = 1005;
bool troll = true;
struct Circle {
	int r, index;
	double x, y;
	bool operator<(const Circle& c) const {
		if (troll) return r > c.r;
		return index < c.index;
	}
} circles[MAX_N], output[MAX_N];
int N, T, W, H;

Circle raise(int cind) {
	Circle c = output[cind];
	for (int i = 0; i < cind; ++i) {
		if (fabs(c.x-output[i].x) < c.r+output[i].r)
			c.y = std::max(c.y, output[i].y+c.r+output[i].r);
	}
	return c;
}

bool pack() {
	output[0] = circles[0];
	output[0].x = output[0].y = 0.0;
	int i = 1;
	for (; i < N; ++i) {
		output[i] = circles[i];
		double prevx = output[i-1].x, prevr = output[i-1].r;
		if (prevx+prevr+output[i].r > W) break;
		output[i].x = prevx+prevr+output[i].r;
		output[i].y = 0.0;
	}
	while (1) {
		if (i == N) break;
		output[i] = circles[i];
		output[i].x = W;
		output[i].y = 0;
		output[i] = raise(i);
		if (output[i].y > H) {return false;}
		i++;		
		for (; i < N; ++i) {
			output[i] = circles[i];
			double prevx = output[i-1].x, prevr = output[i-1].r;
			if (prevx-prevr-output[i].r < 0) break;
			output[i].x = prevx-prevr-output[i].r;
			output[i].y = 0;
			output[i] = raise(i);
			if (output[i].y > H) { return false;}
		}
	}
	return true;
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d %d", &N, &W, &H);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &circles[i].r);
			circles[i].x = circles[i].y = -1.0;
			circles[i].index = i;
		}
		troll = true;
		std::sort(circles, circles+N);
		while (1) {
			if (pack()) break;
			std::swap(circles[rand()%N], circles[rand()%N]);
		}
		troll = false;
		std::sort(output, output+N);
		printf("Case #%d:", t);
		for (int i = 0; i < N; ++i) {
			printf(" %lf %lf", output[i].x, output[i].y);
		}
		printf("\n");
	}
}