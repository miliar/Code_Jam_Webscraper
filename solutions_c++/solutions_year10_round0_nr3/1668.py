#include <cstdlib>
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
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x) {
    return x*x;
}

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()



int main(int argc, char** argv) {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ++ti) {
        int R, K, N;
        int rec[1005] = {0};
        scanf("%d%d%d", &R, &K, &N);
        LL arr[1005] = {0};
        for (int i = 0; i < N; ++i) scanf("%lld", &arr[i]);
        int pos = 0;
        int prevnum = 0, cirnum = 0;
        vector <LL> totsum;
		totsum.PB(0);
        int tot = 0;
        while (rec[pos] == 0) {
            rec[pos] = ++tot;
            int tmp = arr[pos];
            int i = (pos+1)%N;
            for (; tmp + arr[i] <= K && i != pos; i = (i + 1) % N) {
                tmp += arr[i];
            }
            totsum.PB(totsum[totsum.size() - 1] + tmp);
            pos = i % N;
        }
        prevnum = rec[pos] - 1;
        cirnum = totsum.size() - prevnum-1;
        printf("Case #%d: ", ti + 1);
        if (R <= prevnum) printf("%lld\n", totsum[R]);
        else {
            LL res=totsum[prevnum];
            R-=prevnum;
            res += (totsum[totsum.size()-1] - totsum[prevnum]) * (R / cirnum);
            if(R%cirnum!=0) res += totsum[R % cirnum + prevnum] - totsum[prevnum];
            printf("%lld\n", res);
        }
    }
    return (EXIT_SUCCESS);
}

