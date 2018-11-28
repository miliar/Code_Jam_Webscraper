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
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

int main()
{
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        int len, walkS, runS, maxrun, n;
        scanf("%d%d%d%d%d", &len, &walkS, &runS, &maxrun, &n);
        int leftLen = len;
        vector<pair<int,int> > a;
        for (int i = 0; i < n; i ++) {
            int begin, end, wi;
            scanf("%d%d%d", &begin, &end, &wi);
            a.push_back(make_pair(wi, end - begin));
            leftLen -= end - begin;
        }
        if (leftLen > 0) {
            a.push_back(make_pair(0, leftLen));
        }
        sort(a.begin(), a.end());
        double leftRun = maxrun;
        double ansTime = 0;
        for (int i = 0; i < a.size(); i ++) {
            double wi = a[i].first;
            double l = a[i].second;
            double neck = min(leftRun, l / (wi + runS));
            leftRun -= neck;
            ansTime += neck + (l - (wi + runS) * neck) / (wi + walkS);
        }
        printf("Case #%d: %.10lf\n", ++cas, ansTime);
    }
}
