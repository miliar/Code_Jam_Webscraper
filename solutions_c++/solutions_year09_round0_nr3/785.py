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

char W[] = "\0welcome to code jam";
char line[10000];
long long A[MAX];

int N;

void setup() {
	memset(A, 0, MAX * sizeof(long long));
	A[0] = 1;
	memset(line, 0, 10000 * sizeof(char));
	fgets(line, 10000, stdin);
}

void doIt() {
	for (int i = 0; line[i] != '\n'; i++) {
		for (int k = 1; k < MAX; k++) {
			if (line[i] == W[k]) {
				A[k] += A[k-1];
				A[k] %= 10000;
			}
		}
	}
}

int Case;

void print() {
	printf("Case #%d: %04lld\n", Case, A[MAX-1]);
}

int main() {

	//freopen("C-test.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	N = geti();

	scanf("%*c");

	for (Case = 1; Case <= N; Case++) {
		setup();
		doIt();
		print();
	}
}