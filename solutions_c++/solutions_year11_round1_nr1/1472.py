#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int testc;
	scanf("%d", &testc);
	for (int i=1; i<=testc; ++i) {
		int N, Pd, Pg;
		scanf("%d%d%d", &N, &Pd, &Pg);
		printf("Case #%d: ", i);
		if (Pd > 0 && Pg == 0) printf("Broken\n");
		else if (Pd == 0 && Pg == 0) printf("Possible\n");
		else if (Pd < 100 && Pg == 100) printf("Broken\n");
		else {
			for (int t=1; t<=N; ++t) {
				if ((t * Pd) % 100 == 0) {
					for (int k=t*Pd/100; k<=100*t-t*Pd+1; ++k) if ((k * 100) % Pg == 0) {
						if (k*100/Pg >= t) {
							printf("Possible\n");
							goto next;
						}
					}
				}
			}
			printf("Broken\n");
		}
next:;
	}
	getchar();
	return 0;
}