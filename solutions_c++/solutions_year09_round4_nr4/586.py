#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

const int INF = 1<<31;


double dist(int x1, int y1, int x2, int y2) {
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}


int main() {
	int C;
	scanf("%d", &C);

	for (int cases = 1; cases <= C; cases++) {
		int N;
		scanf("%d", &N);

		vector <double> X(N), Y(N), R(N);

		for (int i = 0; i < N; i++)
			scanf("%lf %lf %lf", &X[i], &Y[i], &R[i]);

		//small
		double minR, aux;

		if (N == 1)
			minR = R[0];

		else if (N == 2) {
			if (R[1] > R[0]) minR = R[1];
			else minR = R[0];
		}

		else if (N == 3) {
			minR = (dist(X[0], Y[0], X[1], Y[1]) + R[0] + R[1]) / 2, aux;
			if (R[2] > minR) minR = R[2];

			aux = (dist(X[0], Y[0], X[2], Y[2]) + R[0] + R[2]) / 2;
			if (R[1] > aux) aux = R[1];
			if (aux < minR) minR = aux;

			aux = (dist(X[1], Y[1], X[2], Y[2]) + R[1] + R[2]) / 2;
			if (R[0] > aux) aux = R[0];
			if (aux < minR) minR = aux;
		}

		printf("Case #%d: %lf\n", cases, minR);
	}

	return 0;
}
