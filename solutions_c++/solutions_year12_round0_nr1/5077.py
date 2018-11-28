#include <iostream>
#include <fstream>
#include <cstdio>

#include <cstring>

char mask[27] = "yhesocvxduiglbkrztnwjpfmaq";

void solveTestCase() {
	char buf[200];
	fgets(buf, 200, stdin);
//	scanf("%d%*c", &n);
	int n = strlen(buf);
	for (int i = 0; i < n; ++i) {
		if ('a' <= buf[i] && buf[i] <= 'z') {
			buf[i] = mask[buf[i] - 'a'];
		}
	}
	printf("%s", buf);
}

void solveTheProblem(void) {
	int n;
	scanf("%d%*c", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: ", i + 1);
		solveTestCase();
	}
}

int main(void) {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solveTheProblem();
	return 0;
}