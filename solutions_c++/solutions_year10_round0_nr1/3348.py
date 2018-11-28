#include <iostream>

using namespace std;

int main (){

    int t, cases = 1, n, k;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d", &n, &k);
        printf("Case #%d: ", cases++);
        k = k % (1 << n);

        if(__builtin_popcount(k) == n)
            printf("ON\n");
        else
            printf("OFF\n");
        
    }

    return 0;
}
