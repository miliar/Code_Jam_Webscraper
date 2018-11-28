#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

int main (int argc, char *argv [])
{
    int T = 0;

	int N = 0;
    int S = 0;
    int p = 0;

    int j = 0;
    int i = 1;

	cin >> T;

    while (T)
	{
		int ans = 0;
		int sum = 0;

		cin >> N >> S >> p;

		for (j = 0; j < N; j ++) {
			cin >> sum; 

			if (sum >= (max((p - 1), 0) + max((p - 1), 0) + p)) {
				ans ++;
			} else if (S > 0) {
				if (sum - p >= (2 * max((p - 2), 0))) {
					ans ++;
					S --;
				}
			}
		}

		printf ("Case #%d: %d\n", i, ans);

		i ++;
		T --;
    }

    return 0;
}
