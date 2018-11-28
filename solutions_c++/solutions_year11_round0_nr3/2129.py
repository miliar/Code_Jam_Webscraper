#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

#define pb push_back
#define fs first
#define sc second

using namespace std;

int main(void){
    int test;

    scanf ("%d", &test);

    for (int t=0;t<test;++t){
        int n, tmp,miny = 1000001, xSum=0;
        long long sum = 0LL;

        scanf("%d", &n);
        for (int i=0;i<n;++i){
            scanf("%d", &tmp);
            xSum^=tmp;
            sum+=(long long)tmp;
            miny=min(miny,tmp);
        }
        if ( xSum == 0){
            printf ("Case #%d: %lld\n", t+1, sum-(long long) miny);
        }else{
            printf ("Case #%d: NO\n", t+1);
        }
    }

    return 0;
}
