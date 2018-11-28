#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <string>
#include <numeric>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <memory.h>

using namespace std;

int ret[] = {
1, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 
463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791,
135, 647
};

int main()
{
    int T = 0;
    cin >> T;

    double b = 3 + sqrt(5.0);
    for( int c = 1; c <= T; ++c )
    {
        int n;
        cin >> n;
        printf("Case #%d: %03d\n", c, ret[n]);
    }

	return 0;
}

