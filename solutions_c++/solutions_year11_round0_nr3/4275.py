#include <iostream>
using namespace std;
#define INF 1000000000 
int tests;
int sum = 0;
int main() {
    scanf("%d", &tests);
    int t = 0;
    while(tests > 0) {
        t++;
        tests--;
        int mini = INF;
        sum = 0;
        int n;
        int xori = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            int a;
            scanf("%d", &a);
            //std::cout << a << std::endl;
            if (i == 0) {
                xori = a;
            } else {
                xori ^= a;
            }
            //std::cout << xori << std::endl;
            sum += a;
            mini = min(mini, a);
        }
        //std::cout << mini << " " << xori << " " << sum << std::endl;
        if (xori != 0) {
            printf("Case #%d: NO\n", t);
            continue;
        } else {
            printf("Case #%d: %d\n", t, sum - mini);
        }
    }
    return 0;   
}
