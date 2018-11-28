#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define LL long long

using namespace std;

int main () {
    int tcc;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&tcc);
    for (int i = 0; i < tcc; ++i) {
        int a, b;
        scanf("%d%d", &a, &b);
        LL z = 1LL << a;
        if (((LL) b + 1LL) % (LL) z == 0LL) printf("Case #%d: ON\n", i+1);
        else printf("Case #%d: OFF\n",i+1);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
