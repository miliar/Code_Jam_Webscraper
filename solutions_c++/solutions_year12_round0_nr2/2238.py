#include <fstream>
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
    int T;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        int N, S, p, x, counter = 0;
        scanf("%d %d %d", &N, &S, &p);
        for (int j = 0; j < N; j++) {
            scanf(" %d", &x);
            if (x >= (3 * p - 2)) {
                counter++;
            }
            else if (p > 1 && x >= (3 * p - 4) && S > 0) {
                S--;
                counter++;
            }
        }
        printf("Case #%d: %d\n", i + 1, counter);
    }

    return 0;
}

