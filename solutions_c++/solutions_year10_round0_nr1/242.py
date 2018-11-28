/**********************************************************************
Author: Felicia
Created Time:  2010/5/8 13:24:45
File Name: snapper.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;

int main() {
    freopen("D:\\snapper.out", "w", stdout);
    int T;
    int ca = 1;
    scanf("%d", &T);
    while (T--) {
        int n, k;
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", ca++);
        if ((k + 1) % (1 << n) == 0) {
            printf("ON");
        } else {
            printf("OFF");
        }
        printf("\n");
    }
    return 0;
}

