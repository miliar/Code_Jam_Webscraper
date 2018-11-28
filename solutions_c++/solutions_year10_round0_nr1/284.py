#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		int n, k;
		cin >> n >> k;
		printf("Case #%d: ", t + 1);
		int m = (1 << n) - 1;
		if((k & m) == m) puts("ON");
		else puts("OFF");
	}
	return 0;
}
