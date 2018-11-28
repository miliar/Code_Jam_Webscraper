#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std; 

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int N, T, K;
	int caseT = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d", &N, &K);
		K = K % (1<<N);
		N = (1<<N) - 1;
		printf("Case #%d: ", caseT++);
		if(N == K) puts("ON");
		else puts("OFF");
	}

	return 0;
}