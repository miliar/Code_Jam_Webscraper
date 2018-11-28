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

bool ss[11000000];
long long n;
int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int T, ca = 0;
    ss[1] = 1;
    for (int i = 2; i <= 10000000; i++)
        if (!ss[i])
            for (int j = 2; i * j <= 10000000; j++)
                ss[i * j] = 1;
    for (scanf("%d", &T); T; T--) {
        cin >> n;
        int ansmax = 1, ansmin = 0;
        int li = (int)sqrt(n) + 5;
        if (n < 1000)
            li = n;
        for (int i = 2; i <= li; i++)
            if (!ss[i]) {
                ansmin++;
                long long tmp = i;
                while (tmp <= n) tmp *= i, ansmax++;
            }
        ansmin = max(ansmin, 1);
        printf("Case #%d: %d\n", ++ca, ansmax - ansmin);
    }
}
