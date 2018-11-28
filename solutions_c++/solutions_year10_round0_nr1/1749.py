#include <iostream>
#include <algorithm>

using namespace std;

void solve(int n, int k){
    int mask = 1;
    for(int i=0; i<n; i++){
        if((k & mask) == 0){
            printf("OFF");
            return;
        }
        mask = mask << 1;
    }
    printf("ON");
    return;
}

int main(){
    int t;
    int n, k;
    cin >> t;
    for(int i=0; i<t; i++){
        cin >> n >> k;
        printf("Case #%d: ", i+1);
        solve(n, k);
        printf("\n");
    }

    return 0;
}
