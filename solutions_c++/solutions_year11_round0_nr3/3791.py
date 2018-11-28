#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int tc, n;
int A;

int main(){
    freopen("C.txt","r",stdin);
    freopen("Cans.txt","w",stdout);
    cin >> tc;
    for (int TC = 1; TC <= tc; TC++){
        cin >> n;
        int sum =0, total = 0, mint = 1000000000;
        for (int i = 0; i < n; i++){ 
            cin >> A;
            sum ^= A;
            total += A;
            mint = min(mint, A);
        }
        printf("Case #%d: ",TC);
        if (sum != 0){
            printf("NO\n");
        }else printf("%d\n",total-mint);
    }
    return 0;
}
