#include <cstdio>
#include <algorithm>

using namespace std;

double addS[1010];
double length[1010];

double S, R, T, X;
int N;

void Open() {
	freopen ("P1.in", "r", stdin);
	freopen ("P1.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void init() {
	scanf ("%lf %lf %lf %lf", &X, &S, &R, &T);
	scanf ("%d", &N);
	double tmp = X;
	for (int i = 0; i < N; i++) {
		double ts, te;
		scanf ("%lf %lf %lf", &ts, &te, &addS[i]);
		length[i] = te - ts;
		tmp -= length[i];
	}
	length[N] = tmp;
	addS[N] = 0;
	N++;
}

bool comp(int a, int b) {
	return addS[a] < addS[b];
}

double work() {
	double answer = 0;
	int order[1010];
	for (int i = 0; i < N; i++) order[i] = i;
	sort(order, order + N, comp);
	for (int i = 0; i < N; i++) {
		int j = order[i];
		if (T * (R + addS[j]) < length[j]) {
			answer += T + (length[j] - (T * (R + addS[j]))) / (S + addS[j]);
			T = 0;
		} else {
			answer += length[j] / (R + addS[j]);
			T -= length[j] / (R + addS[j]);
		}
	}
	return answer;
}

void output(int caseNo, double answer) {
	printf ("Case #%d: %0.9lf\n", caseNo, answer);
}

void process() {
	int caseNum;
	scanf ("%d", &caseNum);
	for (int caseNo = 1; caseNo <= caseNum; caseNo++) {
		init();
		output(caseNo, work());
	}
}

int main() {
	Open();
	process();
	Close();
	return 0;
}