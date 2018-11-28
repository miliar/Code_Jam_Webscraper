#include <stdio.h>

int main(void) {
    int test;
    int n, k;
    int temp;
    bool ret;

    scanf("%d", &test);
    for(int i=1 ; i<=test ; i++) {
        scanf("%d %d", &n, &k);

        temp = 1;
        for(int j=0 ; j<n ; j++) {
            temp = temp*2;
        }

        ret = (k+1)%temp;
        printf("Case #%d: %s\n", i, (ret == true) ? "OFF" : "ON");
    }

    return 0;
}
