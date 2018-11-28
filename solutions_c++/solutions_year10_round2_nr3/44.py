#include<iostream>
#include<cstring>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cassert>
#include<numeric>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

int MOD = 100003;

int cache[501][501];
int combi[501][501];

int go(int n);

int go2(int largest, int size) {
    if(largest <= size) return 0;
    if(size == 1)
        return 1;
    int& ret = cache[largest][size];
    if(ret != -1) return ret;
    ret = 0;
    for(int k = 1; k <= size - 1; ++k) {
        int shrinked = size - k;
        if(shrinked > largest - size) continue;
        long long add = go2(size, k);
        add = (add * combi[largest-size-1][shrinked-1]) % MOD;
        (ret += add) %= MOD;
    }
    return ret;
}

int go(int n) {
    int ret = 0;
    for(int i = 1; i <= n - 1; ++i)
        (ret += go2(n, i)) %= MOD;
    return ret;
}

int main()
{
    memset(cache, -1, sizeof(cache));
    memset(combi, 0, sizeof(combi));
    combi[0][0] = 1;
    for(int i = 1; i <= 500; ++i) {
        combi[i][0] = 1;
        for(int j = 1; j <= i; ++j)
        {
            combi[i][j] = (combi[i-1][j-1] + combi[i-1][j]) % MOD;
        }
    }
    int cases;
    scanf("%d", &cases);
    for(int cc = 0; cc < cases; ++cc)
    {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %d\n", cc+1, go(n));
    }
}

