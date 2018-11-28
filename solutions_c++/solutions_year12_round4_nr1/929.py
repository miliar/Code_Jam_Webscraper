#include<iostream>
#include<cstring>
#include<cstdio>
#define MAX(a,b) a = max(a,b)

using namespace std;

int best[60002],panjang[60002],posisi[60002];
int kasus,banyak;

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d",&banyak);
        for (int i=1;i<=banyak;++i) scanf("%d %d",&posisi[i],&panjang[i]);
        panjang[banyak+1] = 1;
        scanf("%d",&posisi[banyak+1]);
        
        memset(best,0,sizeof(best));
        best[1] = posisi[1];
        
        for (int i=1;i<=banyak;++i) {
            if (!best[i]) continue;
            int indeks = i+1;
            while ((indeks <= banyak+1)&&(posisi[i] + best[i] >= posisi[indeks])) {
                MAX(best[indeks], min(panjang[indeks], posisi[indeks]-posisi[i]));
                ++indeks;
            }
        }
        
        printf("Case #%d: ",l);
        if (best[banyak+1]) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
