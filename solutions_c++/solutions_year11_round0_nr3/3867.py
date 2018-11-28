#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

vector<int> candy;
int res;
int S;

void foo(int idx, int s1, int s2, int sum) {
    if(idx>=candy.size()) {
        if(s1==s2 && sum!=S) res = max(res, sum);
        return;
    }

    foo(idx+1, s1^candy[idx], s2, sum+candy[idx]);
    foo(idx+1, s1, s2^candy[idx], sum);
}

int main() {
    int T;
    int N;
    int sum;

    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        cin >> N;


        S=0;
        vector<int> v(N);
        for(int i=0;i<N;i++) { cin >> v[i]; S+=v[i]; }

        candy = v;
        res = -1;
        foo(0, 0,0,0);
        
        if(res < 0) printf("Case #%d: NO\n", tc);
        else printf("Case #%d: %d\n", tc, res);

    }

    return 0;
}
