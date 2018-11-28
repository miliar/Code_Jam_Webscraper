#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

bool isValid(int N, int PD, int PG) {
	if (100 / gcd(100, PD) > N) {
		return false;
	}
	if (PG != 0 && PG != 100) {
		return true;
	} else if (PG == 0) {
		return PD == 0;
	} else {
		return PD == 100;
	}
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		int N, PD, PG;
		scanf("%d%d%d", &N, &PD, &PG);
		printf("Case #%d: %s\n", oo + 1, isValid(N, PD, PG) ? "Possible" : "Broken");
	}
}
