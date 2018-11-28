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
    int C = 0;

    int i = 0;
    int j = 0;

    cin >> T;

    while (T)
	{
        vector <int> candies;
		T --;

        cin >> N;

		for (j = 0; j < N; j ++) {
            int l;
            cin >> l;
            candies.push_back (l);
        }

        sort (candies.begin (), candies.end ());

        int ans = candies [0];
        int total = candies [0];

        for (j = 1; j < N; j ++) {
            ans ^= candies [j];
            total += candies [j];
        }

        if (ans) {
		    printf ("Case #%d: NO\n", i + 1);
        } else {
            for (j = 0; j < N; j ++) {
                if (total ^ candies [j] == candies [j]) {
		            printf ("Case #%d: %d\n", i + 1, total - candies [j]);
                    break;
                }
            }
        }
		i ++;
    }

    return 0;
}
