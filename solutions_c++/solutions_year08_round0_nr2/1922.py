#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

const int MaxT = 200 + 20;

struct Trip {
	int st, ed, type;
} trip[MaxT];

int na, nb, t;
char t1[10], t2[10];

bool visited[MaxT];

void init();
void work();

int main() {
	int totCase;
	scanf("%d", &totCase);
	for (int caseNum = 0; caseNum < totCase; ++caseNum) {
		init();
		printf("Case #%d: ", caseNum + 1);
		work();
	}
	return 0;
}

void init() {
	scanf("%d", &t);
	scanf("%d %d", &na, &nb);
	for (int i = 0; i < na + nb; ++i) {
		scanf("%s %s", t1, t2);
		trip[i].st = 10 * (t1[0] - '0') + t1[1] - '0';
		trip[i].st = trip[i].st * 60 + 10 * (t1[3] - '0') + t1[4] - '0';
		trip[i].ed = 10 * (t2[0] - '0') + t2[1] - '0';
		trip[i].ed = trip[i].ed * 60 + 10 * (t2[3] - '0') + t2[4] - '0';
		trip[i].type = 1;
	}
	for (int i = 0; i < na; ++i)
		trip[i].type = 0;
}

bool myCmp(const Trip & a, const Trip & b) {
	return a.st < b.st;
}

void work() {
	sort(trip, trip + na + nb, myCmp);
	fill(visited, visited + na + nb, false);
	int cntA = 0, cntB = 0;
	for (int i = 0; i < na + nb; ++i) {
		if (visited[i])
			continue;
		if (trip[i].type == 0)
			++cntA;
		else
			++cntB;
		visited[i] = true;
		int prev = i;
		for (int j = i + 1; j < na + nb; ++j) {
			if (visited[j])
				continue;
			if (trip[j].type == trip[prev].type)
				continue;
			if (trip[j].st >= trip[prev].ed + t) {
				visited[j] = true;
				prev = j;
			}
		}
	}
	printf("%d %d\n", cntA, cntB);
}
