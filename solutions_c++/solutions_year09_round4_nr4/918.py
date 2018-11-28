#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main() {
	//ifstream in("B-large.in");
	ifstream in("D-small-attempt2.in");
	//ifstream in("D.in");
	ofstream out("D.out");

	int C;
	in >> C;

	for (int x = 0; x < C; x++) {
		int N;
		in >> N;
		int points[N][3];
		for (int i = 0; i < N; i++) {
			in >> points[i][0];
			in >> points[i][1];
			in >> points[i][2];
		}

		double dx, dy, r1, r2;
		double R1, R2, R;
		double best = 0.0;
		int p1, p2;

		if (N == 1) {
			best = points[0][2];
			char a[1000];
			sprintf(a, "Case #%d: %.6f\n", x + 1, best);
			out << a;
			continue;
		} else if (N == 2) {
			best = max(points[0][2], points[1][2]);
			char a[1000];
			sprintf(a, "Case #%d: %.6f\n", x + 1, best);
			out << a;
			continue;
		}

		int comb[3][4] = { {0, 1, 1, 2}, {0, 1, 0, 2}, {0, 2, 1, 2}};

		for (int i = 0; i < 3; i++) {
			p1 = comb[i][0], p2 = comb[i][1];
			dx = (points[p1][0] - points[p2][0]);
			dy = (points[p1][1] - points[p2][1]);
			r1 = points[p1][2];
			r2 = points[p2][2];
			R1 = (sqrt(dx * dx + dy * dy) + r1 + r2)/2.0;

			p1 = comb[i][2], p2 = comb[i][3];
			dx = (points[p1][0] - points[p2][0]);
			dy = (points[p1][1] - points[p2][1]);
			r1 = points[p1][2];
			r2 = points[p2][2];
			R2 = (sqrt(dx * dx + dy * dy) + r1 + r2)/2.0;

			if (best == 0) best = min(R1, R2);
			else best = min(best, min(R1, R2));
		}

		char a[1000];
		sprintf(a, "Case #%d: %.6f\n", x + 1, best);
		out << a;
	}

	return 0;
}
