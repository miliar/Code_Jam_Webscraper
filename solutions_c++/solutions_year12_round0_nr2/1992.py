#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;
int num[200];
int cnt[200];
int main (){
    freopen ("Bin.in","r",stdin);
    freopen ("Bout.out","w",stdout);
    int test ,ans;
    scanf ("%d",&test);
    int n ,s ,p;
    for (int t=1 ;t<=test ;t++){
        ans = 0;
        memset (cnt ,0 ,sizeof (cnt));
        scanf ("%d%d%d",&n,&s,&p);
        for (int i=1 ;i<=n; i++){
            scanf ("%d",&num[i]);
            cnt[num[i]]++;
        }
        int ck ,cp;
        if (p >= 2){
            ck = p*3-4; cp = min (cnt[ck] ,s);
            cnt[ck] -= cp;
            s -= cp;
            ans += cp;
            cnt[ck] = 0;
        }
        if (p >= 2){
            ck = p*3-3; cp = min (cnt[ck] ,s);
            cnt[ck] -= cp;
            s -= cp;
            ans += cp;
            cnt[ck] = 0;
        }
        int si ,li ,mn;
        for (int i=0 ;i<=30 ;i++){
            si = i/3;
            li = i%3;
            if (li == 0){
                mn = si+1;
                if (i == 0 || i == 30)  mn--;
            }
            else if (li == 1){
                mn = si+1; 
            }
            else{
                mn = si+2;
                if (i == 29)  mn--;
            }
            if (mn >= p)
               ans += cnt[i];
        }
        printf ("Case #%d: %d\n",t,ans);
    }
    return 0;
}
