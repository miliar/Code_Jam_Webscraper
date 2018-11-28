#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int getdecplace(int number) {
    int dec = 1;
    while((dec*10) <= number) {
        dec*=10;
    }
    return dec;
}

int test(int num, int a, int b, int decplace) {
    int recycled = num;
    int counter = 0;

    do {

        int last = recycled % 10;
        recycled /= 10;
        recycled += (last * decplace);

        if((num < recycled) && (recycled <= b)) {
            counter++;
        }

    } while(recycled != num);

    return counter;
}


int main() {

    int t;
    scanf("%d\n", &t);

    for(int tt=0; tt<t; ++tt) {
        int a, b;
        scanf("%d %d", &a, &b);

        int result = 0;

        if(b < 10) {
            printf("Case #%d: %d\n", tt+1, 0);
            continue;
        }

        int decplace = getdecplace(a);

        for(int i=a; i<=b; ++i) {
            result += test(i,a,b,decplace);
        }

        printf("Case #%d: %d\n", tt+1, result);
    }

    return 0;
}
