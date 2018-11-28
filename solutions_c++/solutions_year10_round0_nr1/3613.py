#include <iostream>
#include <cstdio>
using namespace std;
int f[50];

void khoitao() {
     f[1] = 1;
     for (int i = 2; i <= 30; i++)
         f[i] = 1 + f[i-1] * 2;
}

int main() {
    freopen("A-large.in","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    khoitao();
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        int n, k;
        scanf("%d%d",&n,&k);
        if (f[n] > k) printf("OFF\n");
        else
        if (f[n] == k ) printf("ON\n");
        else {
             k = k % (f[n] + 1);
             if (f[n] > k) printf("OFF\n");
             else printf("ON\n");
        }
    }
}
