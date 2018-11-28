#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <map>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

#define MAX 20

typedef pair<int,int> pii;

int geti() { int n; scanf("%d", &n); return n; }

#define i(n) for (int i = 0; i < (n); i++)
#define j(n) for (int j = 0; j < (n); j++)

char line[100];

int N, nDistinct;
long long sum;
map<char, int> M;

int flip(int a) {
	if (a == 0) {
		return 1;
	} else if (a == 1) {
		return 0;
	} else {
		return a;
	}
}

void setup() {
	M.clear();
	nDistinct = 0;
	sum = 0;
	memset(line, 0, 100 * sizeof(char));
	gets(line);
}

void doIt() {
	int nums[70];
	int i = 0;
	for (; line[i] != '\0'; i++) {
		char c = line[i];
		if (M.find(c) == M.end()) {
			M[c] = flip(nDistinct);
			nDistinct++;
		}
		nums[i] = M[c];
	}
	long long base = M.size();
	if (base == 1) base = 2;

	i--;

	long long val = 1;

	for (; i >= 0; i--) {
		sum += nums[i] * val;
		val *= base;
	}
}

int Case;

void print() {
	printf("Case #%d: %lld\n", Case, sum);
}

int main() {

	//freopen("A-test.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	N = geti();

	getc(stdin);

	for (Case = 1; Case <= N; Case++) {
		setup();
		doIt();
		print();
	}
}