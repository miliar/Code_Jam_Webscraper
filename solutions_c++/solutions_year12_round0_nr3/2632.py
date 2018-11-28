#include <cstdio>
#include <cmath>

int startNum, endNum;

int recycleStartFrom(int number) {
	int temp = number;
	int numDigits = 0;
	while (temp > 0) {
		numDigits++;
		temp /= 10;
	}
	int tryNum = number;
	int numAns = 0;
	int a[10];
	int count = 0;
	for (int i = 0; i < numDigits - 1; i++) {
//		temp = tryNum;
		tryNum = pow(10, numDigits - 1) * (tryNum % 10) + tryNum / 10;
		if (tryNum >= startNum && tryNum <= endNum && tryNum < number) {
			bool check = true;
			for (int j = 0; j < count; j++)
				if (tryNum == a[j])
					check = false;
			a[count++] = tryNum;
			//printf ("%d %d %d\n", number, tryNum, count);
			if (check)
				numAns++;
		}
	}
	return numAns;
}

int main() {
	FILE *in = fopen ("C-large.in", "r");
	FILE *out = fopen ("C-large.out", "w");
	int numCase;
	fscanf (in, "%d\n", &numCase);
	for (int i = 0; i < numCase; i++) {
		fscanf (in, "%d %d\n", &startNum, &endNum);
		int numRecyclable = 0;
		for (int j = startNum; j <= endNum; j++) {
			numRecyclable += recycleStartFrom(j);
		}
		fprintf (out, "Case #%d: %d\n", i + 1, numRecyclable);
	}
	return 0;
}