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

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

int n, a1;
int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T, tt = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d", &n);
		int nn = n;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a1);
			if (i == a1)
				nn--;
		}
		tt++;
		printf("Case #%d: %d.000000\n", tt, nn);
		
	}
}
