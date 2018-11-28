#include <iostream>
#include <vector>
#include <bitset>
#include <map>
#include <algorithm>

using namespace std;

bool T[10240];

int patrickValue(vector<int> a, int p, int q) {
    int ret = 0;
    for(int i=p; i <= q; i++) {
        ret ^= a[i];
    }
    return ret;
}

int sum(vector<int> a, int p, int q) {
    int ret = 0;
    for(int i=p; i <= q; i++) {
        ret += a[i];
    }
    return ret;
}

int myMax(int x, int y, int z)
{
    int max = x;
    if(max < y)
        max = y;
    if(max < z)
        max = z;
    return max;
}

int main() {
    int N, M;
    scanf("%d", &N);
    vector<int> sums;
    for(int cases=0; cases < N; cases++) {
        scanf("%d", &M);
        sums.clear();
        for(int j=0; j < M; j++) {
            int temp;
            scanf("%d", &temp);
            sums.push_back(temp);
        }
        sort(sums.begin(), sums.end());
        int sz = sums.size();
        int sean = 0;
        for(int k=0; k <= sz - 2; k++) {
            if(patrickValue(sums, 0,k) == patrickValue(sums, k+1, sz-1)) {
                int left = sum(sums, 0, k);
                int right = sum(sums, k+1, sz-1);
                sean = myMax(left, right, sean);
            }
        }
        if(sean > 0) {
            printf("Case #%d: %d\n", cases+1, sean);
        } else {
            printf("Case #%d: %s\n", cases+1, "NO");
        }
    }
    return 0;
}