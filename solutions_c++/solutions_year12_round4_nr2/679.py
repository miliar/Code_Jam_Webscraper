#include <fstream>
#include <cstdio>
#include <iomanip>

using namespace std;

ifstream in("test.txt");
FILE *out = fopen("answer.txt", "w");

int r[1000];
float x[1000];
float y[1000];

float dist(float x1, float y1, float x2, float y2) {
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

void find(float tX, float tY, int &count) {
	bool find = true;
	for (int i = 0; i < count; i++)
		if (dist(x[i], y[i], tX, tY) < r[i] + r[count] - 0.0001)
			find = false;
	if (find) {
		x[count] = tX;
		y[count] = tY;
		count++;
	}
}

const int DIV = 1000;
const int T = 1000000;
void doit(int t) {
	int N, W, L;
	in >> N >> W >> L;
	for (int i = 0; i < N; i++) {
		in >> r[i];
	}
	x[0] = 0.0f;
	y[0] = 0.0f;
	int count = 1;
	if (count < N)
		find(W, 0, count);
	if (count < N)
		find(0, L, count);
	if (count < N)
		find(W, L, count);
	for (int i = 0; i < DIV; i++)
		if (count < N)
			find(W / DIV * i, 0, count);
	for (int i = 0; i < DIV; i++)
		if (count < N)
			find(0, L / DIV * i, count);
	for (int i = 0; i < DIV; i++)
		if (count < N)
			find(W, L / DIV * i, count);
	for (int i = 0; i < 1000; i++)
		if (count < N)
			find(W / DIV * i, L, count);
	int time = 0;
	while (count < N && time < T) {
		++time;
		find((float)rand()/RAND_MAX*W, (float)rand()/RAND_MAX*L, count);
	}
	if (count == N) {
		fprintf(out, "Case #%d:", t);
		for (int i = 0; i < N; i++)
			fprintf(out, " %.6f %.6f", x[i], y[i]);
		fprintf(out, "\n");
	} else 
		fprintf(out, "PAPAPAPA!");
}

int main() {
	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
		doit(t);
	return 0;
}