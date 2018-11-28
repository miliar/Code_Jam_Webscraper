#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;
const double EPS = 1.0e-9;

int main(void)
{
    int T, n, tmp;
    cin >> T;
    for (int caseId = 1; caseId <= T; caseId++) {
        cin >> n;
        vector<long long> x(n), y(n);
        for (int i = 0; i < n; i++) 
            cin >> x[i];
        for (int i = 0; i < n; i++) 
            cin >> y[i];
        sort(x.begin(), x.end());
        sort(y.rbegin(), y.rend());
        long long product = 0;
        for (int i = 0; i < n; i++)
            product += x[i] * y[i];
        cout << "Case #" << caseId << ": " << product << endl;
    }

    return 0;
}

