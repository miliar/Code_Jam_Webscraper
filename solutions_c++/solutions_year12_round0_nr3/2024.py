#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;
typedef long long lint;
int cnt[30];
int recy (int k ,int l);
int numlen (int k);
int main (){
    int t ,a ,b ,l ,k;
    freopen ("C.in","r",stdin);
    freopen ("C.out","w",stdout);
    lint ans;
    scanf ("%d",&t);
    for (int test=1 ;test<=t ;test++){
        ans = 0;
        scanf ("%d%d",&a,&b);
        l = max (numlen (a) ,numlen (b));
        bool flag;
        for (int i=a ;i<=b ;i++){
            k = i;
            cnt[0] = 0;
            //printf ("%d",k);
            for (int j=1 ;j<l ;j++){
                
                k = recy (k ,l);
                //printf ("->%d",k);
                if (k < i && k >= a){
                    flag = true;
                    for (int p=1 ;p<=cnt[0] ;p++){
                        if (cnt[p] == k)
                            flag = false;
                    }
                    if (flag){
                        cnt[++cnt[0]] = k;
                        //printf ("%d:%d\n",cnt[0],k);
                    }
                    //if (i == 1212)
                    //   printf("%d\n",cnt[cnt[0]-1]);
                    //ans++;
                }
                
            }
            //printf ("\n");
            ans += cnt[0];
            //for (int kc=1 ;kc<=cnt[0] ;kc++){
            //    printf ("%d\t%d\n",kc,cnt[kc]);
            //}
            //printf ("\n");
        }
        printf ("Case #%d: ",test);
        cout << ans << endl;
    }
    return 0;
}
int recy (int k ,int l){
    int mul = 1;
    for (int i=1 ;i<l ;i++){
        mul *= 10;
    }
    int p = k/mul+k%mul*10;
    return p;
}
int numlen (int k){
    int len = 0;
    while (k != 0){
        len++;
        k/=10;
    }
    return len;
}
