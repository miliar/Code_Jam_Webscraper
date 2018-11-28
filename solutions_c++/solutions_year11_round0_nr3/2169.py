#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#define MAXN 1003
using namespace std;
const int INF=0x3f3f3f3f;
const double eps=1e-9;
typedef long long LL;
typedef pair<int, int> pii;

int n, var[MAXN];

int main() {
#ifndef ONLINE_JUDGE
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
#endif

    int dataset;
    scanf("%d", &dataset);
    for(int cas=1; cas<=dataset; ++cas) {
    	scanf("%d", &n);
    	int key=0, minV=1e9, sum=0;
    	for(int i=0; i<n; ++i) {
    		scanf("%d", &var[i]);
    		key^=var[i];
    		minV=min(minV, var[i]);
    		sum+=var[i];
    	}

    	if(key) {
    		printf("Case #%d: NO\n", cas);
    		continue;
    	}

    	printf("Case #%d: %d\n", cas, sum-minV);
    }

    return 0;
}
