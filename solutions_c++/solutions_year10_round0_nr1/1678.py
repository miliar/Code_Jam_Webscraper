#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

int main () {
	int n, k, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", cas, k % (1<<n) == (1<<n) - 1 ? "ON" : "OFF");
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}


