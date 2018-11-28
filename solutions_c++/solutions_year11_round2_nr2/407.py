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

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
const double eps = 1e-6;
bool comp(double a, double b) {
    if (fabs(a - b) < eps) return 0;
    else return a > b;
}
void solve() {
    int C, D, num, pos;
    PII point[210];
    scanf("%d%d", &C, &D);
   // cerr<<C<<" "<<D<<endl;
    for (int i = 0; i < C; i++) {
        scanf("%d%d", &pos, &num);
        //cerr<<pos<<" "<<num<<endl;
        point[i] = make_pair(pos, num);
    }
    double low = 0, high = 1e+14;
    for (int i = 0; i < 200; i++) {
        double mid = (low + high) / 2;
        //cerr<<mid<<endl;
        double leftMost = point[0].first - mid;
        bool valid = true;
        for (int i = 0; i < C && valid; i++) {
            int total = point[i].second;
            while (total && valid) {
                //cerr<<fabs(leftMost - point[i].first)<<endl;
                total--;
                if (point[i].first + mid < leftMost)
                    valid = false;
                else {
                    if (total == 0) {
                        if (i != C - 1)
                            leftMost = max(point[i + 1].first - mid, leftMost + D);
                        else leftMost = leftMost + D;
                    }
                    else leftMost = max(point[i].first - mid, leftMost + D);
                }
            }
        }
        if (valid)
            high = mid;
        else low = mid;
    }
    printf("%.7lf\n", (low + high) / 2.0);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int totalCase;
    scanf("%d", &totalCase);
    for (int Case = 1; Case <= totalCase; Case++) {
        printf("Case #%d: ", Case);
        solve();
        cerr<<"Test "<<Case<<" out of "<<totalCase<<" completed."<<endl;
    }
}
