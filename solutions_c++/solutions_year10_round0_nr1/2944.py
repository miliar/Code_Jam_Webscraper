#include <iostream>
using namespace std;

int powtwo(int b)
{
    int ret = 1;
    for (int i = 0; i < b; i++) {
        ret *= 2;
    }
    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int N, K;
        scanf("%d %d", &N, &K);
        printf("Case #%d: ", i + 1);
        int tmp = powtwo(N);
        if (K % tmp == tmp - 1) {
            printf("ON\n");
        } else {
            printf("OFF\n");
        } 
    }
}
