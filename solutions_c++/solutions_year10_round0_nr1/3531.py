#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        int n, k;
        scanf("%d %d", &n, &k);
        bool on = (k % (1<<n)) == ((1<<n)-1);
        printf("Case #%d: %s\n", i, on ? "ON" : "OFF");
    }
    return 0;
}
