#include <iostream>
#include <cstdio>
#include <memory.h>
using namespace std;

void solve(){
     int c, d, n;
     char form[256][256];
     bool opposed[256][256];
     int isnow[256];
     memset(form, 0, sizeof form);
     memset(opposed, 0, sizeof opposed);
     memset(isnow, 0, sizeof isnow);
     char t1, t2, t3;
     scanf("%d", &c);
     for (int i=0; i<c; ++i){
         scanf(" %c%c%c", &t1, &t2, &t3);
         form[t1][t2]=form[t2][t1]=t3;
     }
     scanf("%d", &d);
     for (int i=0; i<d; ++i){
         scanf(" %c%c", &t1, &t2);
         opposed[t1][t2]=opposed[t2][t1]=true;
     }
     char ans[1000];
     int mx=0;
     scanf("%d ", &n);
     for (int i=0; i<n; ++i){
         scanf("%c", &t1);
         if (mx==0){
            ans[mx++]=t1;
            isnow[t1]++;
            continue;
         }
         if (form[t1][ans[mx-1]]!=0){
            isnow[ans[mx-1]]--;
            ans[mx-1]=form[t1][ans[mx-1]];
            isnow[ans[mx-1]]++;
            continue;
         }
         for (int j=0; j<256; ++j)
             if (isnow[j]>0 && opposed[t1][j]){
                memset(isnow, 0, sizeof isnow);
                mx=0;
                break;
             }
         if (mx==0) continue;
         ans[mx++]=t1;
         isnow[t1]++;
     }
     printf("[");
     for (int i=0; i<mx-1; ++i)
         printf("%c, ", ans[i]);
     if (mx!=0) printf("%c", ans[mx-1]);
     printf("]\n");
}

int main(){
    int t;
    char fin[100], fout[100];
    printf("Input file: ");
    gets(fin);
    printf("Output file: ");
    gets(fout);
    freopen(fin, "r", stdin);
    freopen(fout, "w", stdout);
    scanf("%d", &t);
    for (int i=0; i<t; ++i){
        printf("Case #%d: ", i+1);
        solve();
    }
}
