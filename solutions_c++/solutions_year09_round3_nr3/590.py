#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
    int N;
    int Q,P;
    int p[200];

    cin >> N;
    for(int cc=1;cc<=N;cc++) {
        cin >> P >> Q;

        vector<int> v(Q);
        for(int i=0;i<Q;i++) cin >> v[i];
        sort(v.begin(), v.end());

        int mm=1000,coin;
        do {
            for(int i=1;i<=P;i++) p[i]=1;
            coin=0;
            for(int i=0;i<Q;i++) {
                p[v[i]]=0;
                for(int j=v[i]-1;j>=1 && p[j];j--) coin++;
                for(int j=v[i]+1;j<=P && p[j];j++) coin++;
            }
            
            mm = min(mm, coin);
        } while(next_permutation(v.begin(), v.end()));

        printf("Case #%d: %d\n", cc, mm);
    }

    return 0;
}
