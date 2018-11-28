#include <iostream>
#include <cstdio>
using namespace std;

void solve(){
     int n;
     int a[1000];
     scanf("%d", &n);
     for (int i=0; i<n; ++i)
         scanf("%d", &a[i]);
     int ans=-1;
     for (int i=1; i<(1<<n)-1; ++i){
         int t1=0, t2=0, s1=0, s2=0;
         for (int j=0; j<n; ++j){
             if (i&(1<<j)) t1^=a[j], s1+=a[j];
             else t2^=a[j], s2+=a[j];
         }
         if (t1==t2)
             ans=max(ans, max(s1, s2));
     }
     if (ans==-1)
        printf("NO\n");
     else
         printf("%d\n", ans);
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
