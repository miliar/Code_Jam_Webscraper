#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int T,N,cur,check,sum;
vector<int> candy;
int main() {
    scanf("%d",&T);
    for (int i = 1; i <= T; ++i) {
        candy.clear();
        scanf("%d",&N);
        check = 0;
        for (int j = 0; j < N; ++j) {
            scanf("%d",&cur);
            candy.push_back(cur);
            check ^= cur;
        }
        if (check) {
            printf("Case #%d: NO\n",i);
            continue;
        }
        sort(candy.begin(),candy.end());
        sum = 0;
        for (int j = 1; j < candy.size(); ++j) {
            sum += candy[j];
        }
        printf("Case #%d: %d\n",i,sum);
    }
}
