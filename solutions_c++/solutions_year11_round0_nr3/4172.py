#include <iostream>
#include <cstdio>
using namespace std;

int n;
int a[1000];

bool solvable(){
    int res = a[0];
    for(int i = 1; i < n; i++){
        res ^= a[i];
    }
    if(res == 0) return true;
    return false;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d",&T);

    for(int tc = 1; tc <= T; tc++){
        int sum = 0;
        int Min = 10000000;
        scanf("%d",&n);
        for(int i = 0; i < n; i++){
            scanf("%d", &a[i]);
            sum += a[i];
            Min = min(Min,a[i]);
        }

        if(solvable()){
            sum = sum - Min;
            printf("Case #%d: %d\n",tc,sum);
        }
        else{
            printf("Case #%d: NO\n",tc);
        }
    }
}
