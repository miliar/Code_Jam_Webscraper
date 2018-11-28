#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int data[1010], found[1010];

int main () {
    int tcc;
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    scanf("%d",&tcc);
    
    for (int i = 0; i < tcc; ++i) {
        int R, k, N;
        scanf("%d%d%d", &R, &k, &N);
        for (int j = 0; j < N; ++j)
            scanf("%d",&data[j]);
            
        int awal = 0;
        int ans = 0;
        for (int j = 0; j < R; ++j) {
            int hasil = 0;
            memset(found, -1, sizeof(found));
            while (hasil + data[awal] <= k) {
                  hasil+=data[awal];
                  found[awal]=1;
                  awal=(awal + 1) % N;
                  if (found[awal] == 1) break;
            }
            ans+=hasil;
        }
        printf("Case #%d: %d\n", i+1, ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
