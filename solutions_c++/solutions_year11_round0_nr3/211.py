#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
#define N 1111
int array[N],n;
int main(){
    int i,j,k;
    int cas,sum,Min;
    //freopen("C.in","r",stdin);
    //freopen("C.out","w",stdout);
    scanf("%d",&cas);
    for(k = 1; k <= cas; k++){
        scanf("%d",&n);
        for(i = 1,Min = 1000000,sum = 0; i <= n; i++){
            scanf("%d",&array[i]);
            sum += array[i];
            if(array[i] < Min) Min = array[i];
        }
        sum -= Min;
        bool flag = true;
        int cnt;
        for(i = 0;1; i++){
            cnt = 0;
            for(j = 1; j <= n; j++)
                if((1 << i) & array[j]) cnt++;
            if(cnt % 2 == 1) {flag = false; break;}
            for(j = 1; j <= n; j++)
                if((1 << i) <= array[j]) break;
            if(j == n+1) break;
        }
        if(flag) printf("Case #%d: %d\n",k,sum);
        else printf("Case #%d: NO\n",k);
    }
    return 0;
}
