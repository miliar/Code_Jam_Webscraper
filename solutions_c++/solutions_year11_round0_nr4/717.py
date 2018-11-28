#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 10010;

int a[maxn];
int n;


int main(){
//    freopen("D-large.in", "r", stdin);
//    freopen("out.txt", "w", stdout);

    int T;

    cin >> T;

    for(int k = 1; k <= T; k ++){
        cin >> n;
        for(int i = 1; i <= n; i ++){
            scanf("%d", &a[i]);
        }
        if(n == 1){
             printf("Case #%d: 0.000000\n", k);
             continue;
        }

        int ret = 0;
        for(int i = 1; i <= n; i ++)
            if(a[i] == i)
                ret ++;

        printf("Case #%d: %d.000000\n", k, n - ret);

//        Solve(k);
    }

    return 0;
}
