#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <vector>

#include <limits.h>
#include <math.h>
#include <stdio.h>

using namespace std;

#define foreach(k, b, N) for (int k = b; k <= N; k++)
#define foreach_r(k, b, N) for (int k = b; k >= N; k--)

int n[20000];

int
main()
{
	int cases; 
	int result = 0;

	cin >> cases;

	foreach(i, 1, cases) {
		int N, L, H;

		result = 0;
		cin >> N >> L >> H;

		foreach(j, 0, N - 1) {
			cin >> n[j];
		}

		int possible;
		foreach(j, L, H) {
			possible = 1;
			foreach(k, 0, N - 1) {
				if (n[k] % j != 0 && j % n[k] != 0) {
					possible = 0;
					break;
				}
			}

			if (possible == 1) {
				result = j;
				break;
			}
		}

		if (result == 0)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %d\n", i, result);
	}

	return 0;
}
