#include <cstdio>

int C, T;
__int64 D;
__int64 points[210];
__int64 npoints[420];
__int64 people[210];


void Open() {
	freopen ("P2.in", "r", stdin);
	freopen ("P2.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void init() {
	scanf ("%d%I64d", &C, &D);
	for (int i = 0; i < C; i++) {
		scanf ("%I64d%I64d", &points[i], &people[i]);
	}
}

double calc() {
	__int64 total = 0;
	int count = 0;
	double answer = 0.0;
	for (int i = 0; i < C; i++) {
		if (people[i] == 1) {
			npoints[count++] = points[i] - total * D;
		} else {
			npoints[count++] = points[i] - total * D;;
			npoints[count++] = points[i] - (total + people[i] - 1) * D;
		}
		total += people[i];
	}

	while (1) {
		int minIndex = 0, maxIndex = 0;
		for (int i = 0; i < count; i++)
			points[i] = npoints[i];

		for (int i = 0; i < count; i++) {
			if (points[i] > points[maxIndex]) maxIndex = i;
			if (points[i] <= points[minIndex]) minIndex = i;
		}

		if (maxIndex <= minIndex) {
			double tanswer = ((double)(points[maxIndex] - points[minIndex])) / 2.0;
			if (tanswer > answer) answer = tanswer;
			break;
		}

		int maxBefore = 0, minAfter = count - 1;
		for (int i = 0; i < minIndex; i++)
			if (points[i] > points[maxBefore]) maxBefore = i;
		{
			double tanswer = ((double)(points[maxBefore] - points[minIndex])) / 2.0;
			if (tanswer > answer) answer = tanswer;
		}
		for (int i = maxIndex + 1; i < count; i++)
			if (points[i] < points[minAfter]) minAfter = i;
		{
			double tanswer = ((double)(points[maxIndex] - points[minAfter])) / 2.0;
			if (tanswer > answer) answer = tanswer;
		}
		
		count = 0;
		for (int i = minIndex + 1; i < maxIndex; i++) 
			npoints[count++] = points[i];
	}

	return answer;
}

void output(int caseNo, double answer) {
	printf ("Case #%d: %0.8lf\n", caseNo, answer);
}

void work() {
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		init();
		output(caseNo, calc());
	}
}

int main() {
	Open();
	work();
	Close();
	return 0;
}