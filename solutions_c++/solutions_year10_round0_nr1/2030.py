#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
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
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
//typedef long long LL;
typedef complex<double> tComp;

int main(int argc, char **argv) {
    //     freopen("A.in","r",stdin);

//      freopen("A-small-attempt0.in","r",stdin);
//      freopen("A-small-attempt0.out","w",stdout);

//      freopen("A-small-attempt1.in","r",stdin);
//      freopen("A-small-attempt1.out","w",stdout);

//     freopen("A-small-attempt2.in","r",stdin);
//     freopen("A-small-attempt2.out","w",stdout);

     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);

    int ntestcases = 0;
    scanf("%d\n", &ntestcases);

    int testcase = 0;
    while (testcase < ntestcases) {

        int N = 0;
        int K = 0;
        scanf("%d %d", &N, &K);

        bool light_on = false;
        int f_N = 1 << N;
//         printf("2^%d=%d\n", N, f_N);
        if (K > 0 && (K - (f_N - 1)) >= 0) {
            if (((K - (f_N - 1)) % f_N) == 0) {
                light_on = true;
            }
        }

        printf("Case #%d: ", testcase + 1);
        if (light_on) {
            printf("ON");
        } else {
            printf("OFF");
        }
        printf("\n");

        ++testcase;
    }

    return 0;
}
